import streamlit as st

# Function to get a response from the chatbot
def get_bot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you?": "I'm just a bot, but I'm doing great! How can I help?",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that.")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_input := st.chat_input("Say something"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    bot_response = get_bot_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        st.write(bot_response)