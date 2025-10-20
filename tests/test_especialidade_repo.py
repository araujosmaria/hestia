import sys
import os
from data.especialidade.especialidade_repo import *
from data.especialidade.especialidade_model import Especialidade

class TestEspecialidadeRepo:
    def test_criar_tabela_especialidades(self, test_db):
        # Arrange
        # Act
        resultado = criar_tabela()
        # Assert
        assert resultado == True, "A criacao da tabela deveria retornar True"

    def test_inserir_especialidade(self, test_db):
        # Arrange
        criar_tabela()
        especialidade_teste =  Especialidade(0, "Especialidade Teste")
        # Act
        id_especialidade_inserida = inserir(especialidade_teste)
        assert id_especialidade_inserida is not None
        # Assert
        especialidade_db = obter_por_id (id_especialidade_inserida) 
        assert especialidade_db is not None, "A especialidade inserida não deveria ser None"
        assert especialidade_db.id == 1, "A especialidade inserida deveria ter um ID igual a 1"
        assert especialidade_db.nome == "Especialidade Teste", "O nome da especialidade inserida não confere"

    def test_atualizar_especialidade(self,test_db):
        # Arrange
        criar_tabela()
        especialidade_teste = Especialidade(0, "Especialidade Teste")
        id_especialidade_inserida = inserir(especialidade_teste)
        assert id_especialidade_inserida is not None
        especialidade_inserida = obter_por_id(id_especialidade_inserida)
        assert especialidade_inserida is not None
        # Act
        especialidade_inserida.nome = "Especialidade Atualizada"
        resultado = atualizar(especialidade_inserida)
        # Assert
        assert resultado == True, "A atualização da especialidade deveria retornar True"
        especialidade_db = obter_por_id(id_especialidade_inserida)
        assert especialidade_db is not None
        assert especialidade_db.nome == "Especialidade Atualizada", "O nome da categoria atualizada não confere"

    def test_excluir_especialidade(self, test_db):
        # Arrange
        criar_tabela()
        especialidade_teste = Especialidade(0, "Especialidade Teste")
        id_especialidade_inserida = inserir(especialidade_teste)
        assert id_especialidade_inserida is not None
        # Act
        resultado = excluir(id_especialidade_inserida)
        # Assert
        assert resultado == True, "O resultado da exclusão deveria retornar True"
        especialidade_db = obter_por_id(id_especialidade_inserida)
        assert especialidade_db is None, "A especialidade excluida deveria ser None"

    def test_obter_por_id(self, test_db):
        # Arrange
        criar_tabela()
        especialidade_teste = Especialidade(0, "Especialidade Teste")
        id_especialidade_inserida = inserir(especialidade_teste)
        assert id_especialidade_inserida is not None
        # Act
        especialidade_db = obter_por_id(id_especialidade_inserida)
        # Assert
        assert especialidade_db is not None, "A especialidade retornada não deveria ser None"
        assert especialidade_db.id == id_especialidade_inserida, "O ID da especialidade buscada deveria ser igual ao id da especialidade inserida"
        assert especialidade_db.nome == especialidade_teste.nome, "O nome da especialidade buscada deveria ser igual ao nome da categoria inserida"

    def test_obter_todos(self, test_db):
        # Arrange
        criar_tabela()
        inserir(Especialidade(0, "Especialidade A"))
        inserir(Especialidade(0, "Especialidade B"))
        # Act
        lista_especialidades = obter_todos()                                                                                            
        # Assert
        assert len(lista_especialidades) >= 2, "Deveria retornar pelo menos 2 especialidades"
        nomes = [e.nome for e in lista_especialidades]
        assert "Especialidade A" in nomes, "Especialidade A deveria estar na lista"
        assert "Especialidade B" in nomes, "Especialidade B deveria estar na lista"       