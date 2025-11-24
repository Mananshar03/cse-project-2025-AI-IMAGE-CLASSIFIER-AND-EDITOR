# Ai image classifier project

import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, ImageStat
from collections import Counter
import os

# loading the model
model = MobileNetV2(weights="imagenet")

st.title("AI Image Classifier Project")
st.write("Upload any picture and the program will try to identify what is inside it. You can also edit the image using resize, rotate, flip and compression tools.")

# upload area
uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])


# this function finds which color appears the most
def get_dominant_color(img, resize_val=50):
    small_img = img.resize((resize_val, resize_val))
    pixels = np.array(small_img).reshape(-1, 3)
    common = Counter([tuple(p) for p in pixels]).most_common(1)[0][0]
    return common


# gives a simple name for the color so user understands easily
def simple_color_name(rgb):
    r, g, b = rgb
    if r > 180 and g > 180 and b > 180:
        return "White"
    if r < 60 and g < 60 and b < 60:
        return "Black"
    if r > 150 and g < 80:
        return "Red"
    if g > 150 and r < 80:
        return "Green"
    if b > 150 and r < 80:
        return "Blue"
    if r > 150 and g > 150 and b < 100:
        return "Yellow"
    if r > 180 and g > 100 and b < 80:
        return "Orange"
    return "Unknown"


if uploaded_file is not None:

    # opening the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Picture", use_column_width=True)

    # preparing image for model
    resized_img = img.resize((224, 224))
    arr = image.img_to_array(resized_img)
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)

    # getting prediction
    pred = model.predict(arr)
    labels = decode_predictions(pred, top=3)[0]

    st.subheader("Prediction Results")
    for (_, label, score) in labels:
        st.write(label, " - ", round(score * 100, 2), "%")

    st.subheader("Image Details")

    # dominant color
    main_color = get_dominant_color(img)
    st.write("Dominant Color:", simple_color_name(main_color), "(RGB:", main_color, ")")

    # brightness check
    brightness_val = ImageStat.Stat(img.convert("L")).mean[0]
    if brightness_val > 130:
        light_status = "Bright Image"
    else:
        light_status = "Dark Image"
    st.write("Brightness:", light_status)

    # sharpness check
    sharp_val = np.var(np.array(img.convert("L")))
    if sharp_val > 100:
        sharp_status = "Sharp"
    else:
        sharp_status = "A bit blurry"
    st.write("Sharpness:", sharp_status)

    # contrast
    contrast_val = np.std(np.array(img.convert("L")))
    if contrast_val > 50:
        cont_status = "High Contrast"
    else:
        cont_status = "Low Contrast"
    st.write("Contrast:", cont_status)

    # dimension of original pic
    width, height = img.size
    st.write("Image Size:", width, "x", height)

    # aspect ratio
    aspect = width / height
    if aspect > 1:
        ori = "Landscape"
    elif aspect < 1:
        ori = "Portrait"
    else:
        ori = "Square"
    st.write("Aspect Ratio:", round(aspect, 2), "-", ori)

    # -------------------------------
    # Resize tool
    # -------------------------------
    st.subheader("Resize Picture")

    new_w = st.slider("Width", 50, width, width)
    new_h = st.slider("Height", 50, height, height)

    resized_user_img = img.resize((new_w, new_h))
    st.image(resized_user_img, caption=f"Resized to {new_w} x {new_h}", use_column_width=True)

    # -------------------------------
    # Compression tool
    # -------------------------------
    st.subheader("Compress Picture")

    quality = st.slider("Compression Quality", 1, 100, 80)
    compress_path = "compressed.jpg"
    resized_user_img.save(compress_path, "JPEG", quality=quality)
    size_kb = round(os.path.getsize(compress_path) / 1024, 2)
    st.write("Compressed File Size:", size_kb, "KB")

    # -------------------------------
    # Rotation
    # -------------------------------
    st.subheader("Rotate Picture")

    angle = st.slider("Rotation Angle", 0, 360, 0)
    rotated_img = img.rotate(angle, expand=True)
    st.image(rotated_img, caption=f"Rotated {angle} degrees", use_column_width=True)

    rotated_path = "rotated.jpg"
    rotated_img.save(rotated_path)

    # -------------------------------
    # Flip image
    # -------------------------------
    st.subheader("Flip Picture")

    flip_choice = st.radio("Choose Option", ["None", "Horizontal", "Vertical"])

    if flip_choice == "Horizontal":
        flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_choice == "Vertical":
        flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        flipped = img

    st.image(flipped, caption="Flipped Image", use_column_width=True)

    flipped_path = "flipped.jpg"
    flipped.save(flipped_path)

    # -------------------------------
    # download buttons
    # -------------------------------
    with open(compress_path, "rb") as f:
        st.download_button("Download Compressed Image", data=f, file_name="compressed_image.jpg")

    with open(rotated_path, "rb") as f:
        st.download_button("Download Rotated Image", data=f, file_name="rotated_image.jpg")

    with open(flipped_path, "rb") as f:
        st.download_button("Download Flipped Image", data=f, file_name="flipped_image.jpg")


