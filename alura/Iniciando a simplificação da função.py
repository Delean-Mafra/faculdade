texto2 = "mArIa   doS sAntOs!"
texto3 = "joSé,lUiz   siLvA"
texto4 = "AnA..BeAtrIz   RoDrIgUes"
texto5 = "CARlos  de souZA??"
texto6 = "fernAndO   ALmeiDA!!"
def escreve_texto_corretamente(texto):
    texto_novo = ' '.join(texto.split()).title()
    return texto_novo
import random
salas_de_aula = ["sala 1", "sala 2", "sala 3"]
def aloca_alnos_em_salas(nome_do_alunos, lista_de_salas):
    sala_do_aluno = random.choice(lista_de_salas)
    dict_aluno = {
        "nome": nome_do_alunos,
        "sala": sala_do_aluno
        }
    print(dict_aluno)
nome_final = escreve_texto_corretamente(texto2)
nome_porcesado = aloca_alnos_em_salas(nome_final,salas_de_aula)
print(nome_porcesado)



emails = [
    {
        "assunto": "Bem-vindo à nossa plataforma!",
        "corpo": "Olá, tudo bem? Seja bem-vindo! Estamos felizes em ter você conosco. Qualquer dúvida, é só responder este e-mail."
    },
    {
        "assunto": "Atualização de senha",
        "corpo": "Olá! Recebemos uma solicitação de atualização de senha. Se não foi você, entre em contato com o suporte."
    },
    {
        "assunto": "Confirmação de cadastro",
        "corpo": "Obrigado por se cadastrar. Clique no link para confirmar sua conta e começar a usar nossos serviços."
    },
    {
        "assunto": "Lembrete de pagamento",
        "corpo": "Este é um lembrete amigável de que seu pagamento vence amanhã. Fale conosco se precisar de ajuda."
    },
    {
        "assunto": "Promoção exclusiva",
        "corpo": "Aproveite desconto em todos os planos por tempo limitado. Use o código PROMO20 na finalização."
    },
    {
        "assunto": "Reunião marcada",
        "corpo": "Confirmamos sua reunião para quarta-feira, às 14h. Caso precise remarcar, responda este e-mail."
    },
    {
        "assunto": "Feedback sobre o atendimento",
        "corpo": "Você poderia avaliar nossa última interação? Seu feedback nos ajuda a melhorar continuamente."
    },
    {
        "assunto": "Aviso de manutenção",
        "corpo": "Nosso sistema passará por manutenção no sábado, das 02h às 04h. Alguns serviços podem ficar indisponíveis."
    },
    {
        "assunto": "Recebemos seu pedido",
        "corpo": "Seu pedido foi recebido e está sendo processado. Enviaremos atualizações por e-mail a cada etapa."
    },
    {
        "assunto": "Envio confirmado",
        "corpo": "Seu produto foi enviado! O código de rastreio é XZ123BR. A previsão de entrega é de 3 a 5 dias úteis."
    },
    {
        "assunto": "Convite para webinar",
        "corpo": "Participe do nosso webinar sobre produtividade na próxima terça. Inscreva-se pelo link e garanta sua vaga."
    },
    {
        "assunto": "Atualização de termos",
        "corpo": "Atualizamos nossos Termos de Uso e Política de Privacidade. Confira as mudanças na íntegra em nosso site."
    },
    {
        "assunto": "Recuperação de acesso",
        "corpo": "Para recuperar seu acesso, clique no link abaixo e siga as instruções na página que será aberta."
    },
    {
        "assunto": "Parceria aprovada",
        "corpo": "Sua proposta de parceria foi aprovada! Vamos iniciar os próximos passos ainda esta semana."
    },
    {
        "assunto": "Cupom de boas-vindas",
        "corpo": "Use o cupom BEMVINDO10 para obter desconto na sua primeira compra. Válido por 7 dias."
    },
    {
        "assunto": "Atualização de perfil",
        "corpo": "Identificamos informações faltantes no seu perfil. Acesse sua conta e complete os dados para evitar limitações."
    },
    {
        "assunto": "Confirmação de cancelamento",
        "corpo": "Seu cancelamento foi processado. Lamentamos a sua saída e esperamos te ver de volta em breve."
    },
    {
        "assunto": "Suporte técnico",
        "corpo": "Estamos analisando seu chamado técnico. Assim que houver novidades, retornaremos por este canal."
    },
    {
        "assunto": "Oferta para planos anuais",
        "corpo": "Migre para um plano anual e economize 25%. Essa oferta é válida até o final do mês."
    },
    {
        "assunto": "Agradecimento pela compra",
        "corpo": "Obrigado por comprar com a gente! Sua confiança é muito importante. Qualquer dúvida, estamos à disposição."
    }
]


from google import genai
from google.colab import userdata

# Re-initializing client and chat object as they were not defined in the current session.
# This assumes 'gen_lang_client_0532697187' is the correct secret name.
api_key = userdata.get('gen_lang_client_0532697187')
client = genai.Client(api_key=api_key)

# The model used previously in the conversation was "gemini-2.5-flash".
chat = client.chats.create(model = "gemini-2.5-flash")

resposta = chat.send_message(f"Resuma essa lista de emails em apenas 1 linha: {emails}")
print(resposta.text)

#Resposta da IA via API:
# Esses e-mails são comunicações de uma plataforma/serviço aos usuários, cobrindo desde boas-vindas, gestão de conta e transações até promoções, suporte e avisos.


