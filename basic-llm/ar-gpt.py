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

    # Show user message immediately
    with st.chat_message("user"):
        st.write(user_input)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Build conversation history
    conversation = ""

    for msg in st.session_state.messages:
        conversation += (
            f"{msg['role']}: {msg['content']}\n"
        )

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_response(conversation)

        st.success(response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )