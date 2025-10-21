"""
Gerenciador de transações para operações atômicas multi-tabela.

Uso:
    from util.transaction import transaction

    with transaction() as cursor:
        usuario_repo.inserir(usuario, cursor)
        cliente_repo.inserir(cliente, cursor)
        # Commit automático ao sair
        # Rollback automático em caso de exceção
"""
from contextlib import contextmanager
from typing import Generator
import sqlite3
from util.db_util import get_connection
from util.logger_config import logger


@contextmanager
def transaction() -> Generator[sqlite3.Cursor, None, None]:
    """
    Context manager para transações atômicas.

    Gerencia automaticamente commit/rollback:
    - Commit ao sair com sucesso
    - Rollback em caso de exceção

    Uso:
        with transaction() as cursor:
            usuario_repo.inserir(usuario, cursor)
            cliente_repo.inserir(cliente, cursor)
            # Commit automático ao sair
            # Rollback automático se houver exceção

    Yields:
        sqlite3.Cursor: Cursor para executar operações

    Raises:
        Exception: Re-raise qualquer exceção após rollback
    """
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        logger.debug("Transação iniciada")

        yield cursor

        conn.commit()
        logger.debug("Transação commitada com sucesso")

    except Exception as e:
        if conn:
            conn.rollback()
            logger.warning(f"Transação revertida devido a erro: {e}")
        raise

    finally:
        if conn:
            conn.close()
            logger.debug("Conexão fechada")
