# Langchain LLM Apps - Learning Journey
![Header Image](img%20header.png)
Welcome to my GitHub repository, where I document my learning journey with the [Langchain framework](https://langchain.com/) and Krish Naik Sir Course. This repo will contain my experiments, projects, and notes as I explore and understand how to build LLM-powered applications using Langchain.

## 🛠️ Project Overview

This repository will include:
- **Learning Resources:** Notes and references I find helpful while learning Langchain.
- **Sample Applications:** Code for various LLM apps built using Langchain.
- **Experimentation:** Different ways to use Langchain for integrating LLMs into various use cases, including chatbots, automation, and more.

## 🔍 What is Langchain?

Langchain is a framework designed to make it easier to build applications powered by large language models (LLMs). It helps in managing the complexities of LLMs, such as chaining calls to language models, managing interactions, and deploying them in various environments. Langchain Framework provides services like-
- `LangSmith` : monitoring of llm apps.
- `LangServe`
- `LangGraph`
- `Agents`
- `Retrival` etc.

## 📁 Repository Structure

- `apps/`: Applications built using Langchain, covering different use cases.

## 🚀 Projects and Applications

### 1. Conversational Q&A Chatbot Using Ollama (LLaMA3.1 8B Parameter Model)
![Ollama Langchain App](ollama%20app1/1_ollama_langchain_app.png)

- Implemented a simple LLaMA3.1 chatbot using the Langchain framework. 
- Learned how to use models from Ollama and monitored it through Langsmith.

- [Project Code](ollama%20app1/1_ollama_langchain_app.py)
- Folder: `ollama app1/`

### 2. Student Support Q&A Chatbot (using context-based approach with LLaMA 3.1)
<div align="center">
  <img src="ollama%20app2/Student%20Support%20Q&A%20Chatbot.png" alt="Ollama Langchain App" width="450"/>
</div>

- Implemented a context-based LLaMA3.1 chatbot using the Langchain framework used context of some information for my university and college.
- Learned to use models by context based approach from Ollama and monitored it through Langsmith.

- [Project Code](ollama%20app1/2_ContextBased_ollama_app.py)
- Folder: `ollama app2/`

### 3. Simple Chatbot Deployed using FastAPI and LangServe
<div align="center">
  <img src="ollama%20app3/ollama%20fastapi.png" alt="Ollama FastAPI Deployment" width="650"/>
</div>

- Implemented the LLaMA3.1 chatbot and deployed it with `FastAPI` in Production-grade Langchain server `LangServe`.
  
- [Project Code](ollama%20app3/)
- [Visit here](ollama%20app3/langserve%20swagger%20ui.md) for more details of this langchain server.

*More projects to come as I progress.*

## 📚 Resources

Here are some resources I find helpful in learning Langchain:
- [Langchain Documentation](https://python.langchain.com/en/latest/)
- [Langchain GitHub Repo](https://github.com/hwchase17/langchain)
- [Langchain Tutorials](https://www.youtube.com/channel/UCd5BZT1dzaM_lpmxP0o3POg)

---

Thanks for visiting! Stay tuned for updates as I dive deeper into Langchain and LLM-powered applications.
