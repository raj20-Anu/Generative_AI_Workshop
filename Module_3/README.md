# Module 3 – Modular LLM Pipeline (Production Architecture)

## 📌 Objective
To design a **scalable, maintainable, and production-style AI system** using modular architecture and separation of concerns.

---

## 🧠 What This Module Does
- Accepts user input through a simple UI
- Builds structured prompts using a dedicated prompt layer
- Sends requests to an LLM via an abstraction layer
- Applies post-processing to clean and format responses
- Displays the final output in a user-friendly interface

This module demonstrates how real-world GenAI systems are built beyond single scripts.

---

## 🏗 Architecture Overview

User Input  
→ Prompt Layer  
→ LLM Layer  
→ Post-Processing  
→ Output

---

## 📂 Project Structure
- `input_layer.py` – Handles user input
- `prompt_layer.py` – Builds structured prompts
- `llm_layer.py` – Communicates with Groq via LiteLLM
- `post_processing.py` – Cleans and formats responses
- `pipeline.py` – Orchestrates the entire workflow
- `app.py` – Streamlit-based user interface
- `assets/` – UI assets and visuals

---

## 🛠 Concepts Covered
- Modular AI system design
- Separation of concerns
- Prompt abstraction layer
- Model invocation layer
- Post-processing pipelines
- UI integration using Streamlit
- Production-style GenAI architecture

---

## ▶ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
(Make sure to add your API in .env)
