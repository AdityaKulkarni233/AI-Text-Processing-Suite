# AI Text Toolkit  
### FastAPI + Ollama + Mistral 7B

A modern AI-powered web application that provides:

- Text Summarization  
- Grammar Checking & Proofreading  
- Copy to Clipboard  
- Download Output as .txt  
- Runs Fully Locally using Mistral 7B (via Ollama)

---

## Features

- AI Text Summarizer  
- Grammar Correction & Text Improvement  
- Clean Structured UI  
- Copy Button  
- Download Button  
- Proper Error Handling  
- Runs Fully Local (No API Key Required)

---

## Tech Stack

- Backend: FastAPI  
- AI Model: Mistral 7B  
- LLM Runner: Ollama  
- Frontend: HTML, CSS, JavaScript  
- Server: Uvicorn  

---

## How It Works

1. User enters text.
2. FastAPI receives the request.
3. Backend sends prompt to Ollama.
4. Ollama runs Mistral 7B locally.
5. Model generates response.
6. UI displays output with Copy & Download options.

---

## Installation Guide

### Install Ollama

Download from:
https://ollama.com

Verify installation:
```bash
ollama --version
```

---

### Pull Mistral Model

```bash
ollama pull mistral
```

Check installed models:
```bash
ollama list
```

---

### Install Python Dependencies

```bash
pip install fastapi uvicorn requests
```

---

### Run Ollama

Start the model once:
```bash
ollama run mistral
```

Then type:
```
/bye
```

(Ollama will continue running in the background)

---

### Start FastAPI Server

```bash
uvicorn app:app --reload
```

---

### Open in Browser

```
http://127.0.0.1:8000
```

---

## 📂 Project Structure

```
PROJECT AI
├── app.py
└── static
|    ├── index.html   
|    ├── style.css
|    ├── script.js
|    ├── logo.png
|    └── logo1.png
└── README.MD
```


## Test Example

Try this in Grammar Checker:

```
i has went to the market and buyed some apple yesterday.
```

Expected output:

```
I went to the market and bought some apples yesterday.
```

---

## Common Issues & Fixes

### ❌ "No valid response received"
- Ensure Ollama is running
- Ensure model name matches `ollama list`
- Ensure `"stream": false` is set in backend

### ❌ 404 /logo.png
- Make sure file exists inside `/static`
- Check correct file path in HTML

---

## 💡 Future Improvements

- Dark Mode  
- Multiple Model Selection  
- Cloud Deployment  
- Word Counter  
- PDF Export  
- Paraphrasing Tool  
- Tone Detection  

---

## 🎯 Why This Project?

This project demonstrates:

- Backend API Integration  
- LLM Prompt Engineering  
- Local Model Deployment  
- Frontend + Backend Integration  
- Error Handling  
- Real-world AI application development  

Perfect for:
- AI/ML Portfolio  
- Internship Resume  
- GitHub Showcase  

---

## 👨‍💻 Author

Aditya Kulkarni  
Data Science & AI Enthusiast  

---

## ⭐ Support

If you found this useful, consider giving this repository a star on GitHub.

---

## 📜 License

This project is open-source under the MIT License.