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
  
       # Side Note 1
       expander_1 = st.expander("PLEASE READ BEFORE YOU BEGIN")
       expander_1.markdown("""<b>This App is built to predict Loan Approval Of Customers and To Predict Customeer  </b>. """, unsafe_allow_html=True)
       
      # Upload File
       with st.sidebar:
              df = st.file_uploader("Upload your file: ", type=['pickle'])
               
       try:
        cols = st.selectbox('SELECT VALUE:',
                            options=df.groupby(['Loan ID', 'Customer ID'])
        cols2 = st.multiselect('SELECT LABEL:',
                             df.groupby(['Annual Income', 'Years in current job', 'Home Ownership', 'Purpose', 'Number of Open Accounts',
                                                'Tax_Liens', 'Credit Score', 'Years of Credit History', 'Months since last delinquent',
                                                'Number of Credit Problems', 'Current Credit Balance', 'Maximum Open Credit',
                                                'Bankruptcies', 'Loan Status', 'Current Loan Amount', 'Term', 'Monthly_Debt'])
        df = df.groupby(df[cols2])[cols].sum().reset_index()
       except:
         pass
         
       try:
        df = pd.read_pickle(df)
        st.markdown("Your Data Record: ")
        AgGrid(df, editable=True)
       except:
         pass
     # Setting Checkbox Menu
       type = st.sidebar.radio("Pick one", ['Color', 'No Color'])
       if type == 'Color':
           plotType_color = st.sidebar.selectbox("Plot Type:", ['Choose', 'Line', 'Bar', 'Pie'])
           if plotType_color == 'Line':
             fig = px.line(df, x=df[cols2], y=df[cols])
             st.plotly_chart(fig, use_container_width=True)
           if plotType_color == 'Pie':
             fig = px.pie(names=df[cols2], values=df[cols])
             st.plotly_chart(fig, use_container_width=True)
           if plotType_color == 'Bar':
             fig = px.bar(df, x=df[cols2], y=df[cols], color=df[cols2])
             st.plotly_chart(fig, use_container_width=True)
            
       if type == 'No Color':
           plotType_nocolor = st.sidebar.selectbox("Plot Type:", ['Choose', 'Line', 'Bar', 'Pie'])
           if plotType_nocolor == 'Line':
             fig = px.line(df, x=df[cols2], y=df[cols])
             st.plotly_chart(fig, use_container_width=True)
           if plotType_nocolor == 'Pie':
             fig = px.pie(names=df[cols2], values=df[cols])
             st.plotly_chart(fig, use_container_width=True)
           if plotType_nocolor == 'Bar':
             fig = px.bar(df, x=df[cols2], y=df[cols])
             st.plotly_chart(fig, use_container_width=True)
