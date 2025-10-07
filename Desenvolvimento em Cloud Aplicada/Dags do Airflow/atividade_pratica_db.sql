-- arquivo: criar_banco_e_dados.sql
-- Script SQL para criar banco, usuário, tabelas e inserir dados fictícios.
-- Execute os comandos de criação do banco como superusuário (ex.: usuário "postgres").
-- Após criar o banco, conecte-se ao banco atividade_pratica_db para executar os comandos de criação de tabelas e inserts.

-- 1) Criar usuário e banco (executar no banco "postgres" ou como superusuário)
CREATE USER atividade_user WITH PASSWORD 'SenhaForteExemplo123';
CREATE DATABASE atividade_pratica_db OWNER atividade_user;

-- 2) Conectar ao banco criado (no psql: \c atividade_pratica_db) e então executar:
-- (A partir daqui, rode os comandos enquanto conectado ao banco atividade_pratica_db)

-- 3) Criar esquema/tabela
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    criado_em TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4) Inserir registros fictícios
INSERT INTO usuarios (nome, email) VALUES
('Ana Silva', 'ana.silva@example.com'),
('Bruno Souza', 'bruno.souza@example.com'),
('Carlos Pereira', 'carlos.pereira@example.com'),
('Daniela Costa', 'daniela.costa@example.com'),
('Eduardo Lima', 'eduardo.lima@example.com'),
('Fernanda Alves', 'fernanda.alves@example.com');
