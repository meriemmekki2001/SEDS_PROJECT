import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
from PIL import Image
import pathlib
from tensorflow import keras
from tensorflow.keras import layers
from transformers import pipeline
from tensorflow.keras.models import Sequential





class_names = ['french_fries', 'pizza', 'spaghetti_carbonara', 'waffles']


st.subheader('Since the Training process takes a long time we\'ll only provide the prediction part here, you can check more about the training part in the notebook',  divider='rainbow')

# load the image
uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False, type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.image(uploaded_file)

model = None



# Load the model
if st.button('Click to Load the model and predict the class of the image you loaded'):
    with st.spinner('The model is being loaded, please wait'):


        # add the path to the checkpoints of the trained model here to use it for prediction ..
        model = tf.keras.models.load_model('')
    st.success('The model is successfully loaded')
    img = tf.keras.utils.load_img(uploaded_file, target_size=(512, 512))
    img = tf.expand_dims(img, 0) 
    predictions = model.predict(img)
    score = tf.nn.softmax(predictions[0])

    st.write("The image you loaded is more likely to be:", class_names[np.argmax(score)])
    st.write("Confidence:", 100 * np.max(score))


