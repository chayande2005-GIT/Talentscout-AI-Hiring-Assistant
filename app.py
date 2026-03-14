import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="TalentScout AI Hiring Assistant", page_icon="🤖")

st.title("TalentScout AI Hiring Assistant")

st.sidebar.title("About")

st.sidebar.info(
"""
TalentScout AI Hiring Assistant

This chatbot performs the initial screening of candidates by collecting
their information and asking technical questions based on their tech stack.
"""
)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Type your message")

if user_input:
    response = chatbot_response(user_input)

    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("bot", response))

for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)