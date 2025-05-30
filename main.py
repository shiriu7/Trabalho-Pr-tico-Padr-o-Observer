from abc import ABC, abstractmethod
import re

# =========================
# Observer Pattern - Notificadores
# =========================

class Notificador(ABC):
    @abstractmethod
    def notificar(self, usuario_nome: str, mensagem: str):
        pass

# Notificador por Email, armazena o endereço de e-mail
class NotificadorEmail(Notificador):
    def __init__(self, email: str):
        self.email = email

    def notificar(self, usuario_nome: str, mensagem: str):
        print(f"[Email] Para {usuario_nome} ({self.email}): {mensagem}")

# Notificador por SMS, armazena o número com DDD
class NotificadorSMS(Notificador):
    def __init__(self, numero: str):
        self.numero = numero

    def notificar(self, usuario_nome: str, mensagem: str):
        print(f"[SMS] Para {usuario_nome} ({self.numero}): {mensagem}")

# Notificador por App, apenas exibe a mensagem
class NotificadorApp(Notificador):
    def notificar(self, usuario_nome: str, mensagem: str):
        print(f"[App] Notificação na tela para {usuario_nome}: {mensagem}")

# =========================
# Usuário
# =========================

class Usuario:
    def __init__(self, nome: str, notificador: Notificador):
        self.nome = nome
        self.notificador = notificador

    def receber_notificacao(self, mensagem: str):
        self.notificador.notificar(self.nome, mensagem)

# =========================
# Subject: Gerenciador de Notificações
# =========================

class GerenciadorNotificacoes:
    def __init__(self):
        self._usuarios = []

    def registrar_usuario(self, usuario: Usuario):
        self._usuarios.append(usuario)

    def notificar_todos(self, mensagem: str):
        for usuario in self._usuarios:
            usuario.receber_notificacao(mensagem)

# =========================
# Factory Method Pattern
# =========================

class FabricaNotificador(ABC):
    @abstractmethod
    def criar_notificador(self) -> Notificador:
        pass

def validar_email(email: str) -> bool:
    # Regex simples para validar e-mail
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

def validar_ddd(numero: str) -> bool:
    # Aceita formatos como (11)91234-5678, 11912345678, 1191234-5678
    return re.match(r"^\(?\d{2}\)?\d{4,5}-?\d{4}$", numero) is not None

# Fábrica concreta para Email, solicita o e-mail
class FabricaNotificadorEmail(FabricaNotificador):
    def criar_notificador(self) -> Notificador:
        while True:
            email = input("Informe o endereço de e-mail: ")
            if validar_email(email):
                return NotificadorEmail(email)
            else:
                print("E-mail inválido. Tente novamente.")

# Fábrica concreta para SMS, solicita o número de telefone
class FabricaNotificadorSMS(FabricaNotificador):
    def criar_notificador(self) -> Notificador:
        while True:
            numero = input("Informe o número de celular com DDD: ")
            if validar_ddd(numero):
                return NotificadorSMS(numero)
            else:
                print("Número inválido. Tente novamente. Exemplo: 11912345678 ou (11)91234-5678")

# Fábrica concreta para App, não precisa de dados extras
class FabricaNotificadorApp(FabricaNotificador):
    def criar_notificador(self) -> Notificador:
        return NotificadorApp()

# =========================
# Execução principal com inserção manual
# =========================

def main():
    gerenciador = GerenciadorNotificacoes()

    # Cadastro manual de usuários
    while True:
        nome = input("Digite o nome do usuário (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break

        print("Escolha o tipo de notificação:")
        print("1 - Email")
        print("2 - SMS")
        print("3 - App")
        tipo = input("Digite a opção (1/2/3): ")

        # Seleção da fábrica conforme escolha
        if tipo == '1':
            fabrica = FabricaNotificadorEmail()
        elif tipo == '2':
            fabrica = FabricaNotificadorSMS()
        elif tipo == '3':
            fabrica = FabricaNotificadorApp()
        else:
            print("Tipo inválido, tente novamente.\n")
            continue

        # Criando o notificador com dados conforme o tipo
        notificador = fabrica.criar_notificador()

        # Criando e registrando o usuário
        usuario = Usuario(nome, notificador)
        gerenciador.registrar_usuario(usuario)

        print(f"Usuário {nome} cadastrado com sucesso!\n")

    # Notificação de todos os usuários
    evento = input("Digite a mensagem do evento para notificar todos: ")
    gerenciador.notificar_todos(evento)

# Ponto de entrada
if __name__ == "__main__":
    main()
