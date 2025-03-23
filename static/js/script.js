document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("download-form");
    const speedElement = document.getElementById("speed");
    const etaElement = document.getElementById("eta");

    if (form && speedElement && etaElement) {
        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            const url = document.getElementById("url").value;

            // Avvia il download
            const response = await fetch("/download", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: `url=${encodeURIComponent(url)}`,
            });

            if (response.ok) {
                const blob = await response.blob();
                const downloadUrl = window.URL.createObjectURL(blob);
                const a = document.createElement("a");
                a.href = downloadUrl;
                a.download = "video.mp4";
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(downloadUrl);
            }
        });

        // Aggiorna lo stato del download ogni secondo
        setInterval(async () => {
            const response = await fetch("/status");
            const status = await response.json();

            speedElement.textContent = status.speed;
            etaElement.textContent = status.eta;
        }, 500);
    } else {
        console.error("Uno o più elementi del DOM non sono stati trovati.");
    }
});