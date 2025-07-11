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
## Deployment:
Backend deployed on Render
Extension published on the Chrome Web Store

## 📜 License
This project is licensed under the MIT License - see the LICENSE.md file for details.
