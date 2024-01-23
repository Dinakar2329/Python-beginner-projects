import streamlit as st
from rembg import remove
from PIL import Image

def removebg(img):
    input_image = Image.open(img)
    return remove(input_image)

def main():
    st.title("Background Remover App")

    # Create a two-column layout
    uploaded_file = st.file_uploader("Choose an Image....", type=["jpg", "jpeg", "png"])
    col1, col2 = st.columns(2)

    # Upload image in the first column

    if uploaded_file is not None:
        col1.image(uploaded_file, caption="Uploaded image", use_column_width=True)

        # Create a placeholder for the spinner in the second column
        processing_placeholder = col2.empty()

        with st.spinner("Processing..."):
            # Simulate processing delay
            import time
            time.sleep(2)

            # Actual image processing
            result = removebg(uploaded_file)

        # Clear the spinner placeholder
        processing_placeholder.empty()

        # Display the result in the second column
        col2.image(result, caption="Result", use_column_width=True)

if __name__ == '__main__':
    main()
