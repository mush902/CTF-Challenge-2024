document.addEventListener('DOMContentLoaded', function() {
    const chatHistory = document.querySelector('.chat-history');
    const promptForm = document.getElementById('prompt-form');
    const sendButton = document.getElementById('send-button');
    const acceptButton = document.getElementById('accept-button');
    const rejectButton = document.getElementById('reject-button');
    const initialResponseDisplay = document.querySelector('.chat-history');
    const processedResponseDisplay = document.querySelector('.processed-response');
  
    sendButton.addEventListener('click', function(event) {
      event.preventDefault();
      const promptInput = document.getElementById('prompt');
      const userPrompt = promptInput.value.trim();
      if (userPrompt) {
        sendButton.disabled = true;
        acceptButton.disabled = false;
        rejectButton.disabled = false;
        const userMessage = createMessageElement(userPrompt, 'user-message');
        promptInput.value = ''; // Clear the input field
        sendPromptToServer(userPrompt)
          .then(initialResponse => {
            const modelMessage = createMessageElement(initialResponse, 'model-message');
          })
          .catch(error => {
            const errorMessage = createMessageElement(error, 'error-message');
            console.error('Error:', error);
          });
      }
    });
  
    acceptButton.addEventListener('click', () => {
      const acceptedResponse = initialResponseDisplay.textContent;
      processAcceptedResponse(acceptedResponse)
        .then(newResponse => {
          processedResponseDisplay.textContent = newResponse;
        })
        .catch(error => {
          const errorMessage = createMessageElement(error, 'error-message');
          console.error('Error:', error);
        });
    });
  
    rejectButton.addEventListener('click', () => {
      window.location.reload();
    });
  
    
    function createMessageElement(htmlContent, className) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', className);
        // Set inner HTML instead of text content to render HTML
        messageElement.innerHTML = htmlContent;
        
        const chatHistoryContainer = document.querySelector('.chat-history-container');
        const chatHistory = chatHistoryContainer.querySelector('.chat-history');
        chatHistory.appendChild(messageElement);
        chatHistoryContainer.scrollTop = chatHistoryContainer.scrollHeight;
        return messageElement;
      }

    function sendPromptToServer(prompt) {
      return new Promise((resolve, reject) => {
        fetch('/interact', {
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
            const initialResponse = data.response;
            resolve(initialResponse);
          }
        })
        .catch(error => {
          console.error('Error:', error);
          reject(error);
        });
      });
    }
  
    function processAcceptedResponse(acceptedResponse) {
      return new Promise((resolve, reject) => {
        fetch('/process-response', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ response: acceptedResponse })
        })
        .then(response => response.json())
        .then(data => {
          if (data.error) {
            reject(data.error);
          } else {
            resolve(data.newResponse);
          }
        })
        .catch(error => {
          console.error('Error:', error);
          reject(error);
        });
      });
    }
  });

