from typing import Optional
from data.agenda.agenda_model import Agenda
from data.agenda.agenda_sql import *
from data.util import open_connection
from hestia.data.agenda.agenda_repo import criar_tabela, inserir, obter_todos, excluir, obter_por_id, atualizar

class TestAgendaRepo:
    def test_criar_tabela(self) -> bool:
        try:
            with open_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(CRIAR_TABELA_AGENDA)
                conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao criar tabela de agendas: {e}")
            return False  


    def test_inserir_agenda(self, test_db):
        criar_tabela()
        agenda_teste = Agenda(
            id_agenda = 0,
            dataHora="2025-07-01 11:00:00",
            disponibilidade=True,
            id_cuidador=1
        )
        id_agenda = inserir(agenda_teste)
        assert isinstance(id_agenda, int) and id_agenda > 0

        # Buscar todas as agendas para verificar se a inserção foi feita
        agendas = obter_todos()

        agenda_inserida = next((a for a in agendas if a.id_agenda == id_agenda), None)
        assert agenda_inserida is not None
        assert agenda_inserida.dataHora == agenda_teste.dataHora
        assert agenda_inserida.disponibilidade == agenda_teste.disponibilidade
        assert agenda_inserida.id_cuidador == agenda_teste.id_cuidador



    def test_obter_todos(self) -> list[Agenda]:
        with open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(OBTER_TODOS_AGENDA)
            rows = cursor.fetchall()
            agendas = [
                Agenda(
                    id_agenda=row["id_agenda"],
                    dataHora=row["dataHora"],
                    disponibilidade=row["disponibilidade"],
                    id_cuidador=row["id_cuidador"]
                )
                for row in rows
            ]
            return agendas


    def test_atualizar(self) -> bool:
        criar_tabela()
        agenda_teste = Agenda(
            id_agenda = 0,
            dataHora="2025-07-01 11:00:00",
            disponibilidade=True,
            id_cuidador=1
        )
        id_agenda = inserir(agenda_teste)
        agenda_inserida = obter_por_id(id_agenda=id_agenda)
        # Act
        agenda_inserida.nome = "Especialidade Atualizada"
        resultado = atualizar(agenda_inserida)
        # Assert
        assert resultado == True, "A atualização da especialidade deveria retornar True"


    def test_excluir(self) -> bool:
        # Arrange
        criar_tabela()
        agenda_teste = Agenda(
            id_agenda = 0,
            dataHora="2025-07-01 11:00:00",
            disponibilidade=True,
            id_cuidador=1
        )
        id_agenda = inserir(agenda_teste)
        # Act
        resultado = excluir(id_agenda)
        # Assert
        assert resultado == True, "O resultado da exclusão deveria retornar True"
        # especialidade_db = obter_por_id(id_especialidade_inserida)
        # assert especialidade_db is None, "A especialidade excluida deveria ser None"