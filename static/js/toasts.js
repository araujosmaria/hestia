/**
 * Sistema de Toasts Bootstrap 5
 * Lê mensagens do JSON e exibe como toasts Bootstrap 5
 *
 * Uso no backend:
 *   from util.flash_messages import informar_sucesso, informar_erro
 *   informar_sucesso(request, "Operação realizada com sucesso!")
 *   informar_erro(request, "Erro ao processar dados")
 *
 * Uso no frontend (programático):
 *   window.exibirToast('Mensagem aqui', 'success')
 *   window.exibirToast('Atenção!', 'warning')
 */

document.addEventListener('DOMContentLoaded', function() {
    // Obter mensagens do script JSON
    const mensagensElement = document.getElementById('mensagens-data');

    if (!mensagensElement) {
        return;
    }

    try {
        const mensagens = JSON.parse(mensagensElement.textContent || '[]');

        // Mapeamento de tipos de mensagem para classes Bootstrap
        const tipoMap = {
            'sucesso': 'success',
            'erro': 'danger',
            'aviso': 'warning',
            'info': 'info'
        };

        // Exibir cada mensagem
        mensagens.forEach(msg => {
            const tipoBootstrap = tipoMap[msg.tipo] || 'info';
            mostrarToast(msg.texto, tipoBootstrap);
        });
    } catch (e) {
        console.error('Erro ao processar mensagens:', e);
    }
});

/**
 * Exibe um toast na tela
 * @param {string} mensagem - Texto da mensagem
 * @param {string} tipo - Tipo do toast (success, danger, warning, info)
 * @param {number} delay - Tempo em ms antes de auto-dismiss (padrão: 5000)
 */
function mostrarToast(mensagem, tipo = 'info', delay = 5000) {
    const container = document.getElementById('toast-container');

    if (!container) {
        console.error('Container de toasts não encontrado');
        return;
    }

    // Gerar ID único para o toast
    const id = 'toast-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);

    // Criar elemento do toast
    const toastElement = document.createElement('div');
    toastElement.className = `toast align-items-center text-bg-${tipo} border-0`;
    toastElement.setAttribute('role', 'alert');
    toastElement.setAttribute('aria-live', 'assertive');
    toastElement.setAttribute('aria-atomic', 'true');
    toastElement.id = id;

    // Ícones para cada tipo
    const icones = {
        'success': '<i class="bi bi-check-circle-fill me-2"></i>',
        'danger': '<i class="bi bi-exclamation-circle-fill me-2"></i>',
        'warning': '<i class="bi bi-exclamation-triangle-fill me-2"></i>',
        'info': '<i class="bi bi-info-circle-fill me-2"></i>'
    };

    const icone = icones[tipo] || '';

    toastElement.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${icone}${mensagem}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto"
                    data-bs-dismiss="toast" aria-label="Fechar"></button>
        </div>
    `;

    // Adicionar ao container
    container.appendChild(toastElement);

    // Inicializar e mostrar toast
    const bsToast = new bootstrap.Toast(toastElement, {
        autohide: true,
        delay: delay
    });

    bsToast.show();

    // Remover elemento do DOM após ser escondido
    toastElement.addEventListener('hidden.bs.toast', () => {
        toastElement.remove();
    });
}

/**
 * Função global para exibir toasts programaticamente
 *
 * Exemplos:
 *   window.exibirToast('Salvo com sucesso!', 'success')
 *   window.exibirToast('Erro ao carregar', 'danger')
 *   window.exibirToast('Atenção necessária', 'warning')
 *   window.exibirToast('Informação útil', 'info')
 *   window.exibirToast('Mensagem longa', 'info', 10000) // 10 segundos
 */
window.exibirToast = mostrarToast;
