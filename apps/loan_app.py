import streamlit as st
import pandas as pd
import datetime
import time


def app():
  # App Header
  st.markdown('''# **Loan Application Prediction**
  A Machine Learning Prediction Web App.
  ''')
  
  # Side Note 1
  expander_1 = st.expander("PLEASE READ BEFORE YOU BEGIN")
  expander_1.markdown("""<b>This App is built to predict Loan Approval Of Customers and To Predict Customeer  </b>. """, unsafe_allow_html=True)

