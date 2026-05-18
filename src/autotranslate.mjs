"use strict";

import { getTranslation } from "./i18n.mjs";

const toBeTranslated =()=> /** @type {HTMLElement[]} */([
    ...document.querySelectorAll("[data-translation]")
]);

/**
 * Übersetzt Elemente mit data-translation="collection;key"
 *
 * @param {HTMLElement[]} elements
 */
async function translate(elements) {
    const pageLanguage =
        document.documentElement.lang || "en";

    for (const el of elements) {
        const attr = el.dataset.translation;

        if (!attr) {
            continue;
        }

        const [collection, key] = attr.split(":");

        if (!collection || !key) {
            console.warn(
                `Invalid translation attribute: "${attr}"`
            );
            continue;
        }

        try {
            const translated = await getTranslation(
                collection,
                key,
                // @ts-ignore
                pageLanguage
            );
            if (el instanceof HTMLInputElement || el instanceof HTMLTextAreaElement) {
                el.placeholder = translated;
            } else {
                el.innerText = translated;
            }
        } catch (err) {
            console.error(
                `Translation failed for "${attr}"`,
                err
            );
        }
    }
}

translate(toBeTranslated());

/**
 * Beobachtet Änderungen an lang-Attributen
 */
const observer = new MutationObserver(mutations => {
    const shouldRetranslate = mutations.some(
        mutation =>
            mutation.type === "attributes" &&
            mutation.attributeName === "lang"
    );

    if (shouldRetranslate) {
        translate(toBeTranslated());
    }
});

observer.observe(document.documentElement, {
    attributes: true,
    subtree: true,
    attributeFilter: ["lang"]
});