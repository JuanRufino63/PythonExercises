# Lista de exercícios de tupla e listas
'''
# Ex.1
despensa = ["açucar", "arroz", "feijão"]
def verificando_itens(lista: list):
    item = input("Digite o item que você quer verificar: ")
    if item in lista:
        print(f"Tem o {item} na despensa")
    else:
        print(f"A/O {item} precisa ser comprado")

verificando_itens(despensa)

# Ex.2
def organizando_notas():
    notas = input("Digite a lista de notas: ")
    lista_notas = [int(nota) for nota in notas.split(",")]
    lista_notas.sort()
    print(lista_notas)

organizando_notas()

# Ex.3
def organizando_voluntarios():
    voluntarios = []
    entrada = input("Digite o nome do voluntario: ")
    while entrada != "sair":
        voluntarios.append(entrada)
        entrada = input("Digite o nome do voluntario ou sair para encerrar o programa: ")
    print(voluntarios)

organizando_voluntarios()

# Ex.4
def relatorios_estoque():
    relatorio_1 = tuple(input("Produtos do estoque 1(separados por vírugla) : ").split(","))
    relatorio_2 = tuple(input("Produtos do estoque 2(separados por vírgula) : ").split(","))
    estoque_combinado = relatorio_2 + relatorio_1
    print(estoque_combinado)

relatorios_estoque()

# Ex.5
lista_inicial = ["Ana", "Pedro", "Carlos"]
def reorganizando_lista(lista_convidados):
    print(f"Lista atual de convidados: {lista_convidados}")
    nome_convidado = input("Digite o nome do novo convidado: ")
    posicao = int(input("Digite a posição : "))
    lista_convidados.insert(posicao - 1, nome_convidado)
    return lista_convidados

print(reorganizando_lista(lista_inicial))

# Ex.6
eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
def ordenando_eventos(lista_eventos):
    lista_eventos.reverse()
    return lista_eventos

print(ordenando_eventos(eventos_registrados))

# Ex.7
lista = ['Ana', 'Carlos', 'Pedro']
def corrigindo_posicoes(lista_nomes):
    nome_incorreto = input('Digite o nome incorreto: ')
    nome_certo = input('Digite o nome correto: ')
    print(f'O nome {nome_incorreto} foi substituido por {nome_certo}')
    for i in range(len(lista_nomes)):
        if lista_nomes[i] == nome_incorreto:
            lista_nomes[i] = nome_certo
    return lista_nomes

print(corrigindo_posicoes(lista))

# Ex.8
def removendo_item():
    pedidos_feitos = ['Sanduiches', 'Suco', 'Sobremesa']
    print(", ".join(str(pedido) for pedido in pedidos_feitos))
    pedidos_feitos.pop(-1)
    print(f"Pedidos finais: {pedidos_feitos}")

removendo_item()
'''
# Ex.9
def calculando_medias():
    notas_alunos = input("Digite as notas dos alunos separados por vírgula: ").split(",")
    notas_alunos = [float(nota) for nota in notas_alunos]
    media = round(sum(notas_alunos) / len(notas_alunos), 2)
    print(media)

calculando_medias()
