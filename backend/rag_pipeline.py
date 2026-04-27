from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_text(file_path="data/college_data.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


import re

def split_text(text, chunk_size=500):
    # Clean text
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces

    # Split into sentences (better than raw chunks)
    sentences = text.split(". ")

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def create_vector_store(chunks):
    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index, embeddings


import numpy as np

def retrieve_context(query, chunks, index, top_k=3):
    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = [chunks[i] for i in indices[0]]

    # Convert distances to similarity
    similarities = 1 / (1 + distances[0])

    # Take average similarity
    confidence = float(np.mean(similarities))

    return results

import requests

def ask_llm(query, context, history):
    history_text = ""
    for msg in history[-4:]:  # last 4 messages only
        role = "User" if msg["type"] == "user" else "Assistant"
        history_text += f"{role}: {msg['text']}\n"

    prompt = f"""


    ======================================================================================================================
You are an assistant for a college website.

STRICT INSTRUCTIONS:
- Answer ONLY using the provided context.
- Keep the answer SHORT (3–5 lines maximum).
- Give ONLY ONE final answer.
- Do NOT repeat or rephrase the answer.
- Use bullet points ONLY when listing multiple items.
- Do NOT add examples, stories, or extra explanations.
- If answer is not found, say "Information not available".
- STOP after giving the answer.
===========================================================================================================================

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


if __name__ == "__main__":
    text = load_text()
    chunks = split_text(text)

    index, embeddings = create_vector_store(chunks)

    print("Chunks created:", len(chunks))

    # TEST QUERY
    query = "What courses are offered?"

    results, confidence = retrieve_context(query, chunks, index)
    context = " ".join(results)

    answer = ask_llm(query, context)

    print("\nFinal Answer:\n")
    print(answer)

