import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import datetime
import base64
import time
import pickle

st.markdown("Loan Prediction App ")
st.sidebar.markdown(("💳 Loan Prediction Page")


trained_model = pickle.load(open(
    'C:/Users/Ayo/Downloads/trained_model_Loan_Pred.pkl', 'rb'))


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
    st.markdown('''# **Loan Prediction Application**
       A Machine Learning Prediction Web App.
       ''')

    # Side Note 1
    expander_1 = st.expander("PLEASE READ BEFORE YOU BEGIN")
    expander_1.markdown(
        """<b>This App is built to predict Loan Approval Of Customers and To Predict Customeer  </b>. """, unsafe_allow_html=True)

    # Upload File
    with st.sidebar:
        df = st.file_uploader("Upload your file: ", type=['pickle'])

    try:
        df = pd.read_pickle(df)
        st.markdown("Your Data Record: ")
        AgGrid(df, editable=True)
    except:
        pass

    def Makeprediction(data):
        prediction = trained_model.predict(data)
        print(prediction)

        if (prediction[0] == 'Fully Paid'):
            return 'The Customer will not default'
        else:
            return 'The Customer will default'

    forms = st.form("forms", clear_on_submit=True)
    Current_Loan_Amount = forms.text_input('Current Loan Amount')
    Credit_score = forms.text_input('Credit Score')
    Annual_Income = forms.text_input('Annual Income')
    Years_of_Credit_History = forms.text_input(
        'Years of credit history')
    Number_of_Credit_Problems = forms.text_input('Number Of Credi Problems')
    Monthly_Debt = forms.text_input('Monthly Debt')
    Maximum_Open_Credit = forms.text_input('Maximum Open Credit')
    Number_of_Open_Accounts = forms.text_input('Number Of Open Accounts')
    Current_Credit_Balance = forms.text_input('Current Credit Balance')
    submit = forms.form_submit_button('Submit')

    # features = [Current_Loan_Amount, Credit_Score, Annual_Income, Monthly_Debt,
    #             Years_of_Credit_History, Number_of_Open_Accounts,
    #             Number_of_Credit_Problems, Current_Credit_Balance,
    #             Maximum_Open_Credit]

    defaultcheck = ''

    if submit:
        # makeprediction = trained_model.predict([[Current_Loan_Amount, Credit_score, Annual_Income, Monthly_Debt,
        #                                          Years_of_Credit_History, Number_of_Open_Accounts,
        #                                          Number_of_Credit_Problems, Current_Credit_Balance,
        #                                          Maximum_Open_Credit]])
        # if (makeprediction[0] == 'Fully Paid'):
        #     return 'The Customer will not default'
        # else:
        #     return 'The Customer will default'

        defaultcheck = Makeprediction([[Current_Loan_Amount, Credit_score, Annual_Income, Monthly_Debt,
                                      Years_of_Credit_History, Number_of_Open_Accounts,
                                      Number_of_Credit_Problems, Current_Credit_Balance,
                                      Maximum_Open_Credit]])

    st.success(defaultcheck)
