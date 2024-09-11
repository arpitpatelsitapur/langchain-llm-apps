from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv
load_dotenv()

# fastapi app
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="Simple App for learning purpose."
)

# model
llm=Ollama(model='llama3.1')
# prompt
prompt=ChatPromptTemplate.from_template("Write something about {topic} with 110 words")

# adding Routes
add_routes(
    app,
    prompt|llm,
    path="/ollama_essay"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)






