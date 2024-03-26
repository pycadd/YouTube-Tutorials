# Online DICOM Series and NIFTI Viewer

![Alt text](./assets/pycad.png)

## Introduction
This Python application utilizes Streamlit to provide a user-friendly interface for viewing DICOM and NIfTI medical imaging files in various orientations. It supports axial, coronal, and sagittal views for comprehensive analysis.

## Requirements
- Python
- Streamlit
- SimpleITK
- Numpy
- Matplotlib
- NiBabel

## Installation
Ensure Python is installed on your system. Then, install the required packages using the following command:

```bash
pip install streamlit SimpleITK numpy matplotlib nibabel
```

## Running the Application
To start the application, navigate to the directory containing the script and run:

```bash
streamlit run fancy_viewer.py
```

## Note
This application is designed for educational and demonstration purposes. It should not be used as a diagnostic tool.