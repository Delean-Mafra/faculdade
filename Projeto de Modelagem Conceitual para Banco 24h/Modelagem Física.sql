-- Criação do banco e seleção
CREATE DATABASE banco24h;
\c banco24h

-- Tabela Cliente
CREATE TABLE cliente (
    cpf CHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone CHAR(11)
);

-- Tabela Agência
CREATE TABLE agencia (
    codigo SERIAL PRIMARY KEY,
    endereco VARCHAR(255) NOT NULL
);

-- Tabela Conta
CREATE TABLE conta (
    numero VARCHAR(20) PRIMARY KEY,
    tipo VARCHAR(20) NOT NULL,
    saldo NUMERIC(12,2) NOT NULL,
    cliente_cpf CHAR(11) NOT NULL,
    agencia_codigo INT,
    FOREIGN KEY (cliente_cpf) REFERENCES cliente(cpf),
    FOREIGN KEY (agencia_codigo) REFERENCES agencia(codigo)
);

-- Tabela Caixa Eletrônico (ATM)
CREATE TABLE caixa_eletronico (
    codigo SERIAL PRIMARY KEY,
    localizacao VARCHAR(100),
    agencia_codigo INT NOT NULL,
    FOREIGN KEY (agencia_codigo) REFERENCES agencia(codigo)
);

-- Tabela Transação
CREATE TABLE transacao (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(20) NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    valor NUMERIC(12,2) NOT NULL,
    conta_numero VARCHAR(20),
    caixa_codigo INT,
    FOREIGN KEY (conta_numero) REFERENCES conta(numero),
    FOREIGN KEY (caixa_codigo) REFERENCES caixa_eletronico(codigo)
);
