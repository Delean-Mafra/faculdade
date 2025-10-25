# Política de Segurança (SECURITY.md)

Última atualização: 2025-10-25

Este documento descreve como reportar vulnerabilidades de segurança e quais são os procedimentos adotados para tratar problemas de segurança relacionados a este repositório.

1. Objetivo
- Receber e tratar relatórios de segurança de forma responsável e coordenada.
- Minimizar riscos para usuários e terceiros enquanto trabalhamos em correções.
- Coordenar divulgação responsável quando aplicável.

2. Como reportar uma vulnerabilidade (recomendado)
- Preferimos que relatórios confidenciais sejam enviados por meio do recurso "Security Advisories" do GitHub:
  - Vá em: Repositório > Security > Advisories > New security advisory.
  - Esse fluxo permite manter a comunicação privada e coordenar correções e divulgação.
- Se você não puder usar Security Advisories, abra uma issue com o prefixo "SECURITY:" no título apenas como último recurso. NÃO inclua informações sensíveis ou exploit code em uma issue pública.
  - Ex.: "SECURITY: vulnerabilidade de injeção em script X" (sem PoC público).

3. Se precisar enviar dados sensíveis
- Não publique PoC, senhas, chaves privadas, prints contendo dados pessoais, ou qualquer informação sensível em issues públicas.
- Após a abertura da issue pública (se necessário), o mantenedor poderá oferecer um canal privado (por exemplo, e-mail ou outro meio) para troca segura de informações. Forneça apenas quando o canal privado for confirmado.
- O método preferido é: Security Advisory do GitHub, que já é privado por padrão.

4. Informação a incluir no relatório
Para agilizar a análise, inclua quando possível:
- Resumo curto do problema e componente afetado.
- Passos para reproduzir (passo a passo).
- Ambiente/versões (ex.: Python 3.11, NumPy 1.25).
- Impacto esperado (ex.: execução remota de código, vazamento de informação).
- Proof-of-concept (PoC) ou teste demonstrativo — se for confidencial, envie por canal privado.
- Logs, mensagens de erro e trechos de código relevantes.
- Contato (GitHub username). Se desejar anonimato, indique e discutiremos opções.
- Preferência sobre coordenação de divulgação (por exemplo, prazo para correção antes de divulgação pública).

5. Processo de resposta e prazos
- Agradecemos o reporte. O mantenedor tentará:
  - Acknowledgement inicial em até 3 dias úteis.
  - Fornecer um plano inicial ou mitigação em até 14 dias úteis, dependendo da gravidade e da complexidade.
  - Trabalhar em correção ou mitigação numa janela razoável — geralmente esperamos publicar correções ou mitigação em até 90 dias em casos não críticos; para casos críticos, priorizamos ações imediatas.
- Esses prazos são metas e podem variar conforme disponibilidade, complexidade e necessidade de coordenação externa.

6. Divulgação coordenada e CVE
- Nosso objetivo é coordenar a divulgação com os relatantes. Quando apropriado, vamos:
  - Corrigir a vulnerabilidade em primeiro lugar, em seguida divulgar com as informações necessárias.
  - Trabalhar com mantenedores de dependências quando a vulnerabilidade estiver em bibliotecas de terceiros.
  - Solicitar atribuição de CVE quando aplicável (podemos pedir ajuda do relatante para isso).

7. Política sobre recompensas (bug bounty)
- Atualmente não há programa de recompensa pago para este repositório.
- Reconhecimento público ou privado pode ser oferecido ao divulgador que cooperar na resolução, caso o relatante concorde com divulgação.

8. Escopo
- Inclui código neste repositório e exemplos fornecidos aqui.
- Exclui serviços externos não hospedados neste repositório (a não ser que a vulnerabilidade esteja diretamente ligada ao conteúdo deste repo).

9. Comportamento esperado do relatante
- Forneça informações suficientes para validar o problema.
- Não explore a vulnerabilidade além do necessário para demonstrar e validar o relatório.
- Evite divulgar publicamente até que exista uma mitigação/correção ou acordo de divulgação.

10. Comunicações e transparência
- Após confirmação do problema, manteremos o comunicante atualizado sobre progresso e decisões relevantes.
- Manteremos registro das ações tomadas (commits, PRs, release notes).

11. Contato alternativo
- Se você não puder (ou não quiser) usar Security Advisories e preferir contato por e-mail, indique isso em uma issue pública segura e o mantenedor fornecerá um canal privado adequado. Não envie dados sensíveis antes de confirmar o canal privado.

Agradecemos a preocupação com a segurança e a ajuda para manter este repositório seguro para todos.
