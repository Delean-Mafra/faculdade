describe('Simulador', () => {
  it('Calcula desconto para aposentados', () => {
    cy.request('POST', '/simular', { idade: 65, valorVeiculo: 50000 })
      .then((response) => {
        expect(response.body.valorSeguro).to.equal('2000.00');
      });
  });
});
