import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image


# Load processor and model for TrOCR (OCR model for handwritten text)
@st.cache_resource
def load_model():
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

    return processor, model

# Define a prediction function
def predict_text(image, processor, model):
    # Prepare pixel values
    pixel_values = processor(image, return_tensors="pt").pixel_values

    # Generate text predictions
    predict_ids = model.generate(pixel_values)

    # Decode the predicted text
    predicted_text = processor.batch_decode(predict_ids, skip_special_tokens=True)[0]
    return predicted_text

# Streamlit app
st.title("Handwritten Text Recognition using TrOCR")
st.write("Upload an image of handwritten text to get the predicted text.")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Load the model and processor
    processor, model = load_model()

    # Predict text
    st.write("Processing the image...")
    predicted_text = predict_text(image, processor, model)

    # Display the predicted text
    st.subheader("Predicted Text")
    st.write(predicted_text)