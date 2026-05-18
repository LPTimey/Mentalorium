"use strict";

const textAreas = document.querySelectorAll("textarea");

textAreas.forEach(textarea => {

    const resize = () => {
        textarea.style.height = "auto";

        const styles = getComputedStyle(textarea);

        const maxRows = Number(textarea.dataset.maxRows) || 5;

        const lineHeight = parseFloat(styles.lineHeight);

        const paddingTop = parseFloat(styles.paddingTop);
        const paddingBottom = parseFloat(styles.paddingBottom);

        const verticalPadding = paddingTop + paddingBottom;

        const maxHeight =
            (lineHeight * maxRows) + verticalPadding;

        textarea.style.height =
            Math.min(textarea.scrollHeight + paddingBottom, maxHeight) + "px";

        textarea.style.overflowY =
            textarea.scrollHeight > maxHeight
                ? "auto"
                : "hidden";
    };

    textarea.addEventListener("input", resize);

    resize();
});