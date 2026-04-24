import streamlit as st
from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"

# Initialize OpenAI client
client = OpenAI()

# Page config
st.set_page_config(page_title="Election Assistant", page_icon="🗳️")

# Title
st.title("🗳️ Election Assistant (Gujarati AI)")

# Sidebar
st.sidebar.title("About")
st.sidebar.write("This AI assistant helps you understand election process in simple Gujarati.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Quick buttons
st.write("### Quick Options 👇")
col1, col2, col3 = st.columns(3)

if col1.button("🪜 Process"):
    user_input = "Explain election process step by step in Gujarati"

elif col2.button("📅 Timeline"):
    user_input = "Explain election timeline in Gujarati"

elif col3.button("🗳️ Voting"):
    user_input = "How to vote in election in Gujarati"

else:
    user_input = st.chat_input("ચૂંટણી વિશે પૂછો...")

# When user sends input
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-5.3",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an election assistant. Always reply in very simple Gujarati with steps and examples."
                    },
                    *st.session_state.messages
                ]
            )

            reply = response.choices[0].message.content
            st.markdown(reply)

    # Save bot reply
    st.session_state.messages.append({"role": "assistant", "content": reply})   
