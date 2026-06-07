import streamlit as st
from importlib import import_module

model = import_module("src.model")

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="AR GPT",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AR GPT")

# --------------------------------------------------
# Session State
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.header("Settings")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --------------------------------------------------
# Display Chat History
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --------------------------------------------------
# User Input
# --------------------------------------------------
user_input = st.chat_input("Type a message...")

if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_response(
                st.session_state.messages
            )

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )