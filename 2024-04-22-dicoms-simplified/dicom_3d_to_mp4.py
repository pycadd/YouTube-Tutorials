import pydicom
from PIL import Image
from glob import glob
import cv2
import os

def create_video_from_images():
    png_files = glob('data/dicom_3d_images/*.png')
    height, width, _ = cv2.imread(png_files[0]).shape
    size = (width,height)

    out = cv2.VideoWriter('data/dicom_3d.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for filename in png_files:
        img = cv2.imread(filename)
        out.write(img)
    out.release()

def convert_3d_dicom_to_png_rgb(path_dicom):
    os.makedirs('data/dicom_3d_images', exist_ok=True)

    dicom_file = pydicom.dcmread(path_dicom)
    dicom_array = dicom_file.pixel_array

    for i in range(dicom_array.shape[0]):
        dicom_slice = dicom_array[i,:,:,:]
        dicom_slice_image = Image.fromarray(dicom_slice)
        dicom_slice_image.save(f'data/dicom_3d_images/image{i}.png')

def convert_3d_dicom_to_png_grayscale(path_dicom):
    os.makedirs('data/dicom_3d_images', exist_ok=True)

    dicom_file = pydicom.dcmread(path_dicom)
    dicom_array = dicom_file.pixel_array

    for i in range(dicom_array.shape[0]):
        dicom_slice = dicom_array[i,:,:,:]
        dicom_slice_image = Image.fromarray(dicom_slice).convert('L')
        dicom_slice_image.save(f'data/dicom_3d_images/image{i}.png')


def main(path_dicom):
    print('[INFO]: Converting dicom to png')
    convert_3d_dicom_to_png_grayscale(path_dicom)

    print('[INFO]: Converting png to avi')
    create_video_from_images()


if __name__ == '__main__':
    main('data/dicom_3d.dcm')
