# AI College Chatbot (RAG-Based Knowledge Assistant)

An AI-powered chatbot that answers queries about college information using Retrieval-Augmented Generation (RAG) and a locally hosted LLM.

---

## Overview

This project is a full-stack AI application that allows users to ask questions about a college (MMCOE) and receive accurate, context-based answers.

It uses:
- Semantic search to retrieve relevant information
- A local LLM to generate responses
- Prompt engineering to ensure controlled and reliable outputs

---

## How It Works

1. College data is processed and split into chunks  
2. Chunks are converted into embeddings using Sentence Transformers  
3. FAISS is used to store and retrieve relevant chunks  
4. User query is matched with relevant context  
5. Ollama (phi model) generates a final answer using the retrieved context  

---

## Architecture
User Query
↓
Frontend (React)
↓
FastAPI Backend
↓
FAISS (Semantic Search)
↓
Relevant Context
↓
Ollama (LLM - phi)
↓
Final Answer


---

## Tech Stack

### Backend
- FastAPI
- FAISS
- Sentence-Transformers
- Ollama (phi model)

### Frontend
- React (Vite)
- Axios

---

## Features

- Semantic search using embeddings  
- AI-generated answers using local LLM  
- Context-aware responses using a RAG pipeline  
- Controlled outputs using prompt engineering  
- Chat-style user interface  

---

## Project Structure
ai-college-chatbot/
│
├── backend/
│ ├── main.py
│ ├── rag_pipeline.py
│ ├── scraper.py
│ ├── data/
│ └── requirements.txt
│
├── frontend/
│ └── React App
│
└── README.md


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/samyak-waikar/ai-college-chatbot.git
cd ai-college-chatbot
```
### 2. Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt


Run Ollama (LLM)
Install Ollama from: https://ollama.com
ollama run phi


Start Backend
uvicorn main:app --reload
```
### 3. Frontend Setup
```bash
cd ../frontend
npm install
npm run dev
```

### Example Queries
```bash
What courses are offered?
What is the admission process?
What facilities are available?
Does the college provide placement support?
```

### Limitations
```bash
Uses a lightweight local model (phi), so responses may be simpler
Works only with provided context (no external knowledge)
Requires manual data preparation
```

### Key Learnings
```bash
Implemented a full RAG pipeline
Applied prompt engineering to control LLM output
Built an end-to-end AI system with frontend and backend integration
Handled noisy data and improved retrieval quality
```
### Future Improvements
```bash
Add source citations for answers
Improve UI/UX
Use more advanced LLMs
Deploy the application
```

Author
Samyak Waikar

License
This project is for educational purposes.
