async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `<div class="user-msg">${userInput}</div>`;
    document.getElementById("userInput").value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userInput })
    });

    const data = await response.json();

    chatBox.innerHTML += `<div class="bot-msg">${data.answer}</div>`;
}
