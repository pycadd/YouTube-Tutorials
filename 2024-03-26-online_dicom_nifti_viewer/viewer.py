import streamlit as st
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import tempfile
import os

def load_and_store_dicom_series(directory, session_key):
    if session_key not in st.session_state:
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(directory)
        reader.SetFileNames(dicom_names)
        image_sitk = reader.Execute()
        image_np = sitk.GetArrayFromImage(image_sitk)
        st.session_state[session_key] = image_np
    return st.session_state[session_key]

def plot_slice(slice, size=(4, 4)):
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
    canvas = canvas[::-1, ::-1]
    ax.imshow(canvas, cmap='gray')
    ax.axis('off')
    return fig

def main():
    st.set_page_config(layout="wide")
    st.title("DICOM Series Viewer")

    uploaded_files = st.file_uploader("Choose DICOM Files", accept_multiple_files=True, type=["dcm"], key="dicom_uploader")
    
    if uploaded_files:
        with tempfile.TemporaryDirectory() as temp_dir:
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                file_path = os.path.join(temp_dir, uploaded_file.name)
                with open(file_path, 'wb') as f:
                    f.write(bytes_data)

            # Load DICOM series and store in session state for efficient reloading
            image_np = load_and_store_dicom_series(temp_dir, "dicom_image_data")

        # Adjust the layout to have 2 columns
        col1, col2, col3 = st.columns(3)

        # Axial view
        with col1:
            axial_slice_num = st.slider('Axial Slice', 0, image_np.shape[0] - 1, 0, key="axial_slider")
            fig = plot_slice(image_np[axial_slice_num, :, :], size=(3, 3))
            st.pyplot(fig, clear_figure=True)

        # Coronal view
        with col2:
            coronal_slice_num = st.slider('Coronal Slice', 0, image_np.shape[1] - 1, 0, key="coronal_slider")
            fig = plot_slice(image_np[:, coronal_slice_num, :], size=(3, 3))
            st.pyplot(fig, clear_figure=True)

        # Sagittal view
        with col3:
            sagittal_slice_num = st.slider('Sagittal Slice', 0, image_np.shape[2] - 1, 0, key="sagittal_slider")
            fig = plot_slice(image_np[:, :, sagittal_slice_num], size=(3, 3))
            st.pyplot(fig, clear_figure=True)

if __name__ == "__main__":
    main()
