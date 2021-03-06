import streamlit as st
import base64
import pickle
from PIL import Image

col1, col2 = st.columns(2)
# Image For Page
image = Image.open('image.png')


col1.header("Loan Prediction App ")
header = '<p style="font-family:sans-serif; color:Grey;">This Web Application can predict if a customer can repay or default on their loans.</p>'
col1.markdown(header, unsafe_allow_html=True)
subheader = '<p style="font-family:sans-serif; color:Grey;">We created this webapp to help reduce the high rate of loan defaults in the financial sector.</p>'
col1.markdown(subheader, unsafe_allow_html=True)
col1.write("[![Ayobami's Page](https://img.icons8.com/material-outlined/24/undefined/github.png)](https://github.com/Ayobami6) Ayobami's Page") 
col1.write("[![Project Page](https://img.icons8.com/material-outlined/24/undefined/github.png)](https://github.com/Ayobami6/ProjectCollaboration.github.io) Project Source Code")
col1.write("[![Designegycreatives's Page](https://img.icons8.com/material-outlined/24/undefined/github.png)](https://github.com/Designegycreatives) Designegy Creatives's Page")
col2.image(image)


st.write("Fill in the following details correctly.")

trained_model = pickle.load(
    open('data/trained_model_Loan_Pred.pkl', 'rb'))

# creating function to make prediction


def generateprediction(data):

    makeprediction = trained_model.predict(data)
    print(makeprediction)

    if (makeprediction[0] == 'Fully Paid'):
        return 'The Customer will not default'
    else:
        return 'The Customer will default'

# Creating a function for main app interface


def main():

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="dashboard gif">',
        unsafe_allow_html=True)

    st.sidebar.image("image.gif", use_column_width=True)


# input data

# forms = st.form("forms", clear_on_submit=True)
try:
    Current_Loan_Amount = st.text_input('Current Loan Amount')
    Credit_score = st.text_input('Credit Score')
    Annual_Income = st.text_input('Annual Income')
    Years_of_Credit_History = st.text_input(
        'Years of credit history')
    Number_of_Credit_Problems = st.text_input('Number Of Credit Problems')
    Monthly_Debt = st.text_input('Monthly Debt')
    Maximum_Open_Credit = st.text_input('Maximum Open Credit')
    Number_of_Open_Accounts = st.text_input('Number Of Open Accounts')
    Current_Credit_Balance = st.text_input('Current Credit Balance')
# submit = forms.form_submit_button('Submit')

    default_check = ""

# prediction code
    if st.button('Predict'):
        default_check = generateprediction([[Current_Loan_Amount, Credit_score, Annual_Income, Monthly_Debt,
                                             Years_of_Credit_History, Number_of_Open_Accounts,
                                             Number_of_Credit_Problems, Current_Credit_Balance,
                                             Maximum_Open_Credit]])

except:
    pass
st.success(default_check)


# if __name__ == '__app__':
#     app()
