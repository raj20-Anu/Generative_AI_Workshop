from dotenv import load_dotenv 
from groq import Groq
import os
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(topic, temperature):
    prompt = f"""
You are a deterministic system for downstream software.

ABSOLUTE RULES:
- You MUST use the topic EXACTLY as provided.
- You MUST NOT change, infer, or replace the topic.
- If you violate the format, the response is invalid.

The topic is:
<<<{topic}>>>

Respond ONLY in valid JSON.
No extra text. No explanations.

JSON SCHEMA (STRICT):
{{
  "topic": "{topic}",
  "definition": "one simple sentence definition of {topic}",
  "key_points": [
    "short point 1 about {topic}",
    "short point 2 about {topic}",
    "short point 3 about {topic}"
  ]
}}

"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )

    return response.choices[0].message.content


topic = input("Enter topic: ")
temperature = float(input("Enter temperature (0.0 – 1.0): "))

print("\n--- AI OUTPUT ---\n")
print(generate_response(topic, temperature))