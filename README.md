# Advanced AI Image Classifier & Editor

A great little app built with **Streamlit** that lets you upload an image to get quick AI predictions and gives you simple tools to edit and optimize your pictures.

---

## Project Overview
This project is designed to make both **image classification** and **basic photo editing** super easy for everyone.  
Just upload any picture, and the app instantly tells you what it likely contains using a fast and efficient deep learning model.  

- Shows the **top three predictions** with confidence scores.  
- Provides **useful insights** like dominant color, brightness, sharpness, and dimensions.  
- Includes a **new editing section** where you can resize, compress, rotate, or flip images.  
- All processed images can be **downloaded instantly and free of cost**.  

It is built to be simple, fast, and practical for testing, learning, or quickly optimizing your photos.

---

## Features
- Easy Image Upload – Quickly add JPG, JPEG, or PNG files.  
- **Fast AI Predictions** – Get instant classified results with clear confidence levels.  
- **Detailed Image Insights** – Analyze dominant color, brightness, contrast, and sharpness.  
- **Image Resizer** – Resize images using simple sliders.  
- **Compression Tool** – Reduce file size by adjusting JPEG quality.  
- **Rotation and Flip** – Spin images (0–360°) or flip horizontally/vertically.  
- **Download Everything** – Save all processed and optimized images with one click.  

---

## Technologies / Tools Used
- **Python** – Core programming language.  
- **Streamlit** – Interactive web app framework.  
- **TensorFlow / Keras (MobileNetV2)** – Deep learning model for image classification.  
- **Pillow (PIL)** – Image processing (resize, compress, rotate, etc.).  
- **NumPy** – Numerical operations and image data handling.  
- **ImageStat** – Brightness and contrast analysis.  
- **Collections (Counter)** – Finds the most common color in image data.  

---

## Steps to Install & Run
Setting up and running this app is straightforward. Use your **Terminal (Mac/Linux)** or **Command Prompt/PowerShell (Windows)**:

# AI Image Classifier

This project is a simple AI-powered image classifier built with **Streamlit** and **TensorFlow**. Setting up and running the app is straightforward — just follow the steps below.

---

## 🚀 Setup & Usage

Open your **Terminal (Mac/Linux)** or **Command Prompt/PowerShell (Windows)** and run the following commands:

```bash
# 1. Install required libraries
pip install streamlit tensorflow pillow numpy

# 2. Run the application
to run the app you have to -streamlit run app.py- to the terminal.
# Instructions for Testing

Follow these steps to test the AI Image Classifier and Editor:

1. Open the App  
   Launch the application in your web browser.

2. Upload an Image  
   Add any image file (JPG, JPEG, or PNG) to the app.

3. View Predictions & Insights  
   Check the AI-generated predictions along with initial image insights such as dominant color, brightness, contrast, and sharpness.

4. Try Editing Tools
   Experiment with the built-in tools:  
   - Resizer – adjust image dimensions  
   - Compression – reduce file size  
   - Rotator – spin the image to correct orientation  
   - Flipper – flip horizontally or vertically  

5. Download Processed File 
   Once satisfied with the changes, use the Download buttons to save your optimized image.

