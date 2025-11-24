#Ai image classifier project
import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, ImageStat
from collections import Counter
import os

model = MobileNetV2(weights="imagenet")

st.title("📸 Advanced AI Image Classifier")
st.write("Upload an image and get detailed AI predictions")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

def get_dominant_color(img, resize_val=50):
    img = img.resize((resize_val, resize_val))
    pixels = np.array(img).reshape(-1, 3)
    most_common = Counter([tuple(p) for p in pixels]).most_common(1)[0][0]
    return most_common

def simple_color_name(rgb):
    r, g, b = rgb
    if r > 180 and g > 180 and b > 180: return "White"
    if r < 60 and g < 60 and b < 60: return "Black"
    if r > 150 and g < 80: return "Red"
    if g > 150 and r < 80: return "Green"
    if b > 150 and r < 80: return "Blue"
    if r > 150 and g > 150 and b < 100: return "Yellow"
    if r > 180 and g > 100 and b < 80: return "Orange"
    return "Mixed/Unknown"
if uploaded_file is not None:
    # Display original image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    resized = img.resize((224, 224))
    img_array = image.img_to_array(resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    predictions = model.predict(img_array)
    results = decode_predictions(predictions, top=3)[0]
    st.subheader("AI Classification Results:")
    for (_, label, score) in results:
        st.write(f"**{label}** — {round(score * 100, 2)}% confidence")
    st.subheader("Additional Image Insights")
    dom_rgb = get_dominant_color(img)
    st.write(f"**Dominant Color:** {simple_color_name(dom_rgb)} (RGB: {dom_rgb})")
    brightness = ImageStat.Stat(img.convert("L")).mean[0]
    st.write(f"**Brightness Level:** {'Bright' if brightness > 130 else 'Dark'}")
    laplacian_var = np.var(np.array(img.convert("L")))
    sharpness = "Sharp Image" if laplacian_var > 100 else "Slightly Blurry"
    st.write(f"**Sharpness:** {sharpness}")
    contrast = np.std(np.array(img.convert("L")))
    st.write(f"**Contrast Level:** {'High Contrast' if contrast > 50 else 'Low Contrast'}")
    width, height = img.size
    st.write(f"**Image Dimensions:** {width} x {height} pixels")
    aspect_ratio = width / height
    if aspect_ratio > 1:
        orientation = "Landscape"
    elif aspect_ratio < 1:
        orientation = "Portrait"
    else:
        orientation = "Square"
    st.write(f"**Aspect Ratio:** {round(aspect_ratio, 2)} ({orientation})")
    st.subheader("Image Resize Tool")
    new_width = st.slider("Select Width", 50, width, width)
    new_height = st.slider("Select Height", 50, height, height)
    resized_user_image = img.resize((new_width, new_height))
    st.image(resized_user_image, caption=f"Resized Image ({new_width}x{new_height})", use_column_width=True)
    st.subheader("Image Compression Tool")
    compression_quality = st.slider("Compression Quality (Higher = Better Quality)", 1, 100, 80)
    compressed_path = "compressed_image.jpg"
    resized_user_image.save(compressed_path, "JPEG", quality=compression_quality)
    compressed_size_kb = round(os.path.getsize(compressed_path) / 1024, 2)
    st.write(f"Compressed File Size: {compressed_size_kb} KB")
    st.subheader("Rotate Image")
    rotation_angle = st.slider("Select Rotation Angle", 0, 360, 0)
    rotated_image = img.rotate(rotation_angle, expand=True)
    st.image(rotated_image, caption=f"Rotated Image ({rotation_angle}°)", use_column_width=True)
    rotated_path = "rotated_image.jpg"
    rotated_image.save(rotated_path)
    st.subheader("Flip Image")
    flip_option = st.radio("Choose Flip Type", ["None", "Flip Horizontally", "Flip Vertically"])
    if flip_option == "Flip Horizontally":
        flipped_image = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_option == "Flip Vertically":
        flipped_image = img.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        flipped_image = img
    st.image(flipped_image, caption=flip_option, use_column_width=True)
    flipped_path = "flipped_image.jpg"
    flipped_image.save(flipped_path)
    with open(compressed_path, "rb") as file:
        st.download_button(
            label="Download Resized & Compressed Image",
            data=file,
            file_name="processed_image.jpg",
            mime="image/jpeg"
        )
    with open(rotated_path, "rb") as file:
        st.download_button(
            label="Download Rotated Image",
            data=file,
            file_name="rotated_image.jpg",
            mime="image/jpeg"
        )
    with open(flipped_path, "rb") as file:
        st.download_button(
            label="Download Flipped Image",
            data=file,
            file_name="flipped_image.jpg",
            mime="image/jpeg"
        )
