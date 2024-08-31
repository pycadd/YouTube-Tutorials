# DICOM to Nifti and Nrrd with metadata

![alt text](../assets/pycad.png)


 [![Static Badge](https://img.shields.io/badge/PYCAD-Blog-%23ffc800?logoColor=ffc800&link=https%3A%2F%2Fpycad.co%2F)](https://pycad.co/) [![Static Badge](https://img.shields.io/badge/PYCAD-YouTube-%23e80202?logoColor=ffc800&link=https%3A%2F%2Fgithub.com%2Famine0110%2Fpycad%2Ftree%2Fmain%2Fdocs)](https://www.youtube.com/channel/UCdYyILlPlehK4fKS5DiuMXQ) [![Static Badge](https://img.shields.io/badge/PYCAD-Portfolio-%23eb5d10?logoColor=ffc800&link=https%3A%2F%2Fgithub.com%2Famine0110%2Fpycad%2Ftree%2Fmain%2Fdocs)](https://pycad.co/portfolio/)

This repository contains two Python scripts for converting DICOM series to NIfTI and NRRD formats, and for adding metadata to NRRD files.

## Scripts

### `dcm2nifti.py`

This script uses the `SimpleITK` library to read a DICOM series and convert it to a NIfTI file. It also adds custom metadata to the NIfTI file in JSON format.

### `dcm2nrrd.py`

This script uses the `SimpleITK` library to read a DICOM series and convert it to a NRRD file. It also adds custom metadata to the NRRD file in JSON format.

## Usage

To use these scripts, you need to have Python and the required libraries installed. You can install the required libraries using pip:

```
pip install SimpleITK==2.3.0
```
```
pip install pynrrd==1.0.0
```
```
pip install nibabel==3.2.2
```

See this notebook for a full example: [runner.ipynb](runner.ipynb)
