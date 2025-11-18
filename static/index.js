// async function sendMessage() {
//     const userInput = document.getElementById("userInput").value;
//     const chatBox = document.getElementById("chatBox");

//     chatBox.innerHTML += `<div class="user-msg">${userInput}</div>`;
//     document.getElementById("userInput").value = "";

//     const response = await fetch("/chat", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ query: userInput })
//     });

//     const data = await response.json();

//     chatBox.innerHTML += `<div class="bot-msg">${data.answer}</div>`;
// }


const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const typingBubble = document.getElementById("typing");

function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    addMessage(text, "user");
    userInput.value = "";

    typingBubble.classList.remove("hidden");  // show typing animation

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: text }),
        });

        const data = await response.json();

        setTimeout(() => {
            typingBubble.classList.add("hidden");  // hide typing animation
            addMessage(data.answer, "bot");
        }, 800); // small delay for natural feel

    } catch (error) {
        typingBubble.classList.add("hidden");
        addMessage("⚠️ Error connecting to server.", "bot");
    }
}

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});






