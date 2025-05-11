document.addEventListener('DOMContentLoaded', function() {
    // Funcionalidade de pesquisa
    const searchInput = document.getElementById('produto-search');
    const produtos = document.querySelectorAll('.produto-item');
    const noProdutos = document.getElementById('no-products');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            let searchTerm = this.value.toLowerCase();
            let encontrouAlgum = false;
            
            produtos.forEach(produto => {
                const produtoNome = produto.querySelector('h3').textContent.toLowerCase();
                const produtoDesc = produto.querySelector('p') ? produto.querySelector('p').textContent.toLowerCase() : '';
                
                if (produtoNome.includes(searchTerm) || produtoDesc.includes(searchTerm)) {
                    produto.style.display = 'block';
                    encontrouAlgum = true;
                } else {
                    produto.style.display = 'none';
                }
            });
            
            if (noProdutos) {
                noProdutos.style.display = encontrouAlgum ? 'none' : 'block';
            }
        });
    }
    
    // Funcionalidade do seletor de página
    const pageSelectors = document.querySelectorAll('.page-selector');
    pageSelectors.forEach(selector => {
        selector.addEventListener('change', function() {
            window.location.href = this.value;
        });
    });
    
    // Botão voltar ao topo
    const backToTop = document.querySelector('.back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });
        
        backToTop.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
 
    const paginationLinks = document.querySelectorAll('.pagination-controls a');
    paginationLinks.forEach(link => {
        link.addEventListener('click', function() {
            localStorage.setItem('scrollPosition', window.pageYOffset);
        });
    });
    
    // Restaurar posição ao carregar a página
    if (performance.navigation.type === 1) { // 1 é page reload
        localStorage.removeItem('scrollPosition');
    } else {
        const savedPosition = localStorage.getItem('scrollPosition');
        if (savedPosition) {
            window.scrollTo(0, parseInt(savedPosition));
            // Remover após uso
            localStorage.removeItem('scrollPosition');
        }
    }
});
