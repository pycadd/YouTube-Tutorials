# Dicom to nrrd converter with metadata

import SimpleITK as sitk

class SimpleDicomToNrrdConverter:
    def __init__(self, dicom_folder, output_nrrd):
        self.dicom_folder = dicom_folder
        self.output_nrrd = output_nrrd

    def convert(self):
        # Read the DICOM series
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(self.dicom_folder)
        reader.SetFileNames(dicom_names)
        image = reader.Execute()

        # Add custom metadata
        image.SetMetaData("ExampleKey", "ExampleValue")

        # Save as NRRD
        sitk.WriteImage(image, self.output_nrrd)
        print(f"NRRD file saved successfully: {self.output_nrrd}")

if __name__ == "__main__":
    dicom_folder = "path/to/dicom/folder"
    output_nrrd = "output.nrrd"
    converter = SimpleDicomToNrrdConverter(dicom_folder, output_nrrd)
    converter.convert()
