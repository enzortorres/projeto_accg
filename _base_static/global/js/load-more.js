document.addEventListener('DOMContentLoaded', function () {
    const btn = document.getElementById('ver-mais-btn');
    if (!btn) return;

    btn.addEventListener('click', async () => {
        const nextPage = btn.dataset.nextPage;
        if (!nextPage) return;

        btn.disabled = true;
        btn.innerText = "Carregando...";

        const filtros = btn.dataset.filtros;
        const url = new URL(window.location.href);
        url.searchParams.set('page', nextPage);
        if (filtros) {
            url.searchParams.set('filtros', filtros);
        }

        const response = await fetch(url.toString(), {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        });

        if (response.ok) {
            const html = await response.text();
            document.getElementById('animais-container').insertAdjacentHTML('beforeend', html);

            const newNextPage = parseInt(nextPage) + 1;
            const totalPages = parseInt(btn.dataset.totalPages);

            if (newNextPage > totalPages) {
                btn.remove();
            } else {
                btn.dataset.nextPage = newNextPage;
                btn.disabled = false;
                btn.innerText = "Ver mais";
            }
        } else {
            btn.innerText = "Erro ao carregar";
        }
    });
});
