'''
# Ex.1
clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

def lendo_nomes(lista: list) -> None:
    for nome in lista:
        print(nome)

lendo_nomes(clientes)

# Ex.2
def cont():
    contador = 0
    while contador < 10:
        contador += 1
        print("Processando dados...")

cont()

# Ex.3
def repeticao(num_vezes):
    contador = 0
    while contador < num_vezes:
        contador += 1
        print("Bem-vindo ao buscante!")

repeticao(5)

# Ex.4
valores = [10, 20, 30, 40, 50]
def soma_lista(valores: list):
    sum = 0
    for valor in valores:
        sum += valor
    print(sum)

soma_lista(valores)


# Ex.5
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

def lista_projetos(lista: list):
    for item in lista:
        if(item == None):
            print("Projeto ausente")
        else:
            print(item)

lista_projetos(projetos)

# Ex.6
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
def encontrar_livro(lista_livros: list, livro):
    for item in lista_livros:
        if item == livro:
            print(f"Livro encontrado: {item}")
            break

encontrar_livro(livros, "O Hobbit")

# Ex.7
def controle_estoque(qtd_estoque):
    while qtd_estoque >= 0:
        if qtd_estoque > 0:
            print(f"Venda realizada! Estoque restante: {qtd_estoque}")
        else:
            print("Estoque esgotado")
        qtd_estoque -= 1

controle_estoque(4)

# Ex.8
def contagem(segundos):
    while segundos >= 0:
        if segundos % 2 == 0 and segundos != 0:
            print(f"Faltam apenas {segundos} segundos")
        elif segundos % 2 == 1:
            print(f"A contagem continua: {segundos} segundos restantes")
        else:
            print("Aproveite a promoção agora")
        segundos -= 1

contagem(10)

# Ex.9
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]
def livro_disponivel(livros):
    for livro in livros:
        if livro["estoque"] > 0:
            print(livro["nome"])
        else:
            print("Livro indisponivel")

livro_disponivel(livros)

# Ex.10
def login():
    user = input("Digite o seu nome de usuário-> ")
    senha = input("Digite a sua senha: ")
    while len(user) < 5 and len(senha) < 8:
        if len(user) < 5:
            print("Pelo menos 5")
        if len(senha) < 8:
            print("Pelo menos 8")
        user = input("Digite o seu nome de usuário-> ")
        senha = input("Digite a sua senha")
    print(user)
    print(senha)

login()
'''