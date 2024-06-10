from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Definindo uma classe abstrata para o Assunto
class Assunto(ABC):
    @abstractmethod
    def anexar(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def desanexar(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def notificar(self) -> None:
        pass

    @abstractmethod
    def evento_aprovado(self) -> bool:
        pass

# Classe concreta que atua como um sistema de eventos, implementando Assunto
class SistemaEventos(Assunto):
    _observadores: List[Observador] = []
    _evento_aprovado: bool = False

    def definir_evento_aprovado(self, aprovado: bool) -> None:
        self._evento_aprovado = aprovado

    def evento_aprovado(self) -> bool:
        return self._evento_aprovado

    # Método para anexar um observador à lista de observadores
    def anexar(self, observador: Observador) -> None:
        print(f"SistemaEventos: Observador {observador.__class__.__name__} anexado.")
        self._observadores.append(observador)

    # Método para desanexar um observador da lista de observadores
    def desanexar(self, observador: Observador) -> None:
        print(f"SistemaEventos: Observador {observador.__class__.__name__} desanexado.")
        self._observadores.remove(observador)

    # Método para notificar todos os observadores sobre uma mudança de estado
    def notificar(self) -> None:
        print("SistemaEventos: Notificando observadores sobre o novo registro de evento...")
        for observador in self._observadores:
            if isinstance(observador, Administrador) or (isinstance(observador, UsuarioGeral) and self.evento_aprovado()):
                observador.atualizar(self)

    # Método para registrar um observador para um evento específico
    def registrar_para_evento(self, usuario: Observador) -> None:
        print(f"SistemaEventos: {usuario.__class__.__name__} está se registrando para um evento.")
        self.anexar(usuario)
        self.notificar()

# Definindo uma classe abstrata para o Observador
class Observador(ABC):
    @abstractmethod
    def atualizar(self, assunto: Assunto) -> None:
        pass

# Implementação concreta de um tipo de observador: Usuário Geral
class UsuarioGeral(Observador):
    def atualizar(self, assunto: Assunto) -> None:
        print("UsuarioGeral: Recebeu notificação sobre o registro de evento aprovado. Enviando e-mail...")

# Implementação concreta de um tipo de observador: Voluntário
class Voluntario(Observador):
    def atualizar(self, assunto: Assunto) -> None:
        pass

# Implementação concreta de um tipo de observador: Administrador
class Administrador(Observador):
    def atualizar(self, assunto: Assunto) -> None:
        print("Administrador: Recebeu notificação sobre o registro de evento. Enviando e-mail...")

if __name__ == "__main__":
    # Instanciando o sistema de eventos
    sistema_eventos = SistemaEventos()

    # Instanciando diferentes tipos de observadores
    usuario_geral = UsuarioGeral()
    voluntario = Voluntario()
    administrador = Administrador()

    # Registrando os observadores para um evento
    sistema_eventos.definir_evento_aprovado(True)  # Definindo o evento como aprovado
    sistema_eventos.registrar_para_evento(usuario_geral)
    sistema_eventos.registrar_para_evento(voluntario)  # O voluntário não será notificado
    sistema_eventos.registrar_para_evento(administrador)
