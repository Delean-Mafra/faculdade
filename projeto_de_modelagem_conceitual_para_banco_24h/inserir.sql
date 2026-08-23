-- Inserindo dados de exemplo
INSERT INTO agencia (endereco) VALUES ('Av. Central, 123');
INSERT INTO cliente (cpf, nome, telefone) VALUES ('12345678901', 'João Silva', '11987654321');
INSERT INTO conta (numero, tipo, saldo, cliente_cpf, agencia_codigo) 
    VALUES ('0001', 'Corrente', 1000.00, '12345678901', 1);
INSERT INTO caixa_eletronico (localizacao, agencia_codigo) VALUES ('Shopping Center', 1);
INSERT INTO transacao (tipo, data, hora, valor, conta_numero, caixa_codigo) 
    VALUES ('Saque', '2025-07-21', '14:30:00', 200.00, '0001', 1);
