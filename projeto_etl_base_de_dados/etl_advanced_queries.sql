-- ============================================================
-- QUERIES SQL AVANÇADAS - PROJETO ETL VENDAS
-- ============================================================

-- ============== 1. DASHBOARD DE VENDAS DIÁRIAS ==============

-- Resumo completo do dia
SELECT 
    DATE(o.order_date) AS data_venda,
    COUNT(DISTINCT o.order_id) AS numero_pedidos,
    COUNT(DISTINCT o.customer_id) AS numero_clientes,
    COUNT(oi.order_item_id) AS total_itens_vendidos,
    SUM(oi.quantity) AS quantidade_total,
    SUM(oi.total_price) AS receita_total,
    ROUND(AVG(o.total_amount), 2) AS ticket_medio,
    MIN(o.total_amount) AS menor_compra,
    MAX(o.total_amount) AS maior_compra
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY DATE(o.order_date)
ORDER BY data_venda DESC;

-- ============== 2. ANÁLISE DE CLIENTES ==============

-- Clientes com maior volume de vendas
SELECT 
    c.customer_id,
    c.customer_name,
    c.city,
    COUNT(DISTINCT o.order_id) AS numero_pedidos,
    SUM(o.total_amount) AS valor_total_gasto,
    ROUND(AVG(o.total_amount), 2) AS ticket_medio,
    MAX(o.order_date) AS ultima_compra,
    ROUND((SUM(o.total_amount) / (SELECT SUM(total_amount) FROM orders) * 100), 2) AS percentual_vendas
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.city
HAVING COUNT(DISTINCT o.order_id) > 0
ORDER BY valor_total_gasto DESC
LIMIT 20;

-- Clientes inativos (sem compras nos últimos 30 dias)
SELECT 
    c.customer_id,
    c.customer_name,
    c.email,
    MAX(o.order_date) AS ultima_compra,
    CURRENT_DATE - MAX(o.order_date)::date AS dias_sem_comprar
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date IS NOT NULL
GROUP BY c.customer_id, c.customer_name, c.email
HAVING MAX(o.order_date) < CURRENT_DATE - INTERVAL '30 days'
ORDER BY ultima_compra ASC;

-- ============== 3. ANÁLISE DE PRODUTOS ==============

-- Produtos com melhor performance
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    p.stock_quantity,
    COUNT(DISTINCT oi.order_id) AS numero_vendas,
    SUM(oi.quantity) AS quantidade_vendida,
    SUM(oi.total_price) AS receita_produto,
    ROUND(AVG(oi.quantity), 2) AS media_quantidade_por_venda,
    ROUND((SUM(oi.total_price) / (SELECT SUM(total_price) FROM order_items) * 100), 2) AS percentual_receita
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category, p.price, p.stock_quantity
HAVING SUM(oi.quantity) > 0
ORDER BY receita_produto DESC;

-- Análise de estoque vs vendas
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    p.stock_quantity,
    COALESCE(SUM(oi.quantity), 0) AS quantidade_vendida_30dias,
    CASE 
        WHEN p.stock_quantity < 10 THEN 'CRÍTICO'
        WHEN p.stock_quantity < 25 THEN 'BAIXO'
        WHEN p.stock_quantity < 50 THEN 'MÉDIO'
        ELSE 'ADEQUADO'
    END AS status_estoque,
    CASE 
        WHEN COALESCE(SUM(oi.quantity), 0) > 10 THEN 'ALTA ROTATIVIDADE'
        WHEN COALESCE(SUM(oi.quantity), 0) > 5 THEN 'MÉDIA ROTATIVIDADE'
        ELSE 'BAIXA ROTATIVIDADE'
    END AS rotatividade
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.order_id
    AND o.order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY p.product_id, p.product_name, p.category, p.price, p.stock_quantity
ORDER BY p.stock_quantity ASC;

-- Produtos que podem estar sem saída
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    p.stock_quantity,
    p.created_at,
    COUNT(oi.order_item_id) AS total_vendido_ever,
    MAX(o.order_date) AS ultima_venda,
    CURRENT_DATE - MAX(o.order_date)::date AS dias_sem_vender
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.order_id
GROUP BY p.product_id, p.product_name, p.category, p.price, 
         p.stock_quantity, p.created_at
HAVING COUNT(oi.order_item_id) = 0 
   OR MAX(o.order_date) < CURRENT_DATE - INTERVAL '60 days'
ORDER BY p.stock_quantity DESC;

-- ============== 4. ANÁLISE TEMPORAL ==============

-- Vendas por hora do dia
SELECT 
    DATE(o.order_date) AS data,
    EXTRACT(HOUR FROM o.order_date) AS hora,
    COUNT(*) AS numero_pedidos,
    SUM(oi.total_price) AS receita,
    ROUND(AVG(o.total_amount), 2) AS ticket_medio
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY DATE(o.order_date), EXTRACT(HOUR FROM o.order_date)
ORDER BY data DESC, hora;

