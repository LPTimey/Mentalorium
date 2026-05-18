
/**
 * @typedef {"silent" | "loud"} Mode
 */

/**
 * @typedef {Object} URLParams
 * @property {string | null} lang
 * @property {string | null} persona
 * @property {boolean | null} answerQuality
 * @property {Mode | null} mode
 */

/**
 * Reads URL query parameters from the current page.
 *
 * Example:
 * ?lang=en&persona=teacher&answer=good&mode=silent
 *
 * @returns {URLParams}
 */
export function parseURLParams() {
    const params = new URLSearchParams(window.location.search);

    return {
        lang: params.get("lang"),
        persona: params.get("persona"),
        answerQuality: /** @type {boolean | null} */ (
            params.get("answer") === "true"
        ),
        mode: /** @type {Mode | null} */ (
            params.get("mode")
        )
    };
}

/**
 * @typedef {Object} SetURLParamsOptions
 * @property {string=} lang
 * @property {string=} persona
 * @property {boolean=} answerQuality
 * @property {Mode=} mode
 */

/**
 * Updates the browser URL query parameters.
 *
 * @param {SetURLParamsOptions} options
 * @returns {void}
 */
export function setURLParams({
    lang,
    persona,
    answerQuality,
    mode
}) {
    const params = new URLSearchParams(window.location.search);

    if (lang !== undefined) params.set("lang", lang);
    if (persona !== undefined) params.set("persona", persona);
    if (answerQuality !== undefined) {
        params.set("answer", String(answerQuality));
    }
    if (mode !== undefined) params.set("mode", mode);

    window.history.replaceState(
        {},
        "",
        `${window.location.pathname}?${params.toString()}`
    );
}