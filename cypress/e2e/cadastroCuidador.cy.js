describe("Cadastro de Cuidador", () => {
    it("Deve preencher e enviar o formulário e retornar uma mensagem de sucesso", () => {
        cy.visit("http://127.0.0.1:8000/cadastro_cuidador");

        // Dados Pessoais
        cy.get("input[name='nome']").type("Lara Jean");
        cy.get("input[name='dataNascimento']").type("1990-05-15");
        cy.get("input[name='email']").type("lara@example.com");
        cy.get("input[name='telefone']").type("11999999999");
        cy.get("input[name='cpf']").type("12345678900");
        cy.get("select[name='especialidade']").select("idosos");
        cy.get("input[name='experiencia']").type("5");

        // Foto de Perfil (opcional)
        // Se quiser testar upload de imagem, precisa do plugin cypress-file-upload
        // cy.get("input[name='fotoPerfil']").attachFile("foto.jpg");

        // Localização
        cy.get("input[name='cep']").type("12345000");
        cy.get("input[name='logradouro']").type("Rua das Flores");
        cy.get("input[name='numero']").type("123");
        cy.get("input[name='bairro']").type("Centro");
        cy.get("input[name='cidade']").type("São Paulo");
        cy.get("input[name='estado']").type("SP");

        // Segurança da Conta
        cy.get("input[name='senha']").type("senhaSegura123");
        cy.get("input[name='confirmarSenha']").type("senhaSegura123");

        // Termos
        cy.get("input[name='termos']").check();

        // Enviar formulário
        cy.get('button[type="submit"]').click();

        // Verificar mensagem de sucesso
        cy.contains("Cadastro concluído com sucesso!").should('be.visible');
    });
});
