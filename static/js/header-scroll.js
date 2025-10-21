/**
 * Header Scroll Behavior
 * Esconde o header ao rolar para baixo e mostra ao rolar para cima
 */
(function() {
    let lastScrollTop = 0;
    const header = document.querySelector('.header-cadastro');

    // Se o header não existir na página, não faz nada
    if (!header) return;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScroll > lastScrollTop && currentScroll > 100) {
            // Scrolling down - esconde o header
            header.classList.add('hidden');
        } else {
            // Scrolling up - mostra o header
            header.classList.remove('hidden');
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    });
})();
