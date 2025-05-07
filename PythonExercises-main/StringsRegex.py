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
    num = re.findall(r'd+', descricao_receita)[0] //tirei o barra para parar de dar um aviso chato
    print(num)

receita()

# Ex.5
def substituindo_palavras():
    texto = input("Digite o texto a ser revisado: ")
    substituicao = input("Qual palavra deseja substituir: ")
    nova_palavra = input("Qual a nova palavra: ")
    texto_novo = texto.replace(substituicao, nova_palavra) //re.sub->pode-se usar
    print(texto_novo)

substituindo_palavras()

import re


# Ex.6
def validando_nomes():
    nome_cliente = input("Digite o nome cliente para validação: ")
    if re.fullmatch(r'[A-Z][a-z]*', nome_cliente):
        print("Nome válido")
    else:
        print("Nome inválido")

validando_nomes()

import re

# Ex.7
def cpf_check():
    cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
    if re.fullmatch(r'\d{3}.\d{3}.\d{3}-\d{2}',cpf):
        print("CPF válido")
    else:
        print("CPF inválido")

cpf_check()

import re


# Ex.8
def letras_especificas_comeco():
    livro = input("Digite o título do livro: ")
    letra_inicial = input("Digite a letra inicial: ")
    palavras = re.findall(rf"\b{letra_inicial}[a-zá-ÿ]*", livro, re.IGNORECASE)
    print(palavras)

letras_especificas_comeco()

import re


# Ex.9
def informacoes_pacientes():
    paciente = input("Digite o nome completo e o ano de nascimento do paciente: ")
    padrao = r'(\w+) (\w+) - (\d{4})'

    resultado = re.search(padrao, paciente)
    if resultado:
        primeiro_nome = resultado.group(1)
        sobrenome = resultado.group(2)
        ano_nascimento = resultado.group(3)
        print(f"Primeiro Nome: {primeiro_nome}")
        print(f"Sobrenome: {sobrenome}")
        print(f"Ano de Nascimento: {ano_nascimento}")
    else:
        print("Saída inválida")

informacoes_pacientes()
'''

