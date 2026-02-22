<div align="center">

# 📄 DocuTalk

**AI-Powered Conversational PDF Intelligence System**

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![LLM Provider: Groq](https://img.shields.io/badge/LLM-Groq-f56a25.svg)](https://groq.com/)
[![VectorDB: Chroma](https://img.shields.io/badge/VectorDB-ChromaDB-1e90ff.svg)](https://www.trychroma.com/)
[![Frontend: Chainlit](https://img.shields.io/badge/Frontend-Chainlit-ff69b4.svg)](https://github.com/Chainlit/chainlit)
[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-46E3B7.svg)](https://render.com/)

> *"Documents were never meant to be static. DocuTalk turns them into interactive knowledge systems."*

[**🚀 Live Demo**](https://docutalk-f5yz.onrender.com) | [**Report Bug**](https://github.com/MohnishVik/DocuTalk/issues) | [**Request Feature**](https://github.com/MohnishVik/DocuTalk/issues)

<br>

<img src="./DocuTalk%20UI%20screenshot.jpg" alt="DocuTalk UI Screenshot" width="900" style="border-radius: 8px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);"/>

</div>

---

## 📖 Project Overview

**DocuTalk** is a Retrieval-Augmented Generation (RAG) based document intelligence system that transforms static PDF documents into interactive conversational systems.

Instead of manually scanning long documents, DocuTalk allows users to upload one or more PDFs and ask context-aware questions in real time. The system extracts, processes, embeds, and retrieves relevant content before generating grounded responses using a Large Language Model (LLM). 

**The goal is simple: Make documents talk back.**

---

## ✨ Key Features

* **📚 Multi-PDF Upload Support:** Upload multiple documents within a single session seamlessly.
* **🎯 Context-Aware Responses:** Answers are strictly generated using retrieved document chunks—no hallucinated guesses.
* **🔍 Vector Similarity Search:** Lightning-fast semantic retrieval powered by dense embeddings.
* **🧠 Conversational Memory:** Maintains chat history for rich, multi-turn conversational context.
* **🔗 Source Document References:** Transparency is key; retrieved chunks are attached to the answers.
* **☁️ Cloud Deployment:** Fully deployed and publicly accessible 24/7 via Render.

---

## ⚙️ System Architecture

DocuTalk follows a robust, structured RAG pipeline to ensure high accuracy and speed:

1.  **PDF Ingestion:** Text extraction using `PyPDF2` (Supports multiple uploaded files).
2.  **Text Chunking:** Utilizes `RecursiveCharacterTextSplitter` with an overlapping chunk strategy to maintain semantic continuity.
3.  **Embedding Generation:** Converts text into dense vector representations using Sentence Transformers (`all-MiniLM-L6-v2`).
4.  **Vector Storage:** Embeddings are indexed in `ChromaDB` for high-speed similarity search.
5.  **Retriever + LLM:** Leverages the **Groq API** (`llama-3.1-8b-instant` model) to generate fast, grounded, and contextual responses.
6.  **Conversation Memory:** Session-based buffer memory maintains multi-turn coherence.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Chainlit |
| **Backend** | Python 3.10 |
| **Embeddings** | Sentence Transformers |
| **Vector Database** | ChromaDB |
| **LLM Provider** | Groq |
| **Deployment** | Render |

---

## 🚀 How to Run Locally

Follow these steps to get DocuTalk running on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/MohnishVik/DocuTalk.git
cd DocuTalk
```

### 2. Set up a virtual environment
```bash
python -m venv venv
```

**Activate the environment:**

* **Windows:**
  ```bash
  venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_api_key_here
```

### 5. Start the Application
```bash
chainlit run app.py
```
*The app will automatically open in your default browser at `http://localhost:8000`.*

---

## 🌍 Deployment

DocuTalk is live and fully deployed on **Render**. The production environment features:

* Explicit Python version control (`3.10.11`)
* Secure, environment-based secret management
* Production-ready dependency resolution

🔗 **Public URL:** [https://docutalk-f5yz.onrender.com](https://docutalk-f5yz.onrender.com)

---

## 🗺️ Future Improvements

We are constantly looking to improve DocuTalk. Here is what is on the roadmap:

- [ ] Persistent vector database storage
- [ ] Streaming token responses for faster UI feedback
- [ ] Multi-user authentication system
- [ ] Document session history (save and load past chats)
- [ ] Advanced UI enhancements and usage analytics

---

## 👨‍💻 Author

**MOHNISH S** *AI Systems | Deployment Engineering | Applied Intelligence*

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)]([https://github.com/MohnishVik](https://github.com/MohnishVik)) 

---
<div align="center">
  <i>If you found this project helpful, please consider giving it a ⭐️ on GitHub!</i>
</div>
