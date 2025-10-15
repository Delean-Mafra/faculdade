-- ============== VALIDAÇÃO DE DADOS - QUERIES SQL ==============

-- 1. TOTAL DE VENDAS POR DIA
-- Agrupa e soma o total de vendas por data
SELECT 
    DATE(o.order_date) AS data,
    COUNT(DISTINCT o.order_id) AS numero_pedidos,
    SUM(oi.total_price) AS total_vendas
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY DATE(o.order_date)
ORDER BY data DESC
LIMIT 30;

-- 2. MAIORES VENDAS DO DIA
-- Identifica as 10 maiores transações do dia
SELECT 
    o.order_id,
    DATE(o.order_date) AS data,
    c.customer_name,
    SUM(oi.total_price) AS valor_venda
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE DATE(o.order_date) = CURRENT_DATE
GROUP BY o.order_id, DATE(o.order_date), c.customer_name
ORDER BY valor_venda DESC
LIMIT 10;

-- 3. PRODUTOS MAIS VENDIDOS
-- Faz joins entre orders, order_items e products
-- Conta quantidade de vendas por produto
SELECT 
    p.product_id,
    p.product_name,
    COUNT(oi.order_item_id) AS quantidade_vendida,
    SUM(oi.total_price) AS receita_total,
    AVG(p.price) AS preco_medio
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.order_id
WHERE DATE(o.order_date) = CURRENT_DATE
GROUP BY p.product_id, p.product_name
ORDER BY quantidade_vendida DESC
LIMIT 20;

-- 4. PRODUTOS COM ESTOQUE BAIXO
-- Identifica produtos com estoque menor que 10
SELECT 
    product_id,
    product_name,
    stock_quantity,
    price,
    (stock_quantity * price) AS valor_estoque
FROM products
WHERE stock_quantity < 10
ORDER BY stock_quantity ASC;

-- 5. VALIDAÇÃO DE INTEGRIDADE - CONTAGEM DE REGISTROS
-- Verifica contagem total de registros em cada tabela
SELECT 
    'customers' AS tabela,
    COUNT(*) AS total_registros
FROM customers
UNION ALL
SELECT 
    'products' AS tabela,
    COUNT(*) AS total_registros
FROM products
UNION ALL
SELECT 
    'orders' AS tabela,
    COUNT(*) AS total_registros
FROM orders
UNION ALL
SELECT 
    'order_items' AS tabela,
    COUNT(*) AS total_registros
FROM order_items;

-- 6. VALIDAÇÃO - PEDIDOS SEM ITENS (POSSÍVEIS ORFÃOS)
SELECT 
    o.order_id,
    o.order_date,
    COUNT(oi.order_item_id) AS numero_itens
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, o.order_date
HAVING COUNT(oi.order_item_id) = 0;

-- 7. VALIDAÇÃO - ITENS SEM PEDIDO CORRESPONDENTE
SELECT 
    oi.order_item_id,
    oi.order_id,
    COUNT(*) AS ocorrencias
FROM order_items oi
LEFT JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL
GROUP BY oi.order_item_id, oi.order_id;

-- 8. VALIDAÇÃO - VALORES NEGATIVOS
SELECT 
    'order_items' AS tabela,
    COUNT(*) AS valores_negativos
FROM order_items
WHERE total_price < 0 OR quantity < 0
UNION ALL
SELECT 
    'products' AS tabela,
    COUNT(*) AS valores_negativos
FROM products
WHERE price < 0 OR stock_quantity < 0;

-- 9. RECEITA TOTAL DO DIA (PARA AUDITORIA)
SELECT 
    DATE(o.order_date) AS data_auditoria,
    COUNT(DISTINCT o.order_id) AS numero_pedidos,
    COUNT(DISTINCT oi.order_item_id) AS numero_itens,
    SUM(oi.quantity) AS quantidade_total_itens,
    SUM(oi.total_price) AS receita_total
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY DATE(o.order_date)
ORDER BY data_auditoria DESC;