document.addEventListener("DOMContentLoaded", function () {

    const input = document.getElementById("userInput");
    const chatBody = document.getElementById("chatBody");
    const languageSelect = document.getElementById("languageSelect");

    // 🚨 IMPORTANT SAFETY CHECK
    if (!input || !chatBody || !languageSelect) {
        console.warn("Chatbot elements not found on this page");
        return;
    }

    input.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            e.preventDefault();

            const text = input.value.trim();
            if (text === "") return;

            addMessage(text, "user");

            const reply = getBotResponse(text);
            setTimeout(() => addMessage(reply, "bot"), 400);

            input.value = "";
        }
    });

    function addMessage(text, sender) {
        const msg = document.createElement("p");
        msg.className = sender === "user" ? "user-msg" : "bot-msg";
        msg.textContent = text;
        chatBody.appendChild(msg);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function getBotResponse(message) {
        message = message.toLowerCase();
        const lang = languageSelect.value;

        if (lang === "en") {
            if (message.includes("disease"))
                return "Cotton AI detects Leaf Curl Virus, Bacterial Blight and more.";
            if (message.includes("accuracy"))
                return "Cotton AI provides up to 95% accuracy.";
            if (message.includes("free"))
                return "Yes, Cotton AI is free for farmers 🌱";
            if (message.includes("treatment"))
                return "We suggest both organic and chemical treatments.";
            return "Ask me about cotton diseases, accuracy, or treatment.";
        }

        if (lang === "hi") {
            return "कपास की बीमारी, इलाज या सटीकता के बारे में पूछें।";
        }

        if (lang === "mr") {
            return "कापूस रोग, उपचार किंवा अचूकतेबद्दल विचारा.";
        }
    }

});
