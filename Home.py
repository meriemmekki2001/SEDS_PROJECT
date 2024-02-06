import requests
import streamlit as st
import datetime
from datetime import time as datetime_time  , datetime as datetime_datetime
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import plotly.express as px
import time
from streamlit_option_menu import option_menu
from transformers import pipeline




st.set_page_config(
    page_title="SEDS Project",
    page_icon=":sparkles:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)



st.title('Food Image Classification :spaghetti: :fries: :pizza: :custard:')
st.header(' Chosen framework: :orange[TensorFlow]')
st.header(' Chosen dataset: :orange[food101] ')
st.subheader('Let\'s explore Computer Vision together :female-technologist:',  divider='rainbow')

st.subheader(' I- Image Classification')
st.subheader(' II- What is Computer Vision ?') 
st.subheader(' III- What is Tensorflow ?')
st.subheader(' IV- What is Deep Learning ?')
st.subheader(' V- What is CNN ?') 
st.subheader(' VI- CNN Architecture')
st.subheader(' VII- How to deal with Overfitting ?') 

text = '''  <h5> Dropout</h5>
    <p>This is the content under subtitle .</p>

    <h5> Data Augmentation</h5>
    <p>This is the content under subtitle .</p>

    <h5> Transfer Learning </h5>
    <p>This is the content under subtitle.</p>
'''
st.markdown(text, unsafe_allow_html=True)
st.subheader(' VIII- food101 dataset')





st.text('This is a text that provides a global overview of the apps purpose and functionality.....')





















# buttons
# courses = [
#     'Machine Learning',
#     'Deep Learning',
#     'Data Science'
# ]

# if st.button("Show", type="primary"):
#     st.write(courses)
# else:
#     pass
    
# if st.button('Say hello'):
#     st.write("Hello !")
# else:
#     pass



