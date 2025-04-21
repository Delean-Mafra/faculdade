// API de Cálculo de Seguro (Node.js/Express)
app.post('/simular', (req, res) => {
  const { idade, valorVeiculo, historico } = req.body;
  const taxaBase = 0.05; // 5% do valor do veículo
  const descontoAposentado = 0.2; // 20% de desconto
  let valorFinal = valorVeiculo * taxaBase;

  if (idade >= 60) valorFinal *= (1 - descontoAposentado);
  
  res.json({ valorSeguro: valorFinal.toFixed(2) });
});
