from data.administrador.administrador_model import Administrador
from data.administrador.administrador_repo import (
    criar_tabela,
    inserir,
    obter_todos,
    obter_por_id,
    atualizar,
    excluir
)
# from data.usuario.usuario_repo import criar_tabela as criar_tabela_usuario

class TestAdministradorRepo:
    def test_criar_tabela(self, test_db):
        # criar_tabela_usuario()  
        resultado = criar_tabela()
        assert resultado == True, "A criação da tabela de administradores deveria retornar True"

    def test_inserir_administrador(self, test_db):
        # criar_tabela_usuario()
        criar_tabela()

        admin = Administrador(
            id=None,
            nome="Admin Teste",
            email="admin@test.com",
            senha="senha123",
            telefone="123456789"
        )

        id_inserido = inserir(admin)
        assert id_inserido is not None, "Deveria retornar id ao inserir administrador"

        admin_db = obter_por_id(id_inserido)
        assert admin_db is not None, "Administrador inserido não deveria ser None"
        assert admin_db.nome == admin.nome
        assert admin_db.email == admin.email

    def test_obter_todos_administradores(self, test_db):
        # criar_tabela_usuario()
        criar_tabela()

        inserir(Administrador(nome="Admin A", email="a@admin.com", senha="senhaA", telefone="1111", id=None))
        inserir(Administrador(nome="Admin B", email="b@admin.com", senha="senhaB", telefone="2222", id=None))

        lista = obter_todos()
        nomes = [a.nome for a in lista]

        assert "Admin A" in nomes
        assert "Admin B" in nomes
        assert len(lista) >= 2

    def test_obter_por_id(self, test_db):
        # criar_tabela_usuario()
        criar_tabela()

        admin = Administrador(nome="Admin Teste", email="teste@admin.com", senha="123", telefone="123456", id=None)
        id_admin = inserir(admin)
        assert id_admin is not None

        admin_db = obter_por_id(id_admin)
        assert admin_db is not None
        assert admin_db.id == id_admin
        assert admin_db.nome == admin.nome

    def test_atualizar_administrador(self, test_db):
        # criar_tabela_usuario()
        criar_tabela()

        admin = Administrador(nome="Admin Antigo", email="antigo@admin.com", senha="senha", telefone="123", id=None)
        id_admin = inserir(admin)
        assert id_admin is not None

        admin_atualizado = Administrador(
            id=id_admin,
            nome="Admin Atualizado",
            email="novo@admin.com",
            senha="nova",
            telefone="999"
        )

        resultado = atualizar(admin_atualizado)
        assert resultado == True

        atualizado = obter_por_id(id_admin)
        assert atualizado is not None
        assert atualizado.nome == "Admin Atualizado"
        assert atualizado.email == "novo@admin.com"

    def test_excluir_administrador(self, test_db):
        # criar_tabela_usuario()
        criar_tabela()

        admin = Administrador(nome="Excluir Admin", email="del@admin.com", senha="senha", telefone="000", id=None)
        id_admin = inserir(admin)
        assert id_admin is not None

        resultado = excluir(id_admin)
        assert resultado == True

        admin_db = obter_por_id(id_admin)
        assert admin_db is None