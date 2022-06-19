import streamlit as st
import base64
import pickle
from PIL import Image


st.header("Loan Prediction App ")
st.sidebar.markdown("💸 Beta Page")

# Adding Github pages
st.sidebar.markdown("[![Ayobami's Page](image_1.png)](https://github.com/Ayobami6)
st.sidebar.write("Designegycreatives's [Github Page](https://github.com/Designegycreatives)")

# Image For Page
image = Image.open('image.png')
st.image(image, caption='Prediction WebApp')

expander_1 = st.expander("ABOUT WEBAPP")
expander_1.markdown("""<b>This App</b> Can Predict Which Customer Can 
<b>Repay Or Default On Their Loans</b>. """, unsafe_allow_html=True)

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
