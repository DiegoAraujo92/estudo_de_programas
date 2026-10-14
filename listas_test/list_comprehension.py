
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)
print()

#ou

lista = [numero for numero in range(10)]
print(lista)
print()

# list comprehension executando um for dentro
# da lista passando uma multiplicação como parâmetro
# a esquerda do for 

                # Mapeamento
lista = [numero *5 for numero in range(10)]
print(lista)
print()

# mapeamento de dicionários com list comprehension.
# É uma forma curta e direta de criar uma nova lista a
# partir de uma sequência ou de outro iterável, 
# como uma lista, uma tupla ou um range.
# Lista de produtos com preço atualizado em 5% a mais

produtos = [
    {"nome": "p1" , "preco": 10.0},
    {"nome": "p2", "preco": 20.0},
    {"nome": "p3", "preco": 30.0},
    {"nome": "p4", "preco": 40.0},
    {"nome": "p5", "preco": 50.0}
]
print(*produtos, sep="\n")
print()
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
      for produto in produtos
    ]
print(*novos_produtos, sep="\n")
print()


                # Filtro
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
      for produto in produtos if produto["preco"] < 30
    ]

print(*novos_produtos, sep="\n")
print()

# isisntance() é uma função que verifica
# o tipo do objeto

lista1 = [
    'a', 5, 1.1, True, (1, 2), [1, 2],
    {1, 2}, {"nome": "Luiz"}
]

for item in lista1: 
    if isinstance(item, set):
        print('SET')
        print(item, isinstance(item, set))

    elif isinstance(item, dict):
        print('DICT')
        print(item, isinstance(item, dict))

    elif isinstance(item, list):
        print('LIST')
        print(item, isinstance(item, list)) 

    elif isinstance(item, tuple):
        print('TUPLE')
        print(item, isinstance(item, tuple))

    elif isinstance(item, str):
        print('STR')
        print(item, isinstance(item, str))

    else:
        print('OUTRO')
        print(item, isinstance(item, (int, float, bool)))    

