const header = document.querySelector('#header');
const closeHeader = document.querySelector('.close-header');

closeHeader.addEventListener("click", () => {
    header.classList.toggle('header-hidden');
});

let headerHiddenApplied = false;

function handleResize() {
    if (window.innerWidth < 1000 && !headerHiddenApplied) {
        header.classList.add('header-hidden');
        headerHiddenApplied = true;
    } else if (window.innerWidth >= 1000) {
        headerHiddenApplied = false;
    }
}

// Chama na carga da página
handleResize();

// Monitora redimensionamento
window.addEventListener('resize', handleResize);