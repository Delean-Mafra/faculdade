# Banco 24h – Modelagem Conceitual

Este repositório apresenta a modelagem conceitual de um sistema de Banco 24 horas, desenvolvida para o exercício proposto em disciplina de modelagem de dados. O objetivo é representar, por meio de entidades, atributos e relacionamentos, os elementos essenciais para o funcionamento de um banco automatizado, com transações disponíveis 24h por dia.

## Escopo

O sistema modelado contempla as operações comuns de um banco, permitindo:
- Saques
- Depósitos
- Transferências
- Consulta de saldo
- Pagamento de contas

Além disso, o sistema gerencia dados de clientes, contas, agências e caixas eletrônicos (ATMs).

---

## Entidades e Atributos

### 1. Cliente
- **CPF** (identificador)
- Nome
- Endereço
- Telefone

### 2. Conta
- **Número da Conta** (identificador)
- Saldo
- Tipo de Conta (corrente, poupança, etc.)

### 3. Agência
- **Código da Agência** (identificador)
- Endereço

### 4. ATM (Caixa Eletrônico)
- **Código do Terminal** (identificador)
- Localização

### 5. Transação
- **ID da Transação** (identificador)
- Tipo de Transação (saque, depósito, transferência, pagamento)
- Data
- Hora
- Valor

---

## Relacionamentos e Cardinalidades

- **Cliente – Conta**:  
  Um cliente pode possuir uma ou mais contas.  
  Uma conta pertence a um único cliente.

- **Cliente – Transação**:  
  Um cliente pode realizar várias transações.

- **Conta – Transação**:  
  Uma transação está associada a uma única conta.  
  Uma conta pode estar envolvida em várias transações.

- **Agência – Conta**:  
  Uma agência possui várias contas.  
  Cada conta está vinculada a uma única agência.

- **ATM – Transação**:  
  Um caixa eletrônico pode registrar várias transações.  
  Uma transação pode ser realizada em um ATM (quando for autoatendimento).

---

## Diagrama Entidade-Relacionamento (ER)

> **Observação:** O diagrama ER pode ser visualizado no arquivo [`banco24h-er.png`](banco24h-er.png) incluído neste repositório.
>
> Exemplo de representação textual:
>
> ```
> Cliente (1) — (N) Conta (1) — (N) Transação
>          \                /
>           \              /
>         Agência      ATM (1) — (N) Transação
> ```

---

## Resumo dos Requisitos Atendidos

- **Definição de entidades e atributos** conforme solicitado.
- **Relacionamentos** e **cardinalidades** explicitados.
- **Diagrama ER** representando o modelo conceitual.

---

## Como Utilizar

1. Consulte o arquivo de diagrama ER para visualizar a estrutura conceitual.
2. Utilize a descrição das entidades e relacionamentos como base para implementação física ou lógica do banco de dados.

---

## Licença

Este projeto é destinado a fins acadêmicos e de estudo.

---
