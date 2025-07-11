import os
import requests
import json
from dotenv import load_dotenv

print("--- Starting FINAL RAW REST API Diagnostic Test ---")
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key not found!")

# Use the v1beta endpoint with the new 1.5 model name
# This is the current correct combination for the latest models
model_name = "gemini-1.5-flash-latest"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"

payload = {
    "contents": [{"parts": [{"text": "Is this final API call working? Say yes."}]}]
}
headers = {'Content-Type': 'application/json'}

print(f"\nAttempting to call URL: {url}\n")
try:
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=15)
    response.raise_for_status()
    print("\n✅ --- SUCCESS! IT WORKED! --- ✅")
    print(response.json())
except Exception as e:
    print("\n❌ --- RAW API CALL FAILED --- ❌")
    if 'response' in locals():
      print("Status Code:", response.status_code)
      print("Response Body:", response.text)
    else:
      print("Error:", e)