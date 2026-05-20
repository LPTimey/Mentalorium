import { getTranslation } from "../i18n.mjs";
import { parseURLParams } from "../params.mjs";

/**
 * @param {string} situation
 */
export async function startProcedure(situation) {
    const { mode, lang, persona, answerQuality } = parseURLParams();
    const chatArea = document.getElementById("chatarea");
    const fileDiv = /** @type {HTMLDivElement} */(
        document.querySelector('form div:has(>input[type="file"]')
    );
    fileDiv.dataset.attached = "0";

    const key = answerQuality
        ? "response-good"
        : "response-bad";

    // @ts-ignore
    const responsePromise = getTranslation(persona, key, lang);

    // create loading throbber
    const throbber = document.createElement("div");
    throbber.textContent = "...";
    throbber.className = "loading";

    // add loading throbber
    chatArea?.append(throbber);

    // check disclaimer
    if (mode === "loud") {
        // @ts-ignore
        const disclaimer = await getTranslation("index", "disclaimer-description", lang);

        const disclaimerEl = document.createElement("div");
        disclaimerEl.textContent = disclaimer;

        chatArea?.append(disclaimerEl);
    }

    // wait for both:
    // - translation fetch
    // - random delay between 2–3 seconds
    const [response] = await Promise.all([
        responsePromise,
        new Promise(resolve => {
            setTimeout(resolve, 2000 + Math.random() * 1000);
        })
    ]);

    // remove throbber
    throbber.remove();

    // typewriter effect target
    const message = document.createElement("div");
    chatArea?.append(message);

    // simple typewriter effect
    for (let i = 0; i < response.length; i++) {
        message.textContent += response[i];

        await new Promise(resolve => {
            setTimeout(resolve, 2 + Math.random() * 60);
        });
    }
}