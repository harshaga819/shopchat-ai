import streamlit as st
from agent import run_agent

st.set_page_config(page_title="E-Commerce AI Agent", page_icon="🛍️")

st.title("E-Commerce AI Assistant")
st.caption("Ask about your orders or products.")

with st.sidebar:
    st.subheader("Try asking")
    st.markdown(
        "- Where is my order ORD-1002?\n"
        "- Tell me about product P101.\n"
        "- Find shoes under ₹5000."
    )
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your shopping question...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = run_agent(question)
            except Exception:
                answer = "Sorry, something went wrong while processing your request."
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})