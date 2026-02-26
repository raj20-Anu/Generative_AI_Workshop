# Module 2 – Deterministic & Structured AI Outputs

## 📌 Objective
To demonstrate how AI outputs can be made **predictable, structured, and machine-readable** using temperature control and structured prompting.

---

## 🧠 What This Module Does
- Accepts a topic as user input
- Applies deterministic prompt engineering
- Generates responses in a **fixed, structured format**
- Controls randomness using a **temperature value (0.0 – 1.0)**

The output is designed to be easily parsed by downstream software.

---

## 🛠 Concepts Covered
- Deterministic prompting
- Temperature tuning (0.0 – 1.0)
- Structured response generation
- Output parsing for downstream systems
- Production-style prompt design

---

## 🔑 Temperature Control
This module allows the user to set a **temperature value between 0.0 and 1.0**:

- **0.0 – 0.3** → Highly deterministic, stable, and consistent output  
- **0.4 – 0.7** → Balanced output with slight variation  
- **0.8 – 1.0** → More creative but less predictable responses  

This demonstrates how temperature affects AI behavior in real applications.

---

## ▶ How to Run
```bash
pip install -r requirements.txt
python structured_generator.py
(Make sure to add your API in .env)
