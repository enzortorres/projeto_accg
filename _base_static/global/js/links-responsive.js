//! Menu Responsivo
const link_menu = document.querySelector('.toggle');
const overlay = document.querySelector('.overlay')
const close = document.querySelector(".close-menu");
const menu = document.querySelector(".links");
var menuIsOpen = false;

link_menu.addEventListener('click', () => {
    overlay.style.display = 'block';
    menu.style.right = '0px';
});

close.addEventListener("click", () => {
    overlay.style.display = 'none';
    menu.style.right = '-300px';
});

overlay.addEventListener("click", () => {
    overlay.style.display = 'none';
    menu.style.right = '-300px';
});

function ajustarMenu() {
    if (window.innerWidth > 1000) {
        menu.style.right = '0px';
    } else {
        menu.style.right = '-300px'
    }
}

ajustarMenu();

// window.addEventListener('resize', ajustarMenu);