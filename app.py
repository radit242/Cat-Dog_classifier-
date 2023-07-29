import tensorflow as tf
from tensorflow import keras
from keras import Sequential
import matplotlib.pyplot as plt
import cv2
import streamlit as st
from io import BytesIO
import numpy as np

# Load the model
model = tf.keras.models.load_model('final_model.h5')

st.subheader("DOG VS CAT CLASSIFIER")
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

if file is None:
    st.text("Please upload an image file")
else:
    # Read the image from the file object
    image_bytes = file.read()
    np_arr = np.frombuffer(image_bytes, np.uint8)
    test_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Now you have the image in the 'test_image' variable, and you can use it as needed
    # For example, convert BGR to RGB and display using Streamlit
    if test_image is None:
        st.text("Error: Image not loaded properly.")
    
    else:
        rgb_img = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
        st.image(rgb_img, caption='Uploaded Image', use_column_width=True)

        test_img = cv2.resize(test_image,(256,256))
        test_input = test_img.reshape((1,256,256,3))
        test_input = test_input/255.0

        #predict the class
        def pred(prediction):
            if prediction > 0.5:
                st.subheader("It is a DOG")
            else:
                st.subheader("It is a Cat")
        
        prediction = model.predict(test_input)
        pred(prediction)