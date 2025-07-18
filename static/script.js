document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const input = document.querySelector("input[name='message']");
  const chat = document.querySelector("#chat");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    const userMessage = input.value;
    appendMessage("You", userMessage);
    input.value = "";

    try {
      const response = await fetch("/api", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userMessage }),
      });

      const data = await response.json();
      appendMessage("AI", data.reply);
    } catch (error) {
      appendMessage("Error", "Error connecting to server.");
    }
  });

  function appendMessage(sender, message) {
    const messageElement = document.createElement("div");
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chat.appendChild(messageElement);
  }
});
