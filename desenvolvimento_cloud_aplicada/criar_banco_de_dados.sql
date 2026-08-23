
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'atividade_user') THEN
        CREATE ROLE atividade_user LOGIN PASSWORD 'SenhaForteExemplo123';
    END IF;
END
$$;

SELECT 'CREATE DATABASE atividade_pratica_db OWNER atividade_user'
WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'atividade_pratica_db')\gexec

\c atividade_pratica_db atividade_user

ALTER SCHEMA public OWNER TO atividade_user;
GRANT ALL ON SCHEMA public TO atividade_user;
GRANT ALL PRIVILEGES ON DATABASE atividade_pratica_db TO atividade_user;

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    criado_em TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

WITH seed(nome, email) AS (
    VALUES
        ('Ana Silva', 'ana.silva@example.com'),
        ('Bruno Souza', 'bruno.souza@example.com'),
        ('Carlos Pereira', 'carlos.pereira@example.com'),
        ('Daniela Costa', 'daniela.costa@example.com'),
        ('Eduardo Lima', 'eduardo.lima@example.com'),
        ('Fernanda Alves', 'fernanda.alves@example.com')
)
INSERT INTO usuarios (nome, email)
SELECT s.nome, s.email
FROM seed s
WHERE NOT EXISTS (SELECT 1 FROM usuarios);
