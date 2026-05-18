
/**
 * 
 * @param {string} message 
 * @param {string} situationText
 * @param {string} situation
 */
export function sendMessage(message, situationText, situation) {
    const chatarea = document.getElementById("chatarea");
    const userMessage = document.createElement("div");
    const userFile = document.createElement("div");
    // userMessage.innerText = situationText;
    // userMessage.innerText += "\n\n";
    userMessage.innerText += message;
    userFile.innerHTML = `
    <img src="./assets/file.svg" width="70" height="70">
    <div>
    ${situation}.txt<br>
    TXT
    </div>
    `
    userMessage.classList.add("message", "human");
    userFile.classList.add("message", "human", "file");
    chatarea?.appendChild(userFile);
    chatarea?.appendChild(userMessage);
}