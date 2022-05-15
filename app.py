import streamlit as st
from multiapp import MultiApp
from apps import home, loan_app

app = MultiApp()

# add all applications
app.add_app("Home Page", home.app)
app.add_app("Loan App", loan_app.app)


# The main app
app.run()
