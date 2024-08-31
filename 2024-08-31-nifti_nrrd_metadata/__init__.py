from .dcm2nifti import SimpleDicomToNiftiConverter as sdnifti
from .dcm2nrrd import SimpleDicomToNrrdConverter as sdnrrd

__all__ = ['sdnifti', 'sdnrrd']