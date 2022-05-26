import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import datetime
import base64
import time
import plotly.express as px
import numpy as np
from apps import loan_app



def app():
  
        # Upload File
       with st.sidebar:
              df = st.file_uploader("Upload your file: ", type=['pickle'])
  
     
       try:
        st.text_input("Enter Customer's ID")
       except:
         pass
      
       options = st.selectbox('Explore Customer Loan Records:',
                              ('Choose','Customer Details', 'Loan Details', 'Credit Score Details'))
      
