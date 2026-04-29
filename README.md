GenAI Chatbot API

A modular chatbot backend built using FastAPI with stateful memory and structured API design.

---

## 🧠 Features

- Chat endpoint with prompt handling
- Stateful conversation memory
- History retrieval
- Reset functionality
- Modular architecture (routes, services, models)

---

## 🛠 Tech Stack

- FastAPI
- Pydantic
- Python

---

## ️ Run Locally

```bash
pip install -r requirements.txt
python3 -m uvicorn main:app --reload --port 8001
