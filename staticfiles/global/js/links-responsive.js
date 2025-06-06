const link_menu = document.querySelector('.toggle');
const overlay = document.querySelector('.overlay');
const close_menu = document.querySelector(".close-menu");
const menu = document.querySelector(".links");
let menuIsOpen = false;

link_menu.addEventListener('click', () => {
    overlay.style.display = 'block';
    menu.style.right = '0px';
    menuIsOpen = true;
});

close_menu.addEventListener("click", () => {
    overlay.style.display = 'none';
    menu.style.right = '-300px';
    menuIsOpen = false;
});

overlay.addEventListener("click", () => {
    overlay.style.display = 'none';
    menu.style.right = '-300px';
    menuIsOpen = false;
});

function ajustarMenu() {
    if (window.innerWidth > 1000) {
        menu.style.right = '0px';
        overlay.style.display = 'none';
    } else {
        if (!menuIsOpen) {
            menu.style.right = '-300px';
        }
    }
}

ajustarMenu();

window.addEventListener('resize', ajustarMenu);