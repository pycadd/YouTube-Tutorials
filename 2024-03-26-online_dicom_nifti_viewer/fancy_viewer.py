import streamlit as st
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import tempfile
import os
import nibabel as nib

def load_and_store_dicom_series(directory, session_key):
    if session_key not in st.session_state:
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(directory)
        reader.SetFileNames(dicom_names)
        image_sitk = reader.Execute()
        image_np = sitk.GetArrayFromImage(image_sitk)
        st.session_state[session_key] = image_np
    return st.session_state[session_key]

def plot_slice(slice, size=(4, 4), is_nifti=False):
    # Adjust the figure size for consistent viewer sizes
    fig, ax = plt.subplots(figsize=size)
    # Calculate the square canvas size
    canvas_size = max(slice.shape)
    canvas = np.full((canvas_size, canvas_size), fill_value=slice.min(), dtype=slice.dtype)
    # Center the image within the canvas
    x_offset = (canvas_size - slice.shape[0]) // 2
    y_offset = (canvas_size - slice.shape[1]) // 2
    canvas[x_offset:x_offset+slice.shape[0], y_offset:y_offset+slice.shape[1]] = slice
    fig.patch.set_facecolor('black')  # Set the figure background to black
    ax.set_facecolor('black')
    if is_nifti:
        canvas = np.rot90(canvas)
    else:
        canvas = canvas[::-1, ::-1]

    ax.imshow(canvas, cmap='gray')
    ax.axis('off')
    return fig

def load_nifti_file(filepath, session_key):
    if session_key not in st.session_state:
        nifti_img = nib.load(filepath)
        image_np = np.asanyarray(nifti_img.dataobj)
        st.session_state[session_key] = image_np
    return st.session_state[session_key]


def main():
    st.set_page_config(page_title='DICOM Viewer', layout="wide", page_icon="assets/logo.ico")

    st.image('assets/pycad.png', width=350)
    st.title("DICOM Series Viewer")

    # Custom CSS to style the "cards" with unique colors for each view
    st.markdown("""
    <style>
    .view-label-axial {
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        background-color: #007BFF; /* Blue */
        border-radius: 10px;
        text-align: center;
        margin: 10px 0px;
        padding: 5px;
    }
    .view-label-coronal {
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        background-color: #28A745; /* Green */
        border-radius: 10px;
        text-align: center;
        margin: 10px 0px;
        padding: 5px;
    }
    .view-label-sagittal {
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ffc800; /* Yellow */
        border-radius: 10px;
        text-align: center;
        margin: 10px 0px;
        padding: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    uploaded_files = st.file_uploader("Choose DICOM or NIfTI Files", accept_multiple_files=True, type=["dcm", "nii", "nii.gz"], key="file_uploader")
    
    if uploaded_files:
        with tempfile.TemporaryDirectory() as temp_dir:
            is_nifti = False
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                file_path = os.path.join(temp_dir, uploaded_file.name)
                with open(file_path, 'wb') as f:
                    f.write(bytes_data)
                if uploaded_file.name.endswith(('.nii', '.nii.gz')):
                    is_nifti = True
            
            if is_nifti:
                image_np = load_nifti_file(file_path, "nifti_image_data")
            else:
                image_np = load_and_store_dicom_series(temp_dir, "dicom_image_data")


        col1, col2, col3 = st.columns(3)

        # Display labels for each view with unique colors
        col1.markdown("<div class='view-label-axial'>Axial View</div>", unsafe_allow_html=True)
        col2.markdown("<div class='view-label-coronal'>Coronal View</div>", unsafe_allow_html=True)
        col3.markdown("<div class='view-label-sagittal'>Sagittal View</div>", unsafe_allow_html=True)
        if is_nifti:
            with col1:
                axial_slice_num = st.slider(' ', 0, image_np.shape[2] - 1, 0, key="axial_slider")
                fig = plot_slice(image_np[:, :, axial_slice_num], size=(3, 3), is_nifti=is_nifti)
                st.pyplot(fig, clear_figure=True)

            with col2:
                coronal_slice_num = st.slider('  ', 0, image_np.shape[1] - 1, 0, key="coronal_slider")
                fig = plot_slice(image_np[:, coronal_slice_num, :], size=(3, 3), is_nifti=is_nifti)
                st.pyplot(fig, clear_figure=True)

            with col3:
                sagittal_slice_num = st.slider('   ', 0, image_np.shape[0] - 1, 0, key="sagittal_slider")
                fig = plot_slice(image_np[sagittal_slice_num, :, :], size=(3, 3), is_nifti=is_nifti)
                st.pyplot(fig, clear_figure=True)

        else:
            with col1:
                axial_slice_num = st.slider(' ', 0, image_np.shape[0] - 1, 0, key="axial_slider")
                fig = plot_slice(image_np[axial_slice_num, :, :], size=(3, 3), is_nifti=is_nifti)
                st.pyplot(fig, clear_figure=True)

            with col2:
                coronal_slice_num = st.slider('  ', 0, image_np.shape[1] - 1, 0, key="coronal_slider")
                fig = plot_slice(image_np[:, coronal_slice_num, :], size=(3, 3), is_nifti=is_nifti)
                st.pyplot(fig, clear_figure=True)

            with col3:
                sagittal_slice_num = st.slider('   ', 0, image_np.shape[2] - 1, 0, key="sagittal_slider")
                fig = plot_slice(image_np[:, :, sagittal_slice_num], size=(3, 3), is_nifti=is_nifti)
                st.pyplot(fig, clear_figure=True)

if __name__ == "__main__":
    main()

