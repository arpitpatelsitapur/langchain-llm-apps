import requests
import streamlit as st

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/ollama_essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write something on")

if input_text:
    st.write(get_ollama_response(input_text))


