
// Parte de Avaliações (home_medico.html)
// Seleciona a div de avaliações
const avaliarDiv = document.querySelector('.avaliar-info');

// Esconde a div de avaliações inicialmente
avaliarDiv.style.display = 'none';

// Seleciona o botão de avaliar
const buttonsAvaliar = document.querySelectorAll('.but_avaliar');
buttonsAvaliar.forEach(button => {
    button.addEventListener("click", abrirAvaliar);
});

// Seleciona o botão de fechar
const fecharButton = document.querySelector('.close-avalia');
fecharButton.addEventListener("click", fecharAvaliar);

// Função para abrir a div de avaliações
function abrirAvaliar() {
    avaliarDiv.style.display = 'block';
}

// Função para fechar a div de avaliações
function fecharAvaliar() {
    avaliarDiv.style.display = 'none';
}
