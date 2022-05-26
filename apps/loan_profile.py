import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import datetime
import base64
import time
import plotly.express as px
import numpy as np



def app():
   # Image For Page
       file_ = open("image1.jpg", "rb")
       contents = file_.read()
       data_url = base64.b64encode(contents).decode("utf-8")
       file_.close()

       st.markdown(
       f'<img src="data:image/gif;base64,{data_url}" alt="dashboard gif">',
       unsafe_allow_html=True
       )
       
       # App Header
       st.markdown('''# **Customer Loan Profile**
       A Machine Learning Prediction Web App.
       ''')
  
     
       try:
        st.text_input("Enter Customer's ID")
       except:
         pass
      
       options = st.selectbox('Explore Customer Loan Records:',
                              ('Choose','Customer Details', 'Loan Details', 'Credit Score Details'))
      
