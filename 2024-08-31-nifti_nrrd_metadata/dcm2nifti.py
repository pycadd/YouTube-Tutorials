# Dicom to nifti converter with metadata

import SimpleITK as sitk
import numpy as np
import nibabel as nib
import json
import base64

class SimpleDicomToNiftiConverter:
    def __init__(self, dicom_folder, output_nifti):
        self.dicom_folder = dicom_folder
        self.output_nifti = output_nifti

    def convert(self):
        # Read the DICOM series
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(self.dicom_folder)
        reader.SetFileNames(dicom_names)
        image = reader.Execute()

        # Create affine matrix for NIfTI
        spacing = image.GetSpacing()
        direction = image.GetDirection()
        origin = image.GetOrigin()
        affine = np.eye(4)
        affine[:3, :3] = np.array(direction).reshape(3, 3) * spacing
        affine[:3, 3] = origin

        # Convert SimpleITK image to Nibabel image
        image_array = sitk.GetArrayFromImage(image)
        nifti_image = nib.Nifti1Image(image_array, affine)

        # Add custom metadata as JSON
        custom_metadata = {"ExampleKey": "ExampleValue"}
        json_str = json.dumps(custom_metadata)
        encoded_json = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
        nifti_extension = nib.nifti1.Nifti1Extension(40, encoded_json.encode('utf-8'))
        nifti_image.header.extensions.append(nifti_extension)

        # Save the NIfTI image
        nib.save(nifti_image, self.output_nifti)
        print(f"NIfTI file saved successfully: {self.output_nifti}")