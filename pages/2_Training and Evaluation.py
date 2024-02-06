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
import pickle



# with st.form("my_form"):
#     st.subheader("Model testing part")
#     option = st.selectbox(
#     'Choose a model to train',
#     ('./resources/linear_model.pkl', './resources/poly_model.pkl'), index=None, placeholder="Select a model")

#     st.write('You selected:', option)


#     number = st.number_input('Enter the price',min_value=5,max_value=100,placeholder='Insert a number')
#     st.write('The entered price is ', number)

#     number = st.number_input('Enter the marketing cost',min_value=10,max_value=100000,placeholder='Insert a number')
#     st.write('The entered marketing cost is ', number)

#     number = st.number_input('Enter the day of the week',min_value=1,max_value=7,placeholder='Insert a number')
#     st.write('The entered day is  ', number)

#     number = st.number_input('Enter the month',min_value=1,max_value=12,placeholder='Insert a number')
#     st.write('The entered mounth is  ', number)

#     number = st.number_input('Enter the year',min_value=2015,max_value=2024,placeholder='Insert a number')
#     st.write('The entered year is  ', number)
#     submitted = st.form_submit_button("Train the model")
  
# if submitted:
#     pass




# how to read a model with pickle

# file_path = option
# st.write(file_path)
# with open(file_path, 'rb') as file:
#     model = pickle.load(file)

