/**
 * Chat - Funcionalidades dos templates de chat
 * Implementa o botão "Responder" que adiciona menção ao autor no textarea
 */
(function() {
    document.addEventListener('DOMContentLoaded', function() {
        const buttons = document.querySelectorAll('.responder-btn');
        const textarea = document.getElementById('mensagem');

        // Se não encontrar os elementos, não executa
        if (!textarea || buttons.length === 0) return;

        buttons.forEach(button => {
            button.addEventListener('click', () => {
                const autor = button.getAttribute('data-autor');
                // Preenche o textarea com uma menção e foca o campo
                textarea.value = `@${autor} `;
                textarea.focus();
            });
        });
    });
})();
