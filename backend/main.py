from fastapi import FastAPI
from rag_pipeline import load_text, split_text, create_vector_store, retrieve_context, ask_llm
from fastapi import Query
import json
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once at startup
text = load_text()
chunks = split_text(text)
index, embeddings = create_vector_store(chunks)


@app.get("/")
def home():
    return {"message": "AI College Chatbot is running"}


@app.get("/ask")
def ask(query: str, history: str = Query(default="[]")):
    history_list = json.loads(history)

    results = retrieve_context(query, chunks, index)
    context = " ".join(results)

    answer = ask_llm(query, context, history_list)

    return {
        "answer": answer
        
    }