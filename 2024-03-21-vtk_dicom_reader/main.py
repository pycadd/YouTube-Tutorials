import vtkmodules.all as vtk
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkRenderingCore import vtkActor2D, vtkRenderWindowInteractor, vtkTextMapper, vtkTextProperty
from vtkmodules.vtkImagingCore import vtkImageReslice



class CustomInteractorStyle(vtk.vtkInteractorStyleImage):
    def __init__(self, image_viewer, status_actor):
        super().__init__()
        self.AddObserver('MouseWheelForwardEvent', self.move_slice_forward)
        self.AddObserver('MouseWheelBackwardEvent', self.move_slice_backward)
        self.AddObserver('KeyPressEvent', self.key_press_event)
        self.image_viewer = image_viewer
        self.status_actor = status_actor
        self.slice = image_viewer.GetSliceMin()
        self.min_slice = image_viewer.GetSliceMin()
        self.max_slice = image_viewer.GetSliceMax()
        self.update_status_message()

    def update_status_message(self):
        # Update the status message with the current slice
        message = f'Slice Number {self.slice + 1}/{self.max_slice + 1}'
        self.status_actor.GetMapper().SetInput(message)

    def move_slice_forward(self, obj, event):
        if self.slice < self.max_slice:
            self.slice += 1
            self.image_viewer.SetSlice(self.slice)
            self.update_status_message()
            self.image_viewer.Render()

    def move_slice_backward(self, obj, event):
        if self.slice > self.min_slice:
            self.slice -= 1
            self.image_viewer.SetSlice(self.slice)
            self.update_status_message()
            self.image_viewer.Render()

    def key_press_event(self, obj, event):
        key = self.GetInteractor().GetKeySym()
        if key == 'Up':
            self.move_slice_forward(obj, event)
        elif key == 'Down':
            self.move_slice_backward(obj, event)


class DICOMViewer:
    def __init__(self, dicom_folder, view_orientation='axial'):
        '''
        The view orientation contols which orientation we want to display, here are the options:\n
        - axial
        - coronal
        - sagittal
        '''
        self.dicom_folder = dicom_folder
        self.view_orientation = view_orientation  # New attribute for view orientation
        self.colors = vtkNamedColors()
        self.setup_reader()
        self.setup_reslice()  # Call setup_reslice instead of setup_viewer directly
        self.setup_text_labels()
        self.configure_interactor()

    def setup_reader(self):
        self.reader = vtkDICOMImageReader()
        self.reader.SetDirectoryName(self.dicom_folder)
        self.reader.Update()

    def setup_reslice(self):
        self.reslice = vtkImageReslice()
        self.reslice.SetInputConnection(self.reader.GetOutputPort())

        # Set the output spacing to be 1, 1, 1. This is not strictly necessary but can be useful.
        self.reslice.SetOutputSpacing(1, 1, 1)

        if self.view_orientation == 'coronal':
            self.reslice.SetResliceAxesDirectionCosines(1,0,0, 0,0,1, 0,-1,0)
        elif self.view_orientation == 'sagittal':
            self.reslice.SetResliceAxesDirectionCosines(0,1,0, 0,0,1, 1,0,0)
        # Default is axial; no changes needed

        self.setup_viewer()

    def setup_viewer(self):
        self.image_viewer = vtkImageViewer2()
        self.image_viewer.SetInputConnection(self.reslice.GetOutputPort())
        # Rest of the setup_viewer method remains unchanged


    def setup_text_labels(self):
        self.slice_text_actor = self.create_text_actor("", 15, 10, 20, align_bottom=True)
        self.usage_text_actor = self.create_text_actor(
            "- Slice with mouse wheel or Up/Down-Key\n- Zoom with pressed right mouse button while dragging",
            0.05, 0.95, 14, normalized=True)

    def configure_interactor(self):
        self.interactor = vtkRenderWindowInteractor()
        self.interactor_style = CustomInteractorStyle(self.image_viewer, self.slice_text_actor)
        self.image_viewer.SetupInteractor(self.interactor)
        self.interactor.SetInteractorStyle(self.interactor_style)

    def create_text_actor(self, text, x, y, font_size, align_bottom=False, normalized=False):
        text_prop = vtkTextProperty()
        text_prop.SetFontFamilyToCourier()
        text_prop.SetFontSize(font_size)
        text_prop.SetVerticalJustificationToBottom() if align_bottom else text_prop.SetVerticalJustificationToTop()
        text_prop.SetJustificationToLeft()

        text_mapper = vtkTextMapper()
        text_mapper.SetInput(text)
        text_mapper.SetTextProperty(text_prop)

        text_actor = vtkActor2D()
        text_actor.SetMapper(text_mapper)
        if normalized:
            text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
        text_actor.SetPosition(x, y)

        return text_actor

    def update_status_message(self, message):
        self.slice_text_actor.GetMapper().SetInput(message)

    def render(self):
        self.image_viewer.GetRenderer().AddActor2D(self.slice_text_actor)
        self.image_viewer.GetRenderer().AddActor2D(self.usage_text_actor)
        self.image_viewer.Render()
        self.image_viewer.GetRenderer().ResetCamera()
        self.image_viewer.GetRenderer().SetBackground(self.colors.GetColor3d('Black'))
        self.image_viewer.GetRenderWindow().SetSize(800, 800)
        self.image_viewer.GetRenderWindow().SetWindowName('ReadDICOMSeries')
        self.interactor.Start()


if __name__ == '__main__':
    # Specify the path to your DICOM folder
    dicom_folder_path = r'path/to/dicom/folder'
    
    # Create an instance of DICOMViewer with the DICOM folder path
    viewer = DICOMViewer(dicom_folder=dicom_folder_path, view_orientation='sagittal')
    
    # Render the DICOM series
    viewer.render()

