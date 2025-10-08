
describe("Cadastro de usuário", ()=>{
    it("Deve preencher e enviar o formulário e retornar uma mensagem de sucesso", ()=>{
        cy.visit("http://127.0.0.1:8000/cadastro_cuidador")

        //Preencha campos do formulário
        cy.get("input[name='nome']").type("João")
        cy.get("input[name='dataNascimento']").type("1990-01-01")
        cy.get("input[name='email']").type("joaozinhodoviolao@gmail.com")
        cy.get("input[name='cpf']").type("147.258.369-12")
        cy.get("input[name='telefone']").type("28999142536")
        cy.get("input[name='cep']").type("29310258")
        cy.get("input[name='logradouro']").type("Rua João da Musica")
        cy.get("input[name='numero']").type("10")
        cy.get("input[name='bairro']").type("BNH")
        cy.get("input[name='cidade']").type("Cachoeiro de Itapemirim")
        cy.get("input[name='estado']").type("ES") //Só tem valor 1 na hora de escolher o estado.
        cy.get("select[name='experiencia']").select("1-2")
        cy.get("select[name='escolaridade']").select("tecnico")
        cy.get("input[name='senha']").type("123456789")
        cy.get("input[name='valorHora']").type("25")
        cy.get("textarea[name='apresentacao']").type("tecnico em enfermagem com 5 anos de experiência")
        cy.get("textarea[name='cursos']").type("enfermagem")
        cy.get("input[name='senha']").type("123456789")
        cy.get("input[name='confirmarSenha']").type("123456789")
        cy.get("input[name='termos']").check()
        cy.get("input[name='verificacao']").check()
        cy.get("input[name='comunicacoes']").check()


        cy.get('button[id="btn_cadastro_cuidador"]').click()
        
    })
})