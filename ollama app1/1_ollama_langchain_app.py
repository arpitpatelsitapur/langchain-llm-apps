from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"    # LangSmith tracking

# prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Act as an helpful assistant."),
        ("user","Question:{question}")
    ]
)


# streamlit User Interface
st.title("Conversational Q&A Chatbot Using Ollama(LLaMA3.1 8B parameter model)")
input_text=st.text_input("Ask whatever you want.")

# using llama 3.1
llm=Ollama(model="llama3.1")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))