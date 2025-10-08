-- SQL:


-- arquivo: criar_banco_de_dados.sql
-- Script SQL para criar banco, usuário, tabelas e inserir dados fictícios.

-- Criar usuário e banco postgres
CREATE USER atividade_user WITH PASSWORD 'SenhaForteExemplo123';
CREATE DATABASE atividade_pratica_db OWNER atividade_user;




-- Criar esquema/tabela
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    criado_em TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


-- Inserir registros fictícios
INSERT INTO usuarios (nome, email) VALUES
('Ana Silva', 'ana.silva@example.com'),
('Bruno Souza', 'bruno.souza@example.com'),
('Carlos Pereira', 'carlos.pereira@example.com'),
('Daniela Costa', 'daniela.costa@example.com'),
('Eduardo Lima', 'eduardo.lima@example.com'),
('Fernanda Alves', 'fernanda.alves@example.com');
