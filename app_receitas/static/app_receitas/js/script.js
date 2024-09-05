// Função para carregar o conteúdo via AJAX
function loadContent(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();  // Retorna o HTML como texto
        })
        .then(html => {
            document.getElementById('conteudo').innerHTML = html;  // Insere o conteúdo no container
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

// Carregar o conteúdo da página 'inicio.html' quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    loadContent('/inicio/');  // URL para o conteúdo que você deseja carregar
});
