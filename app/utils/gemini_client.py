# app/utils/gemini_client.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Use v1 (not v1beta) and the -latest model
BASE_URL = "https://generativelanguage.googleapis.com/v1/models"
MODEL = "gemini-1.5-flash"


def _call_gemini(prompt: str) -> str:
    """Low-level helper to call Gemini REST API"""
    url = f"{BASE_URL}/{MODEL}:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    resp = requests.post(url, json=payload)

    # For debugging – you can comment this out later
    print("GEMINI STATUS:", resp.status_code)
    if resp.status_code != 200:
        print("GEMINI RAW ERROR:", resp.text)
        return f"Gemini error: {resp.text}"

    data = resp.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("PARSE ERROR:", e, data)
        return "Gemini response could not be parsed."


def ask_gemini(message: str) -> str:
    """Chatbot reply"""
    return _call_gemini(message)


def generate_recommendation(student_data: str) -> str:
    """Role recommendation"""
    prompt = f"""
You are an AI assistant that recommends lab roles.

Student data:
{student_data}

Give 2–3 clear, short recommendations.
"""
    return _call_gemini(prompt)
