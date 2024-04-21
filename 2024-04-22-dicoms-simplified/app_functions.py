import pydicom
import cv2

def return_information(dcm_file):
    infos_1 = f'''
    Image type: {dcm_file.ImageType} \n
    SOP Class UID: {dcm_file.SOPClassUID}\n
    SOP Instance UID: {dcm_file.SOPInstanceUID}\n
    Study Date: {dcm_file.StudyDate}\n
    Series Date: {dcm_file.SeriesDate}\n
    Content Date: {dcm_file.ContentDate}\n
    Study Time: {dcm_file.StudyTime}\n
    Series Time: {dcm_file.SeriesTime}\n
    Content Time: {dcm_file.ContentTime}\n
    Accession Number: {dcm_file.AccessionNumber}\n
    Modality: {dcm_file.Modality}\n
    Manufacturer: {dcm_file.Manufacturer}\n
    Referring Physician Name: {dcm_file.ReferringPhysicianName}\n
    Patient Name: {dcm_file.PatientName}\n
    Patient ID: {dcm_file.PatientID}\n
    Patient Birth Date: {dcm_file.PatientBirthDate}\n
    Patient Sex: {dcm_file.PatientSex}\n
    Slice Thickness: {dcm_file.SliceThickness}\n
    Patient Position: {dcm_file.PatientPosition}\n
    Study Instance UID: {dcm_file.StudyInstanceUID}\n
    Series Instance UID: {dcm_file.SeriesInstanceUID}\n
    '''
    infos_2 = f'''
    Study ID: {dcm_file.StudyID}\n
    Series Number: {dcm_file.SeriesNumber}\n
    Instance Number: {dcm_file.InstanceNumber}\n
    Image Position Patient: {dcm_file.ImagePositionPatient}\n
    Image Orientation Patient: {dcm_file.ImageOrientationPatient}\n
    Frame Of Reference UID: {dcm_file.FrameOfReferenceUID}\n
    Position Reference Indicator: {dcm_file.PositionReferenceIndicator}\n
    Samples Per Pixel: {dcm_file.SamplesPerPixel}\n
    Photometric Interpretation: {dcm_file.PhotometricInterpretation}\n
    Rows: {dcm_file.Rows}\n
    Columns: {dcm_file.Columns}\n
    Pixel Spacing: {dcm_file.PixelSpacing}\n
    Bits Allocated: {dcm_file.BitsAllocated}\n
    Bits Stored: {dcm_file.BitsStored}\n
    High Bit: {dcm_file.HighBit}\n
    Pixel Representation: {dcm_file.PixelRepresentation}\n
    Window Center: {dcm_file.WindowCenter}\n
    Window Width: {dcm_file.WindowWidth}\n
    Rescale Intercept: {dcm_file.RescaleIntercept}\n
    Rescale Slope: {dcm_file.RescaleSlope}\n
    RescaleType: {dcm_file.RescaleType}\n
    '''
    return infos_1, infos_2


def anonymize_case(dcm_file):
    dicom_file_data = pydicom.dcmread(dcm_file)

    dicom_file_data.PatientName = ''
    dicom_file_data.PatientBirthDate =''
    dicom_file_data.StudyID = ''
    dicom_file_data.PatientSex = ''

    return dicom_file_data

