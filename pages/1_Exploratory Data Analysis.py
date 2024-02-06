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


# load sales dataset

st.subheader('Here is the dataset of our study case')
sales_df = pd.read_csv('./resources/products_sales.csv')
st.dataframe(sales_df) 
 

st.subheader('Dataset description')

# charts

st.line_chart(data=sales_df,y=[  'Day_of_Week', 'Month', 'Year'],width=0,height=0,use_container_width=True)

st.bar_chart(data=sales_df,y=[  'Day_of_Week', 'Month', 'Year'],width=0,height=0,use_container_width=True)



st.subheader('Scatter chart')
st.scatter_chart(sales_df, y=['Marketing_Cost','Sales'])



st.subheader("Scatter plot")
df = px.data.iris()
fig = px.scatter(
    sales_df,
    x="Marketing_Cost",
    y="Sales",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
