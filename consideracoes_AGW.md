# Tipografia
aplique ao menos 2  diferentes familias tipográficas ao projeto.

# Cores
Escolha a cor que será a principal do seu projeto, a cor escolhida para os botões por exemplo, e faça ao menos 5 variações da mesma. Mesmo que não vá aplicar, apenas para te-la disponivel caso precise.

# Faça uso de variaveis CSS
visando facilitar a manutenção no projeto de vocês façam uso de variaveis css. Para não precisar ficar digitando o hexadecimal ou rgb de uma cor ou fonte toda vez que quiser usar, veja este exemplo. 

```
:root{
    --cor-hestia-base:#fff;
    --cor-hestia-main: #2B8C6A;
    --cor-hestia-main-800: #0a3f2cff; //quanto mais escura for a cor maior o numero (800), quanto mais clara menor, isso é apenas um acordo de padronização;
    --cor-hestia-main-100: #9ee5cbff; //quanto mais escura for a cor maior o numero (100), quanto mais clara menor, isso é apenas um acordo de padronização;
    --cor-hestia-dark: #090A0B;
    --cor-hestia-danger: #DC4343;
    --cor-hestia-warning: #ECC86B;
    // fonts - digamos que tenham escolhido as fontes MontSerrat para titulos, e Inter para textos. Lembrem-se de escolher fonts que apresentem contraste uma das outras.
    --font-principal: "Montserrat", sans-serif;
    --font-secundaria: "Inter", sans-serif;
}
```

Agora sempre que quiser usar uma cor, seja no texto, background, borda, etc basta usar a função css var() e passar o nome da variavel definida no root.

exemplo:
```
.header{
    background-color: var(--cor-hestia-base); //Se a cor de base do projeto de vocês por algum motivo deixar de ser branca você altera o hexadecial la em root ao invés de fazer diretamente aqui em .header
}
```

caso você queira padronizar os botões do seu projeto, o uso desse recurso é bastante útil também. pois ao invés de colocar font pelo nome e cor pelo hexadecimal ou rgb você usa as variaveis, ex:

```
.btn{
    backgroun-color: var(--cor-hestia-main); //cor do fundo verde principal do overleaf;
    font-family: var(--font-principal); //font montserrat
    border-color: var(--hestia-main-800); //borda verde escuro
}
```