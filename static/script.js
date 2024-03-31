document.addEventListener('DOMContentLoaded', function() {
    const chatHistory = document.querySelector('.chat-history');
    const promptForm = document.getElementById('prompt-form');

    promptForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const promptInput = document.getElementById('prompt');
        const userPrompt = promptInput.value.trim();

        if (userPrompt) {
            const userMessage = createMessageElement(userPrompt, 'user-message');
            promptInput.value = '';
            sendPromptToServer(userPrompt)
                .then(modelResponse => {
                    const modelMessage = createMessageElement(modelResponse, 'model-message');
                })
                .catch(error => {
                    const errorMessage = createMessageElement(error, 'error-message');
                    console.error('Error:', error);
                });
        }
    });

    function createMessageElement(text, className) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', className);
        messageElement.textContent = text;
        const chatHistoryContainer = document.querySelector('.chat-history-container');
        const chatHistory = chatHistoryContainer.querySelector('.chat-history');
        chatHistory.appendChild(messageElement);
        chatHistoryContainer.scrollTop = chatHistoryContainer.scrollHeight;
        return messageElement;
    }

    function sendPromptToServer(prompt) {
        return new Promise((resolve, reject) => {
            fetch('/process_prompt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: prompt })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    reject(data.error);
                } else {
                    resolve(data.response);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                reject(error);
            });
        });
    }
});