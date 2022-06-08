import streamlit as st
import pickle

trained_model = pickle.load(open(
    'C:/Users/Ayo/Desktop/Collaboration/ProjectCollaboration.github.io/trained_model_Loan_Pred.sav', 'rb'))


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
    st.title('Loan Defualters Prediction')
    st.subheader('This is the beta version')

    # input data

    Current_Loan_Amount = st.text_input('Loan_amount')
    Credit_Score = st.text_input('Credit_score')
    Annual_Income = st.text_input('Annual_income')
    Monthly_Debt = st.text_input('Monthly_debt')
    Years_of_Credit_History = st.text_input('Years of credit')
    Number_of_Open_Accounts = st.text_input('Open Accounts')
    Number_of_Credit_Problems = st.text_input('Credit Problems')
    Current_Credit_Balance = st.text_input('Credit Balance')
    Maximum_Open_Credit = st.text_input('Open credit')
    Term_Long_Term = st.text_input('Long Term')
    Term_Short_Term = st.text_input('Short Term')
    Years_in_current_job_1_year = st.text_input('1 year')
    Years_in_current_job_10_years = st.text_input('10 years')
    Years_in_current_job_2_years = st.text_input('2 years')
    Years_in_current_job_3_years = st.text_input('3 years')
    Years_in_current_job_4_years = st.text_input('4 years')
    Years_in_current_job_5_years = st.text_input('5 years')
    Years_in_current_job_6_years = st.text_input('6 years')
    Years_in_current_job_7_years = st.text_input('7 years')
    Years_in_current_job_8_years = st.text_input(' 8 years on the job')
    Years_in_current_job_9_years = st.text_input('9 years on the job')
    Years_in_current_job_more_1_year = st.text_input('less than 1 year on job')
    Home_Ownership_HaveMortgage = st.text_input('Have Mortgage')
    Home_Ownership_Home_mortgage = st.text_input('Mortgae')
    Home_Ownership_Own_Home = st.text_input('House Owner')
    Home_Ownership_Rent = st.text_input('Rent')
    Purpose_Business_Loan = st.text_input('Busines Loan')
    Purpose_Buy_House = st.text_input('Buy House')

    Purpose_Buy_a_Car = st.text_input('Buy a Car')
    Purpose_Debt_Consolidation = st.text_input('Debt Consolidation')

    Purpose_Educational_Expenses = st.text_input('Educational Expenses')
    Purpose_Home_Improvements = st.text_input('Home Improvements')

    Purpose_Medical_Bills = st.text_input('Medical Bills')

    Purpose_Take_a_Trip = st.text_input('Trip')

    Purpose_major_purchase = st.text_input('Major Purchase')
    Purpose_moving = st.text_input('Moving')
    Purpose_Other = st.text_input('Other')

    Purpose_renewable_energy = st.text_input('Energy Renewable')
    Purpose_small_business = st.text_input('Small business')

    Purpose_vacation = st.text_input('Vacation Purpose')
    Purpose_wedding = st.text_input('Wedding_purpose')
    Purpose_other = st.text_input('other purpose')

    features = [Current_Loan_Amount, Credit_Score, Annual_Income, Monthly_Debt,
                Years_of_Credit_History, Number_of_Open_Accounts,
                Number_of_Credit_Problems, Current_Credit_Balance,
                Maximum_Open_Credit, Term_Long_Term, Term_Short_Term,
                Years_in_current_job_1_year, Years_in_current_job_10_years,
                Years_in_current_job_2_years, Years_in_current_job_3_years,
                Years_in_current_job_4_years, Years_in_current_job_5_years,
                Years_in_current_job_6_years, Years_in_current_job_7_years,
                Years_in_current_job_8_years, Years_in_current_job_9_years,
                Years_in_current_job_more_1_year, Home_Ownership_HaveMortgage,
                Home_Ownership_Home_mortgage, Home_Ownership_Own_Home,
                Home_Ownership_Rent, Purpose_Business_Loan, Purpose_Buy_House,
                Purpose_Buy_a_Car, Purpose_Debt_Consolidation,
                Purpose_Educational_Expenses, Purpose_Home_Improvements,
                Purpose_Medical_Bills, Purpose_Other, Purpose_Take_a_Trip,
                Purpose_major_purchase, Purpose_moving,
                Purpose_renewable_energy, Purpose_small_business,
                Purpose_vacation, Purpose_wedding, Purpose_other]

    default_check = ""

    # prediction code
    if st.button('Predict'):
        default_check = generateprediction([[Current_Loan_Amount, Credit_Score, Annual_Income, Monthly_Debt,
                                            Years_of_Credit_History, Number_of_Open_Accounts,
                                            Number_of_Credit_Problems, Current_Credit_Balance,
                                            Maximum_Open_Credit, Term_Long_Term, Term_Short_Term,
                                            Years_in_current_job_1_year, Years_in_current_job_10_years,
                                            Years_in_current_job_2_years, Years_in_current_job_3_years,
                                            Years_in_current_job_4_years, Years_in_current_job_5_years,
                                            Years_in_current_job_6_years, Years_in_current_job_7_years,
                                            Years_in_current_job_8_years, Years_in_current_job_9_years,
                                            Years_in_current_job_more_1_year, Home_Ownership_HaveMortgage,
                                            Home_Ownership_Home_mortgage, Home_Ownership_Own_Home,
                                            Home_Ownership_Rent, Purpose_Business_Loan, Purpose_Buy_House,
                                            Purpose_Buy_a_Car, Purpose_Debt_Consolidation,
                                            Purpose_Educational_Expenses, Purpose_Home_Improvements,
                                            Purpose_Medical_Bills, Purpose_Other, Purpose_Take_a_Trip,
                                            Purpose_major_purchase, Purpose_moving,
                                            Purpose_renewable_energy, Purpose_small_business,
                                            Purpose_vacation, Purpose_wedding, Purpose_other]])
    st.success(default_check)


if __name__ == '__main__':
    main()
