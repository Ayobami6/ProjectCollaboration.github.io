import streamlit as st
import pandas as pd
import base64
import datetime
import time


def app():
  # App Header
  st.markdown('''# **Loan Application Prediction**
  A Machine Learning Prediction Web App.
  ''')
  
  # Side Note 1
  expander_1 = st.sidebar.expander("PLEASE READ BEFORE YOU BEGIN")
  expander_1.markdown("""<b>This App</b> has been designed out of passion to 
  make <b>business intelligence</b> simple, easy, and efficient for business owners
  with <b>no business analysis experience</b>. """, unsafe_allow_html=True)

