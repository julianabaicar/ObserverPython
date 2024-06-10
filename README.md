# ObserverPython
Design Pattern

# Implementação do Padrão Observer em Python

Este repositório contém uma implementação simples, mas abrangente, do padrão de projeto Observer em Python. O padrão Observer é um padrão de design comportamental que permite que um objeto (referido como sujeito) notifique outros objetos (observadores) sobre mudanças em seu estado sem estar fortemente acoplado a eles. Este exemplo demonstra como criar um sistema onde vários observadores podem se inscrever e receber atualizações de um único sujeito.

Funcionalidades:
- Interface Subject: Define métodos para registrar, remover e notificar observadores.
- Interface Observer: Define o método para receber atualizações do sujeito.
- Classe ConcreteSubject: Implementa a interface Subject e gerencia o estado e a lista de observadores.
- Classe ConcreteObserver: Implementa a interface Observer e reage às atualizações do sujeito.
- Classe Main: Contém um cenário de teste detalhado para demonstrar a funcionalidade do padrão.
