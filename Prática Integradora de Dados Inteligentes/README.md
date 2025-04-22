---
marp: true
theme: uncover # Você pode experimentar outros temas como 'gaia' ou 'default'
size: 16:9
paginate: true
header: "Relatório Sprint 1 - Sistema de Seguro de Veículos"
footer: "Delean Plince Mafra - 21/04/2025"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->
# Relatório de Planejamento e Execução da Primeira Sprint

**Projeto:** Sistema de Seguro de Veículos para Aposentados
**Responsável:** Delean Plince Mafra
**Data:** 21/04/2025

---

# 1. Contexto do Projeto

Fui contratado como Product Owner (PO) para liderar o desenvolvimento de um novo sistema de seguros de veículos voltado para aposentados. A seguradora identificou uma demanda crescente nesse público e precisa de funcionalidades como:

*   Simulação de apólices (cálculo de preços personalizados).
*   Criação de apólices (cadastro digital com documentos simplificados).
*   Gerenciamento de apólices (renovação, cancelamento, histórico).

O projeto será desenvolvido usando Scrum, com sprints de 2 semanas.

---

# 2. Product Backlog (Priorizado)

Criei o backlog com as principais funcionalidades, classificadas por valor para o negócio e complexidade:

➡️ **Em anexo:** "Product Backlog.xlsx"

*(Priorização feita em reunião com stakeholders, considerando ROI e prazo.)*

---

# 3. Planejamento da Sprint 1

**Objetivo:** Entregar o Simulador de Apólice e o Cadastro Básico de Cliente.

**Tarefas da Sprint (Sprint Backlog):**

➡️ **Em anexo:** "tarefa.xlsx"

---

# 4. Execução da Sprint

## Dia 1-3:
*   Reunião de alinhamento com a equipe para definir padrões de código.
*   Desenvolvimento da API de cálculo (exemplo em Node.js):

```javascript
// API de Cálculo de Seguro (Node.js/Express)
app.post('/simular', (req, res) => {
  const { idade, valorVeiculo, historico } = req.body;
  const taxaBase = 0.05; // 5% do valor do veículo
  const descontoAposentado = 0.2; // 20% de desconto
  let valorFinal = valorVeiculo * taxaBase;

  if (idade >= 60) valorFinal *= (1 - descontoAposentado);
  
  res.json({ valorSeguro: valorFinal.toFixed(2) });
});
```

---

# 4. Execução da Sprint (Continuação)

## Dia 4-6:
*   Front-end do simulador (React):

```jsx
function Simulador() {
  const [valor, setValor] = useState(0);
  
  const calcular = async () => {
    // Exemplo de dados, substitua pela lógica real de coleta do formulário
    const dados = { idade: 65, valorVeiculo: 50000, historico: 'bom' }; 
    const response = await fetch('/simular', { 
        method: 'POST', 
        headers: { 'Content-Type': 'application/json' }, // Importante para o backend Express entender o JSON
        body: JSON.stringify(dados) 
    });
    const resultado = await response.json();
    setValor(resultado.valorSeguro);
  };

  return (
    <div>
      {/* Adicione campos de input para idade, valorVeiculo, etc. aqui */}
      <button onClick={calcular}>Simular</button>
      <p>Valor do seguro: R$ {valor}</p>
    </div>
  );
}
```

---

# 4. Execução da Sprint (Continuação)

## Dia 7-10:
*   Testes automatizados (exemplo com Cypress):

```javascript
describe('Simulador', () => {
  it('Calcula desconto para aposentados', () => {
    cy.request('POST', '/simular', { idade: 65, valorVeiculo: 50000 })
      .then((response) => {
        expect(response.body.valorSeguro).to.equal('2000.00');
      });
  });
});
```

---

# 5. Entrega da Sprint (Demo)

## Resultados alcançados:
*   ✅ Simulador funcional com desconto para aposentados.
*   ✅ Formulário de cadastro básico (validação de CPF e campos obrigatórios).
*   ✅ Testes automatizados cobrindo 80% do código.

## Próximos passos (Sprint 2):
*   Desenvolver o Dashboard de Apólices.
*   Melhorar acessibilidade (leitor de tela para idosos).

---

# 6. Materiais de Apoio

*   Repositório no GitHub: `[link_do_seu_repo_aqui]` (Ex: `https://github.com/seu_usuario/projeto-seguro`)
*   Documentação da API (Swagger): `[link_do_swagger_aqui]`

---

# 7. Lições Aprendidas e o que deu certo

## O que deu certo: 👍
*   Equipe alinhada desde o primeiro dia.
*   Feedback rápido dos stakeholders após a demo.

## Pontos de Melhoria: 🛠️
*   Automatizar mais testes de integração.
*   Incluir UX Designer na próxima sprint para melhorar usabilidade.

```

**Observações:**
1.  **Tema:** Usei o tema `uncover` que é limpo e bom para relatórios. Você pode mudar para `gaia` ou `default` ou outros temas que você tenha instalado.
2.  **Anexos:** O Marp não incorpora arquivos Excel diretamente. A menção "Em anexo" foi mantida, mas você precisará distribuir esses arquivos separadamente ou criar slides específicos para resumir o conteúdo deles, se necessário.
3.  **Código React:** Adicionei um `headers: { 'Content-Type': 'application/json' }` no `fetch` do React, pois é comum ser necessário para APIs Express que esperam JSON no corpo da requisição. Também adicionei um comentário sobre `dados` serem um exemplo.
4.  **Links:** Nos "Materiais de Apoio", coloquei placeholders `[link_do_seu_repo_aqui]` e `[link_do_swagger_aqui]`. Substitua-os pelos links reais.
5.  **Visualização:** Para ver isso como uma apresentação, você precisará de uma ferramenta que interprete Marp, como:
    *   A extensão "Marp for VS Code" no Visual Studio Code.
    *   O Marp CLI (ferramenta de linha de comando).

Espero que isso ajude!
