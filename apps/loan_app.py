import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import pickle
import datetime
import base64
import time
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def app(): 
       # App Header
       st.markdown('''# **Loan Application Prediction**
       A Machine Learning Prediction Web App.
       ''')
  
       # Upload File
       with st.sidebar:
              df = st.file_uploader("Upload your file: ", type=['pickle'])
         
              if df is None:
                     df = pd.read_pickle(df)
              else:
                     df = pd.read_pickle('pred.sav')
                     
                     output = df['Loan ID']
                     
                     features = df[['Loan Status', 'Current Loan Amount', 'Term', 'Monthly Debt', 'Customer ID', 'Annual Income',
                                    'Years in current job', 'Home Ownership', 'Purpose', 'Number of Open Accounts', 'Tax Liens', 
                                    'Credit Score', 'Years of Credit History', 'Months since last delinquent', 'Number of Credit Problems',
                                    'Current Credit Balance', 'Maximum Open Credit', 'Bankruptcies']]
                     
                     features = pd.get_dummies(features)
                     output = pd.factorize(output)
                     
                     x_train, x_test, y_train, y_test = train_test_split(features, output, test_size = 0.8)
                     
                     logisticregression = LogisticRegression(random_state = 15)
                     
                     logisticregression.fit(x_train, y_train)
                     
                     y_pred = logisticregression.predict(x_test)
                     
                     score = round(accuracy_score(y_pred, y_test), 2)
                     
                     st.write('We trained a Logistic Regression Model on these data,'
                              'It has a score of {}! Use the'
                              'Input below to try out the model.'.format(score))
                     
                     
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
      
