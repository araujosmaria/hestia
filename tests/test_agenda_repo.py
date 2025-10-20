from datetime import datetime
from typing import Optional
from data.agenda.agenda_model import Agenda
from data.agenda.agenda_sql import *
from data.util import open_connection
from data.agenda.agenda_repo import criar_tabela, inserir, obter_todos, excluir, obter_por_id, atualizar

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
            dataHora=datetime(2025, 7, 1, 11, 0, 0),
            disponibilidade=True,
            id_cuidador=1
        )
        id_agenda = inserir(agenda_teste)
        assert isinstance(id_agenda, int) and id_agenda > 0
        agendas = obter_todos()

        agenda_inserida = next((a for a in agendas if a.id_agenda == id_agenda), None)
        assert agenda_inserida is not None
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
        
    def test_obter_por_id(self):
        criar_tabela()
        agenda_teste = Agenda(
            id_agenda=0,
            dataHora=datetime(2025, 7, 1, 11, 0, 0),
            disponibilidade=True,
            id_cuidador=1
        )
        id_agenda = inserir(agenda_teste)
        assert id_agenda is not None

        agenda = obter_por_id(id_agenda)

        assert agenda is not None
        assert agenda.id_agenda == id_agenda
        assert isinstance(agenda.dataHora, (str, datetime))
        assert agenda.disponibilidade in [True, False, 0, 1]
        assert isinstance(agenda.id_cuidador, int)


    def test_atualizar(self):
        criar_tabela()
        agenda_teste = Agenda(
            id_agenda=0,
            dataHora=datetime(2025, 7, 1, 11, 0, 0),
            disponibilidade=True,
            id_cuidador=1
        )
        id_agenda = inserir(agenda_teste)
        assert id_agenda is not None
        agenda_inserida = obter_por_id(id_agenda)
        assert agenda_inserida is not None

        # Atualize um campo válido
        agenda_inserida.disponibilidade = False
        resultado = atualizar(agenda_inserida)

        assert resultado == True, "A atualização da agenda deveria retornar True"

        # Verifique se atualizou no banco
        agenda_atualizada = obter_por_id(id_agenda)
        assert agenda_atualizada is not None
        assert agenda_atualizada.disponibilidade == False



    def test_excluir(self):
        # Arrange
        criar_tabela()
        agenda_teste = Agenda(
            id_agenda = 0,
            dataHora=datetime(2025, 7, 1, 11, 0, 0),
            disponibilidade=True,
            id_cuidador=1
        )
        id_agenda = inserir(agenda_teste)
        assert id_agenda is not None
        # Act
        resultado = excluir(id_agenda)
        # Assert
        assert resultado == True, "O resultado da exclusão deveria retornar True"