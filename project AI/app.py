from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
import os
import json

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral" # Using Mistral 7B for summarization

# ===============================
# PAGE ROUTE (Single HTML)
# ===============================
@app.get("/")
def serve_summarizer():
    return FileResponse(os.path.join("static", "index.html"))
# ===============================
# SUMMARIZER API
# ===============================

@app.post("/summarize")
def summarize_text(text: str = Form(...)):
    headers = {"Content-Type": "application/json"}

    prompt = f"Summarize the following text clearly and concisely:\n{text}"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            headers=headers
        )

        json_response = response.json()
        summary = json_response.get("response", "No valid response received.")

        return {"summary": summary}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


# ===============================
# GRAMMAR CHECKER API
# ===============================

@app.post("/proofread")
def proofread_text(text: str = Form(...)):
    headers = {"Content-Type": "application/json"}

    prompt = f"Correct the grammar, spelling, and sentence structure of the following text:\n{text}"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            headers=headers
        )

        json_response = response.json()
        corrected_text = json_response.get("response", "No valid response received.")

        return {"corrected_text": corrected_text}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


# ===============================
# RUN SERVER
# ===============================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)