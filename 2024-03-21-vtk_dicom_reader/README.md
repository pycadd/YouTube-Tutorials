# DICOM Series Viewer using VTK
![alt text](../assets/pycad.png)

DICOMViewer is a Python-based application designed for the visualization of DICOM (Digital Imaging and Communications in Medicine) images. It leverages the powerful Visualization Toolkit (VTK) to render DICOM images and provides functionality to view images in axial, coronal, and sagittal orientations. This tool aims to facilitate medical imaging research and education by providing an easy-to-use platform for DICOM image analysis.

## Key Features
- **DICOM Image Reading**: Utilizes `vtkDICOMImageReader` for efficient loading of DICOM image series.
- **Multiple View Orientations**: Supports viewing images in axial, coronal, and sagittal orientations through `vtkImageReslice`.
- **Interactive Image Navigation**: Allows users to navigate through image slices using keyboard inputs or mouse scrolling.
- **Customizable Visualization**: Offers text overlay for slice information and adjustable window size and background color.

## Requirements
- Python 3.6+
- VTK (Visualization Toolkit)

## Installation
Ensure you have Python installed on your system. You can install VTK using pip with the following command:

```bash
pip install vtk
```

## Usage
To use DICOMViewer, clone this repository to your local machine and navigate to the project directory. Run a script with:
```bash
python main.py
```

The main code is:
```python
# Specify the path to your DICOM folder
dicom_folder_path = r'path/to/dicom/folder'

# Create an instance of DICOMViewer with the DICOM folder path
viewer = DICOMViewer(dicom_folder=dicom_folder_path, view_orientation='sagittal')

# Render the DICOM series
viewer.render()
```