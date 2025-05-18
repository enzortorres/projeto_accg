const switchButton = document.querySelector('.conteudo');
let i = 0;

const opcoes = ['opcao1', 'opcao2', 'opcao3'];
const positions = ['0px', 'calc(50% - 150px)', 'calc(100% - 300px)'];

switchButton.classList.add(opcoes[i]);
switchButton.style.left = positions[i];

switchButton.addEventListener("click", () => {
    switchButton.classList.remove(opcoes[i]);

    i = (i + 1) % opcoes.length;

    switchButton.classList.add(opcoes[i]);
    switchButton.style.left = positions[i];
});
