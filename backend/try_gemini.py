import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

print("--- Starting Gemini Diagnostic Test ---")
print(f"Python Version: {sys.version}")
print(f"google-generativeai version: {genai.__version__}")

# --- Step 1: Load Environment Variables ---
try:
    print("\n[Step 1] Loading .env file...")
    load_dotenv()
    print("dotenv loaded successfully.")
except Exception as e:
    print(f"❌ FAILED to load dotenv. Error: {e}")
    sys.exit() # Stop if this fails

# --- Step 2: Read API Key ---
try:
    print("\n[Step 2] Reading API Key from environment...")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment. Check your .env file.")
    print("API Key found successfully.")
except Exception as e:
    print(f"❌ FAILED to read API key. Error: {e}")
    sys.exit()

# --- Step 3: Configure Gemini ---
try:
    print("\n[Step 3] Configuring Gemini client...")
    genai.configure(api_key=api_key)
    print("Gemini client configured successfully.")
except Exception as e:
    print(f"❌ FAILED to configure Gemini. Error: {e}")
    sys.exit()

# --- Step 4: Call the API ---
try:
    print("\n[Step 4] Calling the Gemini API with 'gemini-pro'...")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Is the Gemini API working? Respond with a single word: Yes.")
    
    print("\n✅ --- SUCCESS! --- ✅")
    print("Gemini's Raw Response:", response)
    print("Gemini's Text:", response.text)

except Exception as e:
    print("\n❌ --- API CALL FAILED --- ❌")
    print(f"An error occurred during the API call.")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Details: {e}")
    print("\n--- Common Causes for this Error ---")
    print("1. API Key is invalid or has been disabled.")
    print("2. The 'Vertex AI API' is not enabled in your Google Cloud project.")
    print("3. Your Google Cloud project is not linked to a billing account.")
    print("4. Network issue (firewall, proxy) blocking connection to Google's servers.")