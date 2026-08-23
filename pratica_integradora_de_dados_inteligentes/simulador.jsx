function Simulador() {
  const [valor, setValor] = useState(0);
  
  const calcular = async () => {
    const response = await fetch('/simular', { method: 'POST', body: JSON.stringify(dados) });
    const resultado = await response.json();
    setValor(resultado.valorSeguro);
  };

  return (
    <div>
      <button onClick={calcular}>Simular</button>
      <p>Valor do seguro: R$ {valor}</p>
    </div>
  );
}
