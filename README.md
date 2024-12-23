# Handwritten Text Recognition using TrOCR

This project leverages the TrOCR model from Hugging Face's Transformers library to perform Optical Character Recognition (OCR) on handwritten text. The application allows users to upload images containing handwritten text and receive predictions of the text in a user-friendly interface built with Streamlit.

## Features
- Upload images in .jpg, .jpeg, or .png formats.
- Get real-time predictions of handwritten text.
- Clean and responsive interface with Streamlit.
- Powered by Microsoft's TrOCR model, fine-tuned for handwritten text recognition.

## Requirements
- Python 3.7+
- Streamlit
- Hugging Face Transformers
- Pillow

## Installation
To install the required dependencies, run the following command:

```bash
pip install streamlit transformers pillow
Usage
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/handwritten-text-recognition.git
cd handwritten-text-recognition
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the web browser and navigate to the provided URL (usually http://localhost:8501).

Upload an image with handwritten text, and the app will display the predicted text.

How It Works
The app uses the TrOCR model (Transformer-based Optical Character Recognition) for recognizing handwritten text. Here's the process:

Image Upload: Users upload an image of handwritten text.
Image Processing: The image is processed into pixel values using the TrOCR processor.
Text Prediction: The TrOCR model generates predicted text from the image.
Text Output: The predicted text is displayed on the app's interface.
Example
Upload an image containing handwritten text like a letter or a note, and the app will predict the text.
