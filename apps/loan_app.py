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
       st.markdown('''# **Loan Application Prediction**
       A Machine Learning Prediction Web App.
       ''')
  
       
       # Upload File
       with st.sidebar:
              df = st.file_uploader("Upload your file: ", type=['pickle'])
         
       try:
        df = pd.read_pickle(df)
        st.markdown("Your Data Record: ")
        AgGrid(df, editable=True)
       except:
         pass  
      
       forms = st.form("forms", clear_on_submit=True)
       loan_type = forms.radio('Loan Term', ['Short Term Loan', 'Long Term Loan'])
       credit_score = forms.text_input('Credit Score')
       income = forms.text_input('Annual Income')
       years = forms.text_input('Number Of Years In Current Job')
       home = forms.radio('Home Ownership', ['Owned', 'Rented Apartment'])
       debt = forms.text_input('Monthly Debt')
       credit = forms.text_input('Maximum Open Credit')
       accounts = forms.text_input('Number Of Open Accounts')
       submit = forms.form_submit_button('Predict Loan Output')
        
       if submit:
            st.success("Prediction in process....")
      
