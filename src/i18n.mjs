"use strict";

/** @type {keyof typeof languages} */
export let fallbackLanguage = "en";

export const languages = Object.freeze({
    de: "de-DE",
    en: "en-GB",
    es: "es-HN",
});

class KeyNotFoundError extends Error {
    /**
     * 
     * @param {string} collection 
     * @param {string} key 
     * @param {string} language 
     */
    constructor(collection, key, language) {
        super(`Key "${key}" not found in "${collection}" (${language})`);
    }
}

class CollectionNotFoundError extends Error {
    /**
     * 
     * @param {string} collection 
     * @param {string} language 
     */
    constructor(collection, language) {
        super(`Collection "${collection}" not found for language "${language}"`);
    }
}

/**
 * Lädt eine Translation-Collection
 * 
 * @param {string} collection
 * @param {keyof typeof languages} language
 * @returns {Promise<Record<string, string>>}
 */
async function loadCollection(collection, language) {
    const locale = languages[language];

    try {
        const response = await fetch(`./i18n/${locale}/${collection}.json`);

        if (!response.ok) {
            throw new Error();
        }

        return await response.json();
    } catch {
        throw new CollectionNotFoundError(collection, language);
    }
}

/**
 * 
 * @param {string} collection
 * @param {string} key
 * @param {keyof typeof languages} language
 * @param {boolean} [useFallback=true]
 * @param {keyof typeof languages} [customFallbackLanguage=fallbackLanguage]
 * @returns {Promise<string>}
 * 
 * @throws {CollectionNotFoundError}
 * @throws {KeyNotFoundError}
 */
export async function getTranslation(
    collection,
    key,
    language,
    useFallback = true,
    customFallbackLanguage = fallbackLanguage
) {
    try {
        const json = await loadCollection(collection, language);

        if (key in json && json[key]) {
            return json[key].replaceAll("\\n", "\n");
        }
    } catch (err) {
        if (!useFallback) {
            throw err;
        }
    }

    if (!useFallback) {
        throw new KeyNotFoundError(collection, key, language);
    }

    const fallbackJson = await loadCollection(
        collection,
        customFallbackLanguage
    );

    if (!(key in fallbackJson)) {
        throw new KeyNotFoundError(
            collection,
            key,
            customFallbackLanguage
        );
    }

    return fallbackJson[key].replaceAll("\\n", "\n");
}