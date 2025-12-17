from openai import OpenAI # type: ignore


client = OpenAI(
    base_url="https://127.0.0.1:1234/v1",
    api_key = 'sk-1234'
)

resposta_do_llm = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Quem foi Albert Einstein?"},
    ],
    temperature=0.7  

)

print(resposta_do_llm.choices[0].message.content)











# try:
#     idade = int(input("Digite sua idade: "))
#     if idade < 0:
#         raise ValueError("Idade não pode ser negativa.")
#     print(f"Sua idade é {idade} anos.")
#     nome = input("Digite seu nome: ")
#     nome + idade  # Isso causará um TypeError

# except ValueError as e:
#     print(f"Você não digitou um número válido")
# except TypeError as e:
#     print("Erro de tipo: valor inválido fornecido.")
# except Exception as e:
#     print(f"Ocorreu um erro inesperado: {e}")
# finally:
#     print("Programa encerrado.")
