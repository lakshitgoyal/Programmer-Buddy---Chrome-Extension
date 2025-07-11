console.log("Student Buddy is active on this page!");

// --- 1. Scrape Problem Description ---
// This is a simplified example. You'll need to find the correct selectors for each site.
function getProblemDescription() {
    // Example for LeetCode (selectors might change)
    const title = document.querySelector('.mr-2.text-lg.font-medium.text-label-1.dark\\:text-dark-label-1')?.innerText;
    const description = document.querySelector('.elfjS')?.innerText;

    if (title && description) {
        return `Title: ${title}\n\nDescription: ${description}`;
    }
    // TODO: Add selectors for Codeforces, CodeChef, etc.
    return "Could not automatically detect the problem. Please describe it.";
}

// --- 2. Create the UI ---
function createUI() {
    const container = document.createElement('div');
    container.id = 'buddy-container';
    document.body.appendChild(container);

    container.innerHTML = `
        <div id="buddy-chat-window">
            <div id="buddy-chat-header">Student Buddy</div>
            <div id="buddy-chat-messages"></div>
            <div id="buddy-chat-input-area">
                <input type="text" id="buddy-chat-input" placeholder="Ask for a hint...">
                <button id="buddy-send-button">Send</button>
            </div>
        </div>
        <button id="buddy-toggle-button">🤔</button>
    `;

    // --- 3. Add Event Listeners ---
    const toggleButton = document.getElementById('buddy-toggle-button');
    const chatWindow = document.getElementById('buddy-chat-window');
    const sendButton = document.getElementById('buddy-send-button');
    const inputField = document.getElementById('buddy-chat-input');
    
    toggleButton.addEventListener('click', () => {
        const isHidden = chatWindow.style.display === 'none' || chatWindow.style.display === '';
        chatWindow.style.display = isHidden ? 'flex' : 'none';
        if (isHidden && chatHistory.length === 0) {
            // First time opening, get the initial message
            getHintFromBackend();
        }
    });

    sendButton.addEventListener('click', () => {
        handleUserMessage();
    });

    inputField.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleUserMessage();
        }
    });
}

// --- 4. State and Communication ---
let chatHistory = []; // Stores the conversation {role: 'user'/'assistant', content: '...'}
const problemDescription = getProblemDescription();

function addMessageToChat(text, sender) {
    const messagesContainer = document.getElementById('buddy-chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('buddy-message', `${sender}-message`);
    messageDiv.textContent = text;
    messagesContainer.appendChild(messageDiv);
    // Scroll to the bottom
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

async function getHintFromBackend() {
    addMessageToChat("Thinking...", "ai");

    try {
        const response = await fetch("http://127.0.0.1:8000/get-hint", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                problem_description: problemDescription,
                chat_history: chatHistory
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Remove "Thinking..." message
        const thinkingMessage = document.querySelector('.ai-message:last-child');
        if (thinkingMessage.textContent === "Thinking...") {
            thinkingMessage.remove();
        }
        
        const hint = data.hint || data.error;
        addMessageToChat(hint, "ai");
        chatHistory.push({ role: "assistant", content: hint });

    } catch (error) {
        console.error("Error fetching hint:", error);
        addMessageToChat("Oops! I can't connect to my brain right now. Make sure the backend server is running!", "ai");
    }
}

function handleUserMessage() {
    const inputField = document.getElementById('buddy-chat-input');
    const userMessage = inputField.value.trim();

    if (userMessage) {
        addMessageToChat(userMessage, "user");
        chatHistory.push({ role: "user", content: userMessage });
        inputField.value = '';
        getHintFromBackend(); // Get AI response
    }
}


// --- 5. Initialize ---
createUI();
