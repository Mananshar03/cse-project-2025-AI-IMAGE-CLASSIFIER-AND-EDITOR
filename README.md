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
- **Easy Image Upload** – Quickly add JPG, JPEG, or PNG files.  
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

1. **Install Libraries**  
   ```bash
   pip install streamlit tensorflow pillow numpy

