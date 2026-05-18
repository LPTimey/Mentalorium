"use strict";
import { parseURLParams } from "./src/params.mjs";
import "./src/auto-grow-textarea.mjs"
import { languages } from "./src/i18n.mjs";
import { sendMessage } from "./src/components/user-messsage.mjs";
import { getTranslation } from "./src/i18n.mjs";
import { startProcedure } from "./src/components/ai-message.mjs";

const disclaimerModal = /** @type {HTMLDialogElement} */(document.querySelector("#disclaimer"));
const hiddenModal = /** @type {HTMLDialogElement} */(document.querySelector("#settings"));
const hiddenMenu = /** @type {HTMLDivElement} */(document.querySelector("#hidden-menu"));
const timerLengthSeconds = 3;
/** @type {number | null} */
let timer = null;
let pressed = new Set();

[...hiddenMenu.children].forEach(button => {
    button.addEventListener("click", () => {

        // start timer on first press
        if (timer === null) {
            timer = setTimeout(() => {
                pressed.clear();
                timer = null;
                console.log("Too slow, reset");
            }, timerLengthSeconds * 1000);
        }

        // add current button
        pressed.add(button);

        console.log(`Pressed: ${pressed.size}`);

        // all pressed in time
        if (pressed.size >= 2) {
            clearTimeout(timer);
            timer = null;

            console.log("SUCCESS!");

            // reset if needed
            pressed.clear();

            // callback here
            onAllPressed();
        }
    });
});

function onAllPressed() {
    hiddenModal.showModal()
}

const inputForm = /** @type {HTMLFormElement} */(document.getElementById("inputarea"));
inputForm?.addEventListener("submit", async(event) => { 
    event.preventDefault();
    const {lang, persona} = parseURLParams();
    // @ts-ignore
    const situation = await getTranslation(persona, "situation", lang)
    // @ts-ignore
    const prompt = await getTranslation("index", "prompt", lang)
    sendMessage(prompt, situation, persona || "")
    const sendButton = /** @type {HTMLButtonElement} */(inputForm.querySelector(".send"))
    const textArea = /** @type {HTMLTextAreaElement} */(inputForm.querySelector("textarea"))
    textArea.value = "";
    textArea.dispatchEvent(new Event("change"));
    textArea.dispatchEvent(new Event("input"));
    sendButton.inert = true;
    startProcedure(situation)
})

window.addEventListener("DOMContentLoaded", () => {
    const {
        lang,
        mode
    } = parseURLParams();

    // @ts-ignore
    if (lang && languages[lang]) {
        document.documentElement.lang = lang;

        const languageSelect =
            /** @type {HTMLSelectElement} */ (
                document.querySelector("#language-select")
            );

        languageSelect.value = lang;
    }

    if (mode === "loud") {
        disclaimerModal.showModal()
    }

    import("./src/autotranslate.mjs")
    import("./src/set-prompt.mjs")
});