import streamlit as st
import requests

st.title("Live currency converter")
amount = st.number_input("Enter the amount in INR", min_value=1)

target_currency = st.selectbox("Convert to:", ["USD", "AED", "EUR", "JPY", "GBP"])

if st.button("convert"):
    URL = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        converted_amount = rate * amount
        st.success(f"{amount} INR = {converted_amount: .2f} {target_currency}")
    else:
        st.error("failed to fetch conversion rate")