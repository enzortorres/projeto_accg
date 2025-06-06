document.addEventListener("DOMContentLoaded", () => {
    const idadeEl = document.getElementById("idade-formatada");

    if (idadeEl) {
        const texto = idadeEl.textContent.trim();

        const posE = texto.indexOf(" e ");
        if (posE !== -1) {
            const anos = texto.substring(0, posE).trim();
            const meses = texto.substring(posE + 3).trim();

            idadeEl.innerHTML = `
                <div class="idade-anos">${anos}</div>
                <div class="idade-meses">e ${meses}</div>
            `;
        } else {
            // Se não tiver "e", decide se é só anos ou só meses
            if (texto.includes("Ano")) {
                idadeEl.innerHTML = `<div class="idade-anos">${texto}</div>`;
            } else {
                idadeEl.innerHTML = `<div class="idade-meses">${texto}</div>`;
            }
        }
    }
});
