import langchain_file as lch
import streamlit as st

st.title("Interactive LLM Response Generator")

if "responses" not in st.session_state:
  st.session_state.responses = []

prompt_text = st.sidebar.text_input("Enter your prompt:", key="unique_prompt_input")

if st.sidebar.button("Submit Prompt"):
  response = lch.generate_output(prompt_text)
  st.session_state.responses.append(response)
  
  for i in st.session_state.responses:
    st.markdown(i['prompt'])
    st.markdown(i['response'])
    st.markdown('---')