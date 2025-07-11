# Programmer Buddy - Chrome Extension
<sub>A smart Socratic tutor to help you think, not just code.</sub>

Programmer Buddy is a Chrome extension designed for students and self-learners tackling programming problems on platforms like LeetCode, Codeforces, and CodeChef. Instead of giving you the answer, Buddy acts as a Socratic guide, asking leading questions and providing step-by-step hints to help you arrive at the solution on your own.
It's the perfect companion to build problem-solving skills, overcome mental blocks, and foster a deeper understanding of algorithms and data structures.
Install on Chrome Web Store <!-- TODO: Add link when published -->
## ✨ Features
### Socratic Learning:
  Get guiding questions and conceptual hints, never the direct solution.
### Seamless Integration: 
  Automatically appears on popular coding problem websites.
### Interactive Chat: 
Have a real-time conversation with your AI-powered buddy.
### Context-Aware: 
Buddy reads the problem description to provide relevant, high-quality guidance.
### Lightweight & Minimalist: 
A clean, unobtrusive UI that doesn't get in your way.
## 🚀 How It Works
Programmer Buddy is a powerful combination of a browser extension frontend and an AI-powered backend.
#### Content Script (extension/):
  When you navigate to a supported problem page, a JavaScript content script activates. It carefully scrapes the problem description from the page and injects the "Buddy" chat interface into the DOM.
#### API Request: 
  Your interactions in the chat window, along with the problem context, are sent to a dedicated backend API.
#### FastAPI Backend (backend/): 
  A lightweight Python backend built with FastAPI receives the request.
#### The AI Brain (Google Gemini): 
  The backend uses a meticulously crafted system prompt to instruct Google's Gemini Pro model. This prompt commands the AI to act as a Socratic tutor, forbidding it from ever revealing the final answer.
### Helpful Hint: 
  The AI-generated hint is sent back to the browser and displayed in the chat window, continuing the learning conversation.
<!-- Optional: Create a simple diagram -->
## 🛠️ Tech Stack
### Frontend: 
  HTML, CSS, JavaScript (no frameworks)
### Backend: 
  Python, FastAPI
### AI: Google Gemini API


# 🔧 Local Development & Testing

Want to run the project locally to test, contribute, or see how it works under the hood? You'll need to run both the backend server and the frontend extension.

## Prerequisites

Python 3.11+

Google Chrome

A Google Gemini API Key (you can get a free one from Google AI Studio)

## Part 1: Backend Setup (The AI Brain)

First, let's get the local server running.

### Clone the Repository
    git clone https://github.com/your-username/programmer-buddy.git
    cd programmer-buddy/backend


Create and Activate a Virtual Environment
This keeps the project's dependencies isolated.

# Create the environment
    python -m venv venv

### Activate it
#### On Windows:
    .\venv\Scripts\activate
#### On macOS/Linux:
    source venv/bin/activate

#### Install Dependencies
With the virtual environment active, run:
    pip install -r requirements.txt

### Set Up Your API Key

Create a new file in the backend directory named .env.

Open this .env file and add your Google Gemini API key like so:

GEMINI_API_KEY="AIzaSy...YourSecretKeyHere..."

Run the Server!
Now, start the FastAPI server:

uvicorn main:app --reload

The backend is now live at http://127.0.0.1:8000. Leave this terminal window running.

## Part 2: Frontend Setup (The Chrome Extension)

Now, let's connect the Chrome extension to your local server.

Configure the Endpoint

In a code editor, open the file extension/content.js.

Find the fetch call inside the getHintFromBackend function and ensure the URL points to your local server.

// extension/content.js

const response = await fetch("http://127.0.0.1:8000/get-hint", {
    // ...
});

Load the Extension in Chrome

Open Google Chrome and navigate to chrome://extensions.

Enable "Developer mode" using the toggle in the top-right corner.

Click the "Load unpacked" button.

In the file browser that appears, select the extension folder from this project.

✅ All Done! The "Programmer Buddy" extension is now installed and connected to your local backend. Navigate to a supported website like LeetCode to see it in action

## 📜 License
This project is licensed under the MIT License - see the LICENSE.md file for details.
