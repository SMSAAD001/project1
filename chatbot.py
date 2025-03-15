import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Hugging Face API endpoint and key
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
HF_API_KEY = os.getenv("HF_API_KEY")  # Load API key from .env

headers = {"Authorization": f"Bearer {HF_API_KEY}"} if HF_API_KEY else {}

def chat_with_ai(user_input):
    if not HF_API_KEY:
        return "⚠ AI service unavailable. Missing API key."

    try:
        response = requests.post(HF_API_URL, headers=headers, json={"inputs": user_input})
        response_data = response.json()

        # Handle list response
        if isinstance(response_data, list) and len(response_data) > 0:
            return response_data[0].get("generated_text", "🤖 AI didn't understand.")
        
        # Handle dictionary response
        elif isinstance(response_data, dict) and "generated_text" in response_data:
            return response_data["generated_text"]
        
        return "🤖 AI response not recognized."

    except Exception as e:
        return f"⚠ Error: {str(e)}"
