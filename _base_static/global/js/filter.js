const checkboxes = document.querySelectorAll('.filter-checkbox');
const container = document.getElementById('animais-container');
const resetBtn = document.querySelector('.reset');

function carregarAnimaisComFiltros(filtros) {
    const urlFiltros = filtros.length ? `?filtros=${filtros.join(',')}` : '';
    fetch(`/animais/${urlFiltros}`, {
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
    .then(response => response.text())
    .then(html => {
        container.innerHTML = html;

        const btn = document.getElementById('ver-mais-btn');
        if (btn) btn.remove();
    });
}

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', () => {
        const selected = Array.from(checkboxes)
            .filter(cb => cb.checked)
            .map(cb => cb.value);

        carregarAnimaisComFiltros(selected);
    });
});

resetBtn.addEventListener('click', () => {
    checkboxes.forEach(cb => cb.checked = false);
    window.location.href = window.location.pathname;
});
