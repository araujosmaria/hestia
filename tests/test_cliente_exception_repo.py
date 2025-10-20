import pytest
from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.usuario import usuario_repo
from datetime import datetime


class TestClienteExceptions:
    """Testes para cobrir linhas faltantes do cliente_repo"""

    def test_inserir_cpf_duplicado(self, test_db):
        """Testa inserção com CPF duplicado - cobre linhas 230-231"""
        usuario_repo.criar_tabela()
        cliente_repo.criar_tabela()

        cliente1 = Cliente(
            id=0,
            nome="Cliente 1",
            dataNascimento="1990-01-01",
            email="cliente1@test.com",
            telefone="11999999999",
            cpf="12345678901",
            senha="senha123",
            perfil="cliente",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now(),
            cep="12345678",
            logradouro="Rua Teste",
            numero="100",
            complemento="Apto 1",
            bairro="Centro",
            cidade="São Paulo",
            estado="SP",
            ativo=True,
            parentesco_paciente="Filho",
            confirmarSenha="senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )

        id1 = cliente_repo.inserir(cliente1)
        assert id1 is not None

        # Tenta inserir com mesmo CPF
        cliente2 = Cliente(
            id=0,
            nome="Cliente 2",
            dataNascimento="1995-05-15",
            email="cliente2@test.com",
            telefone="11988888888",
            cpf="12345678901",  # CPF duplicado
            senha="senha456",
            perfil="cliente",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now(),
            cep="87654321",
            logradouro="Rua Outra",
            numero="200",
            complemento="Casa",
            bairro="Bairro",
            cidade="Rio de Janeiro",
            estado="RJ",
            ativo=True,
            parentesco_paciente="Pai",
            confirmarSenha="senha456",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )

        # Deve retornar None e printar erro (linhas 230-231)
        id2 = cliente_repo.inserir(cliente2)
        assert id2 is None
