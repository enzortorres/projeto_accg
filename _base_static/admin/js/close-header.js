const body = document.querySelector('body');
if (!body.classList.contains('login')) {
const header = document.querySelector('#header');
    const closeHeader = document.querySelector('.close-header');

    closeHeader.addEventListener("click", () => {
        body.classList.toggle('header-hidden');
    });

    let headerHiddenApplied = false;

    function handleResize() {
        if (window.innerWidth < 1000 && !headerHiddenApplied) {
            body.classList.add('header-hidden');
            headerHiddenApplied = true;
        } else if (window.innerWidth >= 1000) {
            headerHiddenApplied = false;
        }
    }

    handleResize();
    window.addEventListener('resize', handleResize);
}
