# Medical Imaging Data Extraction with SimpleITK
![Alt text](../assets/pycad.png)

This Python script demonstrates how to extract and handle medical imaging data using the SimpleITK library. SimpleITK is a simplified interface to the Insight Segmentation and Registration Toolkit (ITK), designed to facilitate image analysis tasks in medical imaging. This example covers reading DICOM series, as well as single NIfTI and NRRD files, extracting both the pixel data and relevant metadata such as spacing, origin, and direction.

[Link to the video.](https://youtu.be/-Tcnoak4hP0?si=YyQtrJ02jwuVDpHg)

## Features

- **Extract Array and Metadata**: Converts SimpleITK image objects into NumPy arrays and extracts metadata.
- **Read DICOM Series**: Demonstrates how to read a series of DICOM images, which is common in medical imaging datasets.
- **Read NIfTI/NRRD Files**: Shows the process for reading single-file formats like NIfTI (.nii) and NRRD (.nrrd), widely used for storing medical imaging data.

## Prerequisites

To use this script, you need to have Python installed along with the following packages:
- SimpleITK
- NumPy (implicitly used by SimpleITK to return arrays)

You can install SimpleITK using pip:

```bash
pip install SimpleITK
```

## Usage
1. **DICOM Series**: To read a DICOM series, specify the path to the DICOM folder in `path_to_dicom_folder`, then call `read_dicom(path_to_dicom_folder)`. This will return a NumPy array of the image data and a dictionary containing the image metadata.

2. **NIfTI/NRRD Files**: To read a NIfTI or NRRD file, specify the file path in `path_to_nifti_nrrd_file`, then call `read_nifti_nrrd(path_to_nifti_nrrd_file)`. Similar to the DICOM series, this returns the image data as a NumPy array and its metadata.

## Code Structure
- `extract_array_metadat(sitk_image)`: Extracts the image data and metadata from a SimpleITK image object.
- `read_dicom(dicom_path)`: Reads a DICOM series from the given path.
- `read_nifti_nrrd(file_path)`: Reads a single NIfTI or NRRD file.

## Example Output
When run, this script prints the metadata and the shape of the NumPy array for both DICOM series and NIfTI/NRRD files, providing a simple way to verify the image data and its attributes.