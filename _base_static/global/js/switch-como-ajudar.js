const switchButton = document.querySelector('.switch');
const contents = [
    document.querySelector('.content-doe'),
    document.querySelector('.content-adote'),
    document.querySelector('.content-apadrinhe')
];

let i = 0;

const opcoes = ['opcao1', 'opcao2', 'opcao3'];
const positions = ['0px', 'calc(50% - 150px)', 'calc(100% - 300px)'];

switchButton.classList.add(opcoes[i]);
switchButton.style.left = positions[i];

function updateContent(index) {
    contents.forEach((content, idx) => {
        content.classList.remove('fade-in');
        content.classList.add('hidden');

        if (idx === index) {
            content.classList.remove('hidden');

            // Garante que a animação é reativada mesmo se for o mesmo elemento
            setTimeout(() => {
                content.classList.add('fade-in');
            }, 10);
        }
    });
}

updateContent(i);

switchButton.addEventListener("click", () => {
    switchButton.classList.remove(opcoes[i]);

    i = (i + 1) % opcoes.length;

    switchButton.classList.add(opcoes[i]);
    switchButton.style.left = positions[i];

    updateContent(i);
});
