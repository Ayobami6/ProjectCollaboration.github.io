import streamlit as st



st.header("Loan Prediction App ")
st.sidebar.markdown("💳 Home Page")

# Image For Page
file_ = open("image_1.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="dashboard gif">',
    unsafe_allow_html=True)

expander_1 = st.expander("PLEASE READ BEFORE YOU BEGIN")
expander_1.markdown("""<b>This App</b> Can Predict Which Customer Can 
<b>Repay Or Default On Their Loans</b>. """, unsafe_allow_html=True)