-- Tendência de vendas (últimos 30 dias)
SELECT 
    DATE(o.order_date) AS data,
    DAYNAME(o.order_date) AS dia_semana,
    COUNT(DISTINCT o.order_id) AS numero_pedidos,
    SUM(oi.total_price) AS receita_dia,
    AVG(SUM(oi.total_price)) OVER (
        ORDER BY DATE(o.order_date) 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS media_movel_7dias
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY DATE(o.order_date)
ORDER BY data DESC;

-- ============== 5. ANÁLISE DE CATEGORIAS ==============

-- Performance por categoria de produto
SELECT 
    p.category,
    COUNT(DISTINCT oi.order_id) AS numero_vendas,
    SUM(oi.quantity) AS quantidade_total,
    SUM(oi.total_price) AS receita_categoria,
    ROUND(AVG(p.price), 2) AS preco_medio,
    COUNT(DISTINCT p.product_id) AS numero_produtos,
    ROUND((SUM(oi.total_price) / (SELECT SUM(total_price) FROM order_items) * 100), 2) AS percentual_receita_total
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
HAVING SUM(oi.total_price) > 0
ORDER BY receita_categoria DESC;

-- ============== 6. ANÁLISE DE PEDIDOS ANORMAIS ==============

-- Pedidos com valores extremos (possíveis anomalias)
SELECT 
    o.order_id,
    o.customer_id,
    c.customer_name,
    o.order_date,
    o.total_amount,
    COUNT(oi.order_item_id) AS numero_itens,
    ROUND((o.total_amount / NULLIF(COUNT(oi.order_item_id), 0)), 2) AS valor_medio_item
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, o.customer_id, c.customer_name, o.order_date, o.total_amount
HAVING o.total_amount > (SELECT PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total_amount) FROM orders)
   OR o.total_amount < (SELECT PERCENTILE_CONT(0.05) WITHIN GROUP (ORDER BY total_amount) FROM orders WHERE total_amount > 0)
ORDER BY o.total_amount DESC;

-- ============== 7. SEGMENTAÇÃO DE CLIENTES (RFM) ==============

-- Análise RFM (Recência, Frequência, Monetário)
WITH rfm AS (
    SELECT 
        c.customer_id,
        c.customer_name,
        CURRENT_DATE - MAX(o.order_date)::date AS recencia,
        COUNT(DISTINCT o.order_id) AS frequencia,
        SUM(o.total_amount) AS monetario
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT 
    customer_id,
    customer_name,
    recencia,
    frequencia,
    monetario,
    CASE 
        WHEN recencia <= 7 AND frequencia >= 3 AND monetario >= 1000 THEN 'CAMPEÃO'
        WHEN recencia <= 30 AND frequencia >= 2 THEN 'CLIENTE LEAL'
        WHEN recencia > 90 AND frequencia >= 1 THEN 'CLIENTE EM RISCO'
        WHEN recencia > 180 THEN 'CLIENTE DORMINHOCO'
        ELSE 'CLIENTE NOVO'
    END AS segmento
FROM rfm
ORDER BY monetario DESC;

-- ============== 8. ANÁLISE DE CUSTOS E MARGENS ==============

-- Simulação: Margem de lucro por categoria
-- Assumindo: custo = 60% do preço de venda
SELECT 
    p.category,
    SUM(oi.total_price) AS receita_bruta,
    ROUND(SUM(oi.total_price) * 0.40, 2) AS lucro_estimado,
    ROUND(ROUND(SUM(oi.total_price) * 0.40, 2) / SUM(oi.total_price) * 100, 2) AS margem_percentual,
    SUM(oi.quantity) AS quantidade_vendida
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY lucro_estimado DESC;

-- ============== 9. RELATÓRIO EXECUTIVO ==============

-- KPIs principais
SELECT 
    'RECEITA TOTAL' AS kpi,
    ROUND(SUM(total_amount)::NUMERIC, 2)::TEXT AS valor
FROM orders
UNION ALL
SELECT 'Pedidos Completados', COUNT(*) FROM orders WHERE status = 'completed'
UNION ALL
SELECT 'Total de Itens Vendidos', COUNT(*) FROM order_items
UNION ALL
SELECT 'Itens com Quantidade > 0', COUNT(*) FROM order_items WHERE quantity > 0
UNION ALL
SELECT 'Data Última Atualização', MAX(created_at)::TEXT FROM orders;NÚMERO DE PEDIDOS', COUNT(*)::TEXT FROM orders
UNION ALL
SELECT 'NÚMERO DE CLIENTES', COUNT(DISTINCT customer_id)::TEXT FROM orders
UNION ALL
SELECT 'TICKET MÉDIO', ROUND(AVG(total_amount)::NUMERIC, 2)::TEXT FROM orders
UNION ALL
SELECT 'PRODUTOS VENDIDOS', COUNT(DISTINCT product_id)::TEXT FROM order_items
UNION ALL
SELECT 'CATEGORIAS ATIVAS', COUNT(DISTINCT category)::TEXT FROM products;

-- ============== 10. AUDITORIA E QUALIDADE ==============

-- Relatório de qualidade de dados
SELECT 
    'Total de Clientes' AS item, COUNT(*)::TEXT AS valor FROM customers
UNION ALL
SELECT 'Clientes com Email', COUNT(*) FROM customers WHERE email IS NOT NULL
UNION ALL
SELECT 'Total de Produtos', COUNT(*) FROM products
UNION ALL
SELECT 'Produtos com Preço', COUNT(*) FROM products WHERE price > 0
UNION ALL
SELECT 'Total de Pedidos', COUNT(*) FROM orders
UNION ALL
SELECT '