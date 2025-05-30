
# 📢 Sistema de Notificações com Observer e Factory Method

## ✅ Descrição do Projeto

Este projeto implementa um **sistema de notificações** onde os usuários podem ser notificados por diferentes meios: **Email**, **SMS** ou **Notificação no App**.

A arquitetura do projeto foi construída utilizando dois padrões de projeto clássicos:

* **Observer**: para notificar automaticamente todos os usuários cadastrados sempre que um evento importante ocorre.
* **Factory Method**: para criar instâncias de diferentes tipos de notificadores de forma flexível e desacoplada.

---

## 🎯 Funcionalidades

* Cadastro manual de usuários.
* Escolha do tipo de notificação (Email, SMS ou App).
* Para Email e SMS, coleta de informações adicionais como e-mail ou número de celular com DDD.
* Notificação de todos os usuários cadastrados quando um evento ocorre.
* Flexível para adicionar novos tipos de notificadores sem alterar o núcleo da aplicação.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* Paradigma de **Programação Orientada a Objetos**
* Padrões de projeto: **Observer** e **Factory Method**

---

## 🏗️ Arquitetura e Padrões de Projeto

### ✅ Padrão Observer

* **Subject**: `GerenciadorNotificacoes` → gerencia e notifica todos os usuários.
* **Observer**: `Notificador` → interface que define como notificar.
  **Implementações concretas**:

  * `NotificadorEmail`
  * `NotificadorSMS`
  * `NotificadorApp`

### ✅ Padrão Factory Method

* **Creator**: `FabricaNotificador` → interface para criação de notificadores.
* **Concrete Creators**:

  * `FabricaNotificadorEmail`
  * `FabricaNotificadorSMS`
  * `FabricaNotificadorApp`

Cada fábrica é responsável por criar a instância do notificador conforme o tipo escolhido, coletando os dados necessários.

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seuusuario/sistema-notificacoes.git
```

2. **Acesse o diretório do projeto:**

```bash
cd sistema-notificacoes
```

3. **Execute o script:**

```bash
python notificacoes.py
```

4. **Siga as instruções no terminal:**

   * Informe o nome do usuário.
   * Escolha o tipo de notificação.
   * Forneça e-mail ou telefone se necessário.
   * Ao finalizar, digite "sair" e informe a mensagem do evento para notificar todos.

---

## ✅ Exemplo de Uso

```bash
Digite o nome do usuário (ou 'sair' para finalizar): Ana
Escolha o tipo de notificação:
1 - Email
2 - SMS
3 - App
Digite a opção (1/2/3): 1
Informe o endereço de e-mail: ana@example.com
Usuário Ana cadastrado com sucesso!

Digite o nome do usuário (ou 'sair' para finalizar): sair
Digite a mensagem do evento para notificar todos: Atualização do sistema disponível!

[Email] Para Ana (ana@example.com): Atualização do sistema disponível!
```

---

## 🔧 Como Adicionar um Novo Tipo de Notificação

1. Crie uma nova classe que herde de `Notificador` e implemente o método `notificar`.
2. Crie uma nova `FabricaNotificadorXYZ` que herde de `FabricaNotificador` e implemente o método `criar_notificador`.
3. No `main()`, adicione uma nova opção no menu de escolha de notificadores.

**Exemplo:** adicionar notificação via WhatsApp.

---

## 📄 Estrutura do Projeto

```
sistema-notificacoes/
│
├── notificacoes.py     # Arquivo principal com toda a lógica
├── README.md           # Este arquivo
└── requirements.txt    # (opcional) Dependências, se necessário
```

---

## 💡 Principais Conceitos Envolvidos

* **Encapsulamento**: cada tipo de notificador encapsula sua lógica de notificação.
* **Polimorfismo**: todos os notificadores implementam a mesma interface `Notificador`.
* **Desacoplamento**: o `GerenciadorNotificacoes` não conhece os detalhes dos notificadores.
* **Extensibilidade**: com o Factory Method, é fácil adicionar novos tipos de notificadores.



