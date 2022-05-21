import streamlit as st
from multiapp import MultiApp
from apps import home, loan_app, loan_profile

app = MultiApp()

# add all applications
app.add_app("Home Page", home.app)
app.add_app("Loan App", loan_app.app)
app.add_app("Customer Loan Profile", loan_profile.app)


# The main app
app.run()
