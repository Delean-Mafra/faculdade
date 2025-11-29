from openai import OpenAI 
import json
import os
from google.colab import userdata

os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY')


client_openai = OpenAI(

    base_url="https://api.groq.com/openai/v1",
    api_key="GROQ_API_KEY"
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": """Voce recebera uma linha de texto que e uma resenha de um aplicativo em um marktplac online.
Eu quero que você analise essa resenha, e me retorne um JSON com as seguintes chaves:
- 'usuario': o nome do usuário que fez a resenha
- 'resenha_original': a resenha no idioma original que você recebeu
- 'resenha_pt': a resenha traduzida para o português e deve estar sempre na ligua portuguêsa
- 'avaliacao': uma avalicao se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções)

Exemplo de entrada:
'879485937$Pedro Silva$This is a positive review for the app'
Exemplo de saída:
{
    "usuario": "Pedro Silva",
    "resenha_original": "This is a positive review for the app",
    "resenha_pt": "Esta é uma resenha positiva para o aplicativo",
    "avaliacao": "Positiva"
}

Regra importante: Retorne APENAS o JSON solicitado, sem nenhum texto adicional fora do JSON.
"""
            },
            {
                "role": "user",
                "content": f"Resenha: {linha}"
            }
        ],
        temperature=0.7
    )
    print(resposta_do_llm.choices[0].message.content)
    return resposta_do_llm.choices[0].message.content


linhas_de_resenhas = []

with open("alura.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linhas_de_resenhas.append(linha.strip())


# Etapa 2
lista_de_resenhas_json = []


for resenha in linhas_de_resenhas:
    resenha_json = recebe_linha_e_retorna_json(resenha)
    resenha_dict = json.loads(resenha_json)
    lista_de_resenhas_json.append(resenha_dict)

    print(resenha_dict)



## Retorno do codigo:

# {
#     "usuario": "Safoan Riyad",
#     "resenha_original": "J'aimais bien ChatGPT. Mais la derniÃ¨re mise Ã  jour a tout gÃ¢chÃ©. Elle a tout oubliÃ©.",
#     "resenha_pt": "Eu gostava muito do ChatGPT. Mas a última atualização arruinou tudo. Ela esqueceu tudo.",
#     "avaliacao": "Negativa"
# }
# {'usuario': 'Safoan Riyad', 'resenha_original': "J'aimais bien ChatGPT. Mais la derniÃ¨re mise Ã  jour a tout gÃ¢chÃ©. Elle a tout oubliÃ©.", 'resenha_pt': 'Eu gostava muito do ChatGPT. Mas a última atualização arruinou tudo. Ela esqueceu tudo.', 'avaliacao': 'Negativa'}
# {
#     "usuario": "Habimana Therese",
#     "resenha_original": "This app is very important but sometimes it gives lies",
#     "resenha_pt": "Este aplicativo é muito importante, mas às vezes dá mentiras",
#     "avaliacao": "Neutra"
# }
# {'usuario': 'Habimana Therese', 'resenha_original': 'This app is very important but sometimes it gives lies', 'resenha_pt': 'Este aplicativo é muito importante, mas às vezes dá mentiras', 'avaliacao': 'Neutra'}
# {
#     "usuario": "Shahidatun jannat",
#     "resenha_original": "Wonderful app..i just aastonished.. love this app..",
#     "resenha_pt": "Aplicativo maravilhoso... eu fiquei maravilhado... amo este aplicativo...",
#     "avaliacao": "Positiva"
# }
# {'usuario': 'Shahidatun jannat', 'resenha_original': 'Wonderful app..i just aastonished.. love this app..', 'resenha_pt': 'Aplicativo maravilhoso... eu fiquei maravilhado... amo este aplicativo...', 'avaliacao': 'Positiva'}
# {
#     "usuario": "Rayyan R",
#     "resenha_original": "Anytime i try to get the app to work. It tells me \"an error has occured\" can this be fixed",
#     "resenha_pt": "Sempre que tento fazer o app funcionar, ele me diz \"um erro ocorreu\". Isso pode ser consertado?",
#     "avaliacao": "Negativa"
# }
# {'usuario': 'Rayyan R', 'resenha_original': 'Anytime i try to get the app to work. It tells me "an error has occured" can this be fixed', 'resenha_pt': 'Sempre que tento fazer o app funcionar, ele me diz "um erro ocorreu". Isso pode ser consertado?', 'avaliacao': 'Negativa'}
# {"usuario":"Nkanyi Cele","resenha_original":"Acabo de instalar la aplicación desde Google Play Store, pero lamentablemente no se abre. Se queda dando vueltas.","resenha_pt":"Acabei de instalar o aplicativo na Google Play Store, mas infelizmente não abre. Fica dando voltas.","avaliacao":"Negativa"}    
# {'usuario': 'Nkanyi Cele', 'resenha_original': 'Acabo de instalar la aplicación desde Google Play Store, pero lamentablemente no se abre. Se queda dando vueltas.', 'resenha_pt': 'Acabei de instalar o aplicativo na Google Play Store, mas infelizmente não abre. Fica dando voltas.', 'avaliacao': 'Negativa'}
# {
#     "usuario": "Jayanth Pudducheri",
#     "resenha_original": "Gerçekten harika, günlük yaşam için çok ihtiyaç duyulan bir uygulama",
#     "resenha_pt": "Realmente incrível, um aplicativo muito necessário para a vida cotidiana",
#     "avaliacao": "Positiva"
# }
# {'usuario': 'Jayanth Pudducheri', 'resenha_original': 'Gerçekten harika, günlük yaşam için çok ihtiyaç duyulan bir uygulama', 'resenha_pt': 'Realmente 
# incrível, um aplicativo muito necessário para a vida cotidiana', 'avaliacao': 'Positiva'}
# {
#     "usuario": "saikat das",
#     "resenha_original": "You guys are rocking. Out of this world, feels like Matrix.",
#     "resenha_pt": "Vocês estão arrasando. Fora desse mundo, parece com a Matrix.",
#     "avaliacao": "Positiva"
# }
# {'usuario': 'saikat das', 'resenha_original': 'You guys are rocking. Out of this world, feels like Matrix.', 'resenha_pt': 'Vocês estão arrasando. Fora desse mundo, parece com a Matrix.', 'avaliacao': 'Positiva'}
# {
#     "usuario": "Mohamedi Mustapha",
#     "resenha_original": "It's incredible help me to my university education Carrer",
#     "resenha_pt": "É incrível ajudar na minha carreira universitária.",
#     "avaliacao": "Positiva"
# }
# {'usuario': 'Mohamedi Mustapha', 'resenha_original': "It's incredible help me to my university education Carrer", 'resenha_pt': 'É incrível ajudar na minha carreira universitária.', 'avaliacao': 'Positiva'}
# {
#     "usuario": "James Williams",
#     "resenha_original": "this ai app has some good features but it is lacking in understanding.",
#     "resenha_pt": "Este aplicativo de IA possui alguns recursos bons, mas falta compreensão.",
#     "avaliacao": "Neutra"
# }
# {'usuario': 'James Williams', 'resenha_original': 'this ai app has some good features but it is lacking in understanding.', 'resenha_pt': 'Este aplicativo de IA possui alguns recursos bons, mas falta compreensão.', 'avaliacao': 'Neutra'}
# {
#     "usuario": "Alexis",
#     "resenha_original": "Cool, just wish there wasn't a limit for the free trial to be honest",
#     "resenha_pt": "Legal, só queria que não houvesse limite para o teste gratuito, para ser honesto.",
#     "avaliacao": "Negativa"
# }
# {'usuario': 'Alexis', 'resenha_original': "Cool, just wish there wasn't a limit for the free trial to be honest", 'resenha_pt': 'Legal, só queria que não houvesse limite para o teste gratuito, para ser honesto.', 'avaliacao': 'Negativa'}
# {
#     "usuario": "Mark Feldman",
#     "resenha_original": "L'IA est géniale, mais pour une raison inconnue, elle s'arrête sans arrêt, me dit « Une erreur s'est produite » et m'empêche totalement de l'utiliser. C'est vraiment dommage.",
#     "resenha_pt": "A IA é genial, mas por uma razão desconhecida, ela para sem parar, me diz 'Ocorreu um erro' e me impede totalmente de usá-la. É realmente lamentável.",
#     "avaliacao": "Negativa"
# }
# {'usuario': 'Mark Feldman', 'resenha_original': "L'IA est géniale, mais pour une raison inconnue, elle s'arrête sans arrêt, me dit « Une erreur s'est produite » et m'empêche totalement de l'utiliser. C'est vraiment dommage.", 'resenha_pt': "A IA é genial, mas por uma razão desconhecida, ela para sem parar, me diz 'Ocorreu um erro' e me impede totalmente de usá-la. É realmente lamentável.", 'avaliacao': 'Negativa'}
# {
#     "usuario": "Somshuvra Saha",
#     "resenha_original": "Database too old to use. No database opdate after that. It can give information regarding recent events. Gemini is best which 
# can give real time information.",
#     "resenha_pt": "Banco de dados muito antigo para usar. Nenhuma atualização do banco de dados depois disso. Pode fornecer informações sobre eventos recentes. Gemini é o melhor que pode fornecer informações em tempo real.",
#     "avaliacao": "Negativa"
# }
# {'usuario': 'Somshuvra Saha', 'resenha_original': 'Database too old to use. No database opdate after that. It can give information regarding recent events. Gemini is best which can give real time information.', 'resenha_pt': 'Banco de dados muito antigo para usar. Nenhuma atualização do banco de dados depois disso. Pode fornecer informações sobre eventos recentes. Gemini é o melhor que pode fornecer informações em tempo real.', 'avaliacao': 'Negativa'}
# {"usuario":"Ahmad Raza","resenha_original":"very good but it would be better if the normal version responded fast","resenha_pt":"muito bom, mas seria melhor se a versão normal respondesse mais rápido","avaliacao":"Positiva"}
# {'usuario': 'Ahmad Raza', 'resenha_original': 'very good but it would be better if the normal version responded fast', 'resenha_pt': 'muito bom, mas seria melhor se a versão normal respondesse mais rápido', 'avaliacao': 'Positiva'}
# {"usuario":"Andrew MacKay","resenha_original":"Voice frequently disconnects, and finding specific chats would be easier if we could tag them and filter by tag or custom gpt.","resenha_pt":"O áudio desconecta com frequência, e encontrar conversas específicas seria mais fácil se pudéssemos marcá-las e filtrá-las por tag ou GPT personalizado.","avaliacao":"Negativa"}
# {'usuario': 'Andrew MacKay', 'resenha_original': 'Voice frequently disconnects, and finding specific chats would be easier if we could tag them and filter by tag or custom gpt.', 'resenha_pt': 'O áudio desconecta com frequência, e encontrar conversas específicas seria mais fácil se pudéssemos marcá-las e filtrá-las por tag ou GPT personalizado.', 'avaliacao': 'Negativa'}
# {
#     "usuario": "Kavya Kavya",
#     "resenha_original": "je?li jest za darmo to daj? 5 gwiazdek ze wzgl?du na czat gpt 4.0 jak wiemy nie jest za darmo wi?c tylko 3 gwiazdki",
#     "resenha_pt": "Se fosse gratuito, daria 5 estrelas por causa do chat GPT-4.0, mas como sabemos que não é gratuito, apenas 3 estrelas.",   
#     "avaliacao": "Negativa"
# }
# {'usuario': 'Kavya Kavya', 'resenha_original': 'je?li jest za darmo to daj? 5 gwiazdek ze wzgl?du na czat gpt 4.0 jak wiemy nie jest za darmo wi?c tylko 3 gwiazdki', 'resenha_pt': 'Se fosse gratuito, daria 5 estrelas por causa do chat GPT-4.0, mas como sabemos que não é gratuito, apenas 3 estrelas.', 
# 'avaliacao': 'Negativa'}
# {"usuario":"Vaishnavi Tandon","resenha_original":"To use it a lot of improvements are still needed, specially for Indian","resenha_pt":"Para usá-lo, ainda são necessárias muitas melhorias, especialmente para a Índia","avaliacao":"Negativa"}
# {'usuario': 'Vaishnavi Tandon', 'resenha_original': 'To use it a lot of improvements are still needed, specially for Indian', 'resenha_pt': 'Para usá-lo, ainda são necessárias muitas melhorias, especialmente para a Índia', 'avaliacao': 'Negativa'}
# {
#     "usuario": "Hdfc Gg",
#     "resenha_original": "App is cool but developer should add more features on this app, like-generating photos and videos",
#     "resenha_pt": "O aplicativo é legal, mas o desenvolvedor deveria adicionar mais recursos, como geração de fotos e vídeos.",
#     "avaliacao": "Positiva"
# }
# {'usuario': 'Hdfc Gg', 'resenha_original': 'App is cool but developer should add more features on this app, like-generating photos and videos', 'resenha_pt': 'O aplicativo é legal, mas o desenvolvedor deveria adicionar mais recursos, como geração de fotos e vídeos.', 'avaliacao': 'Positiva'}
# {"usuario":"Yavuz YurtbeÃ„ÂŸendi","resenha_original":"Does not work on my tablet, it is stuck at loading screen","resenha_pt":"Não funciona no meu tablet, fica preso na tela de carregamento","avaliacao":"Negativa"}
# {'usuario': 'Yavuz YurtbeÃ„ÂŸendi', 'resenha_original': 'Does not work on my tablet, it is stuck at loading screen', 'resenha_pt': 'Não funciona no meu tablet, fica preso na tela de carregamento', 'avaliacao': 'Negativa'}
# {"usuario":"Eyob Getachew","resenha_original":"Aplica?ia e destul de bun?, dar dac? exist? acces la fotografii ar fi grozav, cum ar fi Ã®ntrebarea cu inteligen?a artificial?, Ã®mi place mai mult op?iunea asta ?i cred c? e ideea fiec?ruia.","resenha_pt":"O aplicativo é bem bom, mas se houvesse acesso a fotos seria ótimo, como a Pergunta com inteligência artificial, eu gosto mais dessa opção e acho que é a ideia de cada pessoa.","avaliacao":"Positiva"}
# {'usuario': 'Eyob Getachew', 'resenha_original': 'Aplica?ia e destul de bun?, dar dac? exist? acces la fotografii ar fi grozav, cum ar fi Ã®ntrebarea cu inteligen?a artificial?, Ã®mi place mai mult op?iunea asta ?i cred c? e ideea fiec?ruia.', 'resenha_pt': 'O aplicativo é bem bom, mas se houvesse acesso a fotos seria ótimo, como a Pergunta com inteligência artificial, eu gosto mais dessa opção e acho que é a ideia de cada pessoa.', 'avaliacao': 'Positiva'}
# {
#     "usuario": "Hrushi Padia",
#     "resenha_original": "I am unable to understand the symbols of mathematics as they are not getting converted. For example the multiplication sign i.e. ÃƒÂ— is shown as \\times_6 and same for all the symbols. I can't understand the sum as it gets hard to read.",
#     "resenha_pt": "Não consigo entender os símbolos de matemática pois eles não são convertidos. Por exemplo, o sinal de multiplicação, isto é, ×, aparece como \\times_6 e o mesmo acontece com todos os símbolos. Eu não consigo entender a soma pois fica difícil de ler.",
#     "avaliacao": "Negativa"
# }
# {'usuario': 'Hrushi Padia', 'resenha_original': "I am unable to understand the symbols of mathematics as they are not getting converted. For example the multiplication sign i.e. ÃƒÂ— is shown as \\times_6 and same for all the symbols. I can't understand the sum as it gets hard to read.", 'resenha_pt': 'Não consigo entender os símbolos de matemática pois eles não são convertidos. Por exemplo, o sinal de multiplicação, isto é, ×, aparece como \\times_6 e o mesmo acontece com todos os símbolos. Eu não consigo entender a soma pois fica difícil de ler.', 'avaliacao': 'Negativa'}
# {
#     "usuario": "Karli du Plessis",
#     "resenha_original": "Lo adoro, lo uso per cose molto dialogate, ma ora con il limite di messaggi, a mio parere è un po' ingiusto, nonostante le intenzioni. Non voglio usare la versione premium perché la versione gratuita ha sempre funzionato perfettamente per me. Non c'è un modo alternativo per gestirlo, oltre a imporre limiti praticamente a tutto? Isn't there an alternative way to manage it other than putting limits on literally everything?",  
#     "resenha_pt": "Eu adoro, uso-o para coisas muito dialogadas, mas agora com o limite de mensagens, na minha opinião, é um pouco injusto, apesar das 
# intenções. Não quero usar a versão premium porque a versão gratuita sempre funcionou perfeitamente para mim. Não há uma maneira alternativa de lidar com isso, além de impor limites praticamente a tudo? Não há uma maneira alternativa de gerenciá-lo além de colocar limites literalmente em tudo?",       
#     "avaliacao": "Neutra"
# }
# {'usuario': 'Karli du Plessis', 'resenha_original': "Lo adoro, lo uso per cose molto dialogate, ma ora con il limite di messaggi, a mio parere è un po' ingiusto, nonostante le intenzioni. Non voglio usare la versione premium perché la versione gratuita ha sempre funzionato perfettamente per me. Non c'è un modo alternativo per gestirlo, oltre a imporre limiti praticamente a tutto? Isn't there an alternative way to manage it other than putting limits 
# on literally everything?", 'resenha_pt': 'Eu adoro, uso-o para coisas muito dialogadas, mas agora com o limite de mensagens, na minha opinião, é um pouco injusto, apesar das intenções. Não quero usar a versão premium porque a versão gratuita sempre funcionou perfeitamente para mim. Não há uma maneira 
# alternativa de lidar com isso, além de impor limites praticamente a tudo? Não há uma maneira alternativa de gerenciá-lo além de colocar limites literalmente em tudo?', 'avaliacao': 'Neutra'}
# {
#     "usuario": "jason yones",
#     "resenha_original": "I like it but it always say \"I cannot assist with that\" for no reason, it just basically say the same word",
#     "resenha_pt": "Eu gosto, mas ele sempre diz \"I cannot assist with that\" sem motivo, basicamente repete a mesma frase",
#     "avaliacao": "Neutra"
# }
# {'usuario': 'jason yones', 'resenha_original': 'I like it but it always say "I cannot assist with that" for no reason, it just basically say the same word', 'resenha_pt': 'Eu gosto, mas ele sempre diz "I cannot assist with that" sem motivo, basicamente repete a mesma frase', 'avaliacao': 'Neutra'}    
# {
#     "usuario": "Ibrahim Ghani",
#     "resenha_original": "Middling experience. The web version feels nicer. This app feels... Obese.",
#     "resenha_pt": "Experiência mediana. A versão web parece mais agradável. Este aplicativo parece... obeso.",
#     "avaliacao": "Neutra"
# }
# {'usuario': 'Ibrahim Ghani', 'resenha_original': 'Middling experience. The web version feels nicer. This app feels... Obese.', 'resenha_pt': 'Experiência mediana. A versão web parece mais agradável. Este aplicativo parece... obeso.', 'avaliacao': 'Neutra'}
# {
#     "usuario": "AMISHA BESRA",
#     "resenha_original": "nÃ¥got visar ett oÃ¶vertrÃ¤ffat svar och en del information matchar inte det givna Ã¤mnet",
#     "resenha_pt": "Algum coisa mostra uma resposta excessivamente generosa e algumas informações não correspondem ao tópico dado.",
#     "avaliacao": "Negativa"
# }
# {'usuario': 'AMISHA BESRA', 'resenha_original': 'nÃ¥got visar ett oÃ¶vertrÃ¤ffat svar och en del information matchar inte det givna Ã¤mnet', 'resenha_pt': 'Algum coisa mostra uma resposta excessivamente generosa e algumas informações não correspondem ao tópico dado.', 'avaliacao': 'Negativa'}






