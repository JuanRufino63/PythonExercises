'''
# Ex.1
def format_saudacao():
    nome_cliente = input("Digite o nome da cliente: ")
    cidade_cliente = input("Digite o nome da cidade do cliente: ")
    print(f"Olá {nome_cliente}! Bem_vinda ao sistema da cidade de {cidade_cliente}.")
format_saudacao()

# Ex.2
def pistas():
    palavra_chave = input("Digite a palavra-chave: ")
    print(palavra_chave[:3])
    print(palavra_chave[-3:])

pistas()

# Ex.3
def inicio_fim_string():
    url = input("Digite a URL para validação: ")
    if url.startswith("https://") and url.endswith(".com"):
        print("URL válida")
    else:
        print("URL inválida")

inicio_fim_string()

import re


# Ex.4
def receita():
    descricao_receita = input("Digite a descrição da receita: ")
    num = re.findall(r'\d+', descricao_receita)[0]
    print(num)

receita()
'''
