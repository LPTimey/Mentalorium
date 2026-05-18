"use strict";

import { getTranslation } from "./i18n.mjs";
import { parseURLParams } from "./params.mjs"

const area = /** @type {HTMLTextAreaElement} */(
    document.getElementById("query")
);

const { persona, lang } = parseURLParams();
// @ts-ignore
const situation = await getTranslation(persona, "situation", lang)
// @ts-ignore
const prompt = await getTranslation("index", "prompt", lang)

area.value = ""
area.value = prompt
// area.value = `${situation}\n${prompt}`
area.dispatchEvent(new Event("change"));
area.dispatchEvent(new Event("input"));
