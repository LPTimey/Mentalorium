if ("serviceWorker" in navigator) {
    window.addEventListener("load", async () => {
        try {
            const registration = await navigator.serviceWorker.register("./sw.js");

            console.log("Service Worker registriert:", registration);

            registration.update();
        } catch (error) {
            console.error("SW Registrierung fehlgeschlagen:", error);
        }
    });
}