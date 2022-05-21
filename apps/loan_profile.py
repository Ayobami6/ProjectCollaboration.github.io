import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import datetime
import base64
import time


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
  
       # Side Note 1
       expander_1 = st.expander("PLEASE READ BEFORE YOU BEGIN")
       expander_1.markdown("""<b>This App is built to predict Loan Approval Of Customers and To Predict Customeer  </b>. """, unsafe_allow_html=True)
