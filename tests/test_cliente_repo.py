import random
import string
from datetime import datetime
import pytest
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_repo import (
    criar_tabela as criar_tabela_cliente,
    inserir,
    obter_todos,
    obter_por_id,
    excluir
)
from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario


class TestClienteRepo:

    def criar_cliente_fake(self) -> Cliente:
        """Cria um cliente válido e único para testes"""
        sufixo = ''.join(random.choices(string.digits, k=6))
        # Cria também o usuário interno, necessário para a inserção do cliente
        usuario = Usuario(
            id=None,
            nome=f"Usuário Teste {sufixo}",
            dataNascimento="2000-01-01",
            email=f"usuario{sufixo}@teste.com",
            telefone="123456789",
            cpf=f"123456{sufixo}",
            senha="Senha123",
            perfil="cliente",
            foto=None,
            token_redefinicao=None,
            data_token=None,
            data_cadastro=str(datetime.now().date()),
            cep="12345-000",
            logradouro="Rua Teste",
            numero="123",
            complemento="",
            bairro="Centro",
            cidade="Cidade",
            estado="Estado",
            ativo=True
        )

        # Retorna o cliente com os campos adicionais de teste
        return Cliente(
            id=None,
            nome=usuario.nome,
            dataNascimento=usuario.dataNascimento,
            email=usuario.email,
            telefone=usuario.telefone,
            cpf=usuario.cpf,
            senha=usuario.senha,
            perfil=usuario.perfil,
            foto=usuario.foto,
            token_redefinicao=usuario.token_redefinicao,
            data_token=usuario.data_token,
            data_cadastro=usuario.data_cadastro,
            cep=usuario.cep,
            logradouro=usuario.logradouro,
            numero=usuario.numero,
            complemento=usuario.complemento,
            bairro=usuario.bairro,
            cidade=usuario.cidade,
            estado=usuario.estado,
            ativo=usuario.ativo,
            parentesco_paciente="Filho",
            confirmarSenha="Senha123",
            termos=True,
            verificacao=True,
            comunicacoes=True
        )

    def test_criar_tabela(self, test_db):
        """Testa a criação da tabela de clientes"""
        criar_tabela_usuario()
        resultado = criar_tabela_cliente()
        assert resultado is True, "A criação da tabela deveria retornar True"

    def test_inserir(self, test_db):
        """Testa a inserção de um cliente"""
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_teste = self.criar_cliente_fake()

        id_cliente = inserir(cliente_teste)
        assert id_cliente is not None, "O cliente inserido não deveria ser None"

        cliente_db = obter_por_id(id_cliente)
        assert cliente_db is not None, "O cliente retornado não deveria ser None"
        assert cliente_db.parentesco_paciente == "Filho", "O parentesco do cliente não foi inserido corretamente"

    def test_obter_por_id(self, test_db):
        """Testa a busca de um cliente por ID"""
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_teste = self.criar_cliente_fake()
        id_cliente = inserir(cliente_teste)

        cliente_db = obter_por_id(id_cliente)
        assert cliente_db is not None, "O cliente retornado não deveria ser None"

    def test_obter_todos(self, test_db):
        """Testa a busca de todos os clientes"""
        criar_tabela_usuario()
        criar_tabela_cliente()
        inserir(self.criar_cliente_fake())
        inserir(self.criar_cliente_fake())

        lista_clientes = obter_todos()
        assert len(lista_clientes) >= 2, "Deveria retornar pelo menos 2 clientes"

    def test_excluir(self, test_db):
        """Testa a exclusão de um cliente"""
        criar_tabela_usuario()
        criar_tabela_cliente()
        cliente_teste = self.criar_cliente_fake()
        id_cliente = inserir(cliente_teste)

        resultado = excluir(id_cliente)
        cliente_db = obter_por_id(id_cliente)

        assert resultado is True, "A exclusão do cliente deveria retornar True"
        assert cliente_db is None, "O cliente excluído deveria ser None"
