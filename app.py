# pyrefly: ignore [missing-import]
import asyncio
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# pyrefly: ignore [missing-import]
import streamlit as st

from rag.rag_chain import ask_question

st.set_page_config(
    page_title="DStarix Internship Guide Chatbot",
    page_icon="📘",
    layout="wide"
)

# ---------------- Session ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("📘 Internship Guide")

    st.markdown("---")

    st.markdown("""
### About

This chatbot answers questions based on the **DStarix Internship Rule Book** using **Retrieval-Augmented Generation (RAG)**.

""")




    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- Main ---------------- #

st.title("🤖 DStarix Internship Guide Chatbot")

st.write(
    "Ask any question related to the Internship Rule Book."
)

# Display chat history

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# Chat input

user_question = st.chat_input(
    "Ask your question..."
)

if user_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):

        st.markdown(user_question)

    with st.chat_message("assistant"):

        with st.spinner("Searching Internship Guide..."):

            try:

                response = ask_question(user_question)

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                st.error(str(e))