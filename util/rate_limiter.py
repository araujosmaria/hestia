"""
Módulo de Rate Limiting para proteção contra força bruta.
Controla tentativas de login, cadastro e recuperação de senha.
"""
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, List


class SimpleRateLimiter:
    """
    Rate limiter simples baseado em memória.

    Rastreia tentativas por identificador (geralmente IP) em uma janela de tempo.
    Adequado para aplicações pequenas/médias. Para produção em escala, considere Redis.
    """

    def __init__(self, max_tentativas: int = 5, janela_minutos: int = 5):
        """
        Args:
            max_tentativas: Número máximo de tentativas permitidas
            janela_minutos: Janela de tempo em minutos
        """
        self.max_tentativas = max_tentativas
        self.janela = timedelta(minutes=janela_minutos)
        self.tentativas: Dict[str, List[datetime]] = defaultdict(list)

    def verificar(self, identificador: str) -> bool:
        """
        Verifica se o identificador está dentro do limite de tentativas.

        Args:
            identificador: Identificador único (ex: IP, email)

        Returns:
            True se dentro do limite (pode prosseguir)
            False se excedeu o limite (bloquear)
        """
        agora = datetime.now()

        # Limpar tentativas antigas fora da janela
        self.tentativas[identificador] = [
            t for t in self.tentativas[identificador]
            if agora - t < self.janela
        ]

        # Verificar se excedeu o limite
        if len(self.tentativas[identificador]) >= self.max_tentativas:
            return False

        # Registrar tentativa atual
        self.tentativas[identificador].append(agora)
        return True

    def resetar(self, identificador: str) -> None:
        """
        Reseta contador de tentativas para um identificador.
        Útil após login bem-sucedido.

        Args:
            identificador: Identificador único
        """
        if identificador in self.tentativas:
            del self.tentativas[identificador]

    def tentativas_restantes(self, identificador: str) -> int:
        """
        Retorna quantas tentativas restam para o identificador.

        Args:
            identificador: Identificador único

        Returns:
            Número de tentativas restantes
        """
        agora = datetime.now()

        # Limpar tentativas antigas
        self.tentativas[identificador] = [
            t for t in self.tentativas[identificador]
            if agora - t < self.janela
        ]

        tentativas_usadas = len(self.tentativas[identificador])
        return max(0, self.max_tentativas - tentativas_usadas)

    def tempo_ate_liberar(self, identificador: str) -> int:
        """
        Retorna quantos segundos faltam até liberar novas tentativas.

        Args:
            identificador: Identificador único

        Returns:
            Segundos até liberar (0 se já liberado)
        """
        if identificador not in self.tentativas or not self.tentativas[identificador]:
            return 0

        agora = datetime.now()
        tentativa_mais_antiga = min(self.tentativas[identificador])
        tempo_decorrido = agora - tentativa_mais_antiga

        if tempo_decorrido >= self.janela:
            return 0

        tempo_restante = self.janela - tempo_decorrido
        return int(tempo_restante.total_seconds())

    def limpar_expirados(self) -> int:
        """
        Remove todos os registros expirados de memória.
        Útil para executar periodicamente e liberar memória.

        Returns:
            Número de identificadores removidos
        """
        agora = datetime.now()
        identificadores_para_remover = []

        for identificador, tentativas in self.tentativas.items():
            # Filtrar tentativas válidas
            tentativas_validas = [t for t in tentativas if agora - t < self.janela]

            if not tentativas_validas:
                identificadores_para_remover.append(identificador)
            else:
                self.tentativas[identificador] = tentativas_validas

        for identificador in identificadores_para_remover:
            del self.tentativas[identificador]

        return len(identificadores_para_remover)
