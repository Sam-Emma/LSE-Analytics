import streamlit as st
from datetime import datetime
from main import get_response
def chat_interface():
    st.title("Trade Bot")
    if "messages" not in st.session_state:
         st.session_state.messages = []
    for message in st.session_state.messages:
      with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
    if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
     st.chat_message("user").markdown(prompt)
    # Add user message to chat history
     st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
     with st.chat_message("assistant"):
        table1, table2, report = get_response(prompt)
        st.write(report)
        st.dataframe(table1)
        st.dataframe(table2)
        st.line_chart(table2, x="Date", y=["Strategy P&L", "Buy and Hold P&L"])
    # Add assistant response to chat history
     st.session_state.messages.append({"role": "assistant", "content": [table1, table2]})
# Run the chat interface
if __name__ == "__main__":
    chat_interface()
