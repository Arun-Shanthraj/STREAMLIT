import streamlit as st

st.title("Chai maker app")

if st.button("Make chai"):
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala has been added your chai")

tea_type = st.radio("Pick your chai base:", ["Milk", "Water", "Sugar", "Honey"])
st.write(f"Selected base {tea_type}")

flavour = st.selectbox("choose flavour:", ["adrak", "kesar", "tulsi"])
st.write(f"Selected flavour: {flavour}")

sugar = st.slider("Sugar level", 0, 5, 4)
st.write(f"selected sugar level: {sugar}")

cups = st.number_input("how many cups", min_value=1, max_value=10, step=1)
st.write(f"selected number of cups: {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome {name} ! your chai is on the way")

dob = st.date_input("select your date of birth")
st.write(f"Your date of birth is {dob} ")
