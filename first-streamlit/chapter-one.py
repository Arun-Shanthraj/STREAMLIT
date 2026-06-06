import streamlit as st

st.subheader("Brewed with streamlit")
st.text("welcome to your first interactive app")
st.write("choose your favourite variety of chai")

chai = st.selectbox("Your favourite chai:", ['masala chai', 'lemon chai', 'adrak chai', 'kesar chai'])
st.write(f"Your choose {chai}. Excellent choice")
st.success("Your chai has been brewed success")