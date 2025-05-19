const header = document.querySelector('#header');
const closeHeader = document.querySelector('button.close-header');

closeHeader.addEventListener("click", () => {
    header.classList.toggle('show');
});
