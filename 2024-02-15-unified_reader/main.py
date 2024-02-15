import SimpleITK as sitk

def extract_array_metadat(sitk_image: sitk.Image):
    '''
    Return the 3D numpy.array and the needed metadata for file creation (segmentation especially).
    '''
    np_array = sitk.GetArrayFromImage(sitk_image)
    metadata = {
        'spacing': sitk_image.GetSpacing(),
        'origin': sitk_image.GetOrigin(),
        'direction': sitk_image.GetDirection(),
    }

    return np_array, metadata

def read_dicom(dicom_path: str):
    '''
    Reads a folder of dicoms and returns the 3D array + the metadata
    '''
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dicom_path)
    reader.SetFileNames(dicom_names)
    image_sitk = reader.Execute()
    return extract_array_metadat(image_sitk)

def read_nifti_nrrd(file_path: str):
    '''
    Reads a NIFTI or NRRD file and returns the 3D array + the metadata
    '''
    image_sitk = sitk.ReadImage(file_path)
    return extract_array_metadat(image_sitk)


if __name__ == '__main__':
    path_nifti = 'path/to/dicom/folder'
    np_array, metadata = read_dicom(path_nifti)
    print(metadata)
    print(np_array.shape)

    path_nifti = 'path/to/nifti/nrrd/file'
    np_array, metadata = read_nifti_nrrd(path_nifti)
    print(metadata)
    print(np_array.shape)