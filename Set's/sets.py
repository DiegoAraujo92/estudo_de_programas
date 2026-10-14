set_vazio = set()

set1 = {'nome', 1, 2, 3}
print(set1)

lista_set = [1, 2, 3, 3, 3, 3 ,3, 1]
lista2 = set(lista_set)  # Converte a lista em um set, removendo os elementos duplicados
lista_set = list(lista2)  # Converte o set de volta para uma lista, sem elementos duplicados.
print(lista2)
print(lista_set)

print(3 in set1)  # Verifica se o elemento 3 está presente no set1
for numero in set1:
    print(numero)  # Itera sobre os elementos do set1 e imprime cada elemento

set_vazio.add('Diego') # Adiciona o elemento 'Diego' ao set_vazio
set_vazio.add(1)
set_vazio.update(['Araujo', 1])  # Em caso de .update() se passar uma string como parâmetro,
print(set_vazio)                 # o set() vai iterar sobre as letras da string, add mais de 1 elemento

set_limpo = {1, 2, 3, 4, 5}
set_limpo.clear()             # Limpa todos os elementos do set().
print(set_limpo)


s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1.union(s2) or s1 | s2  # Une os dois sets o metodo e o operador =>' | '<=
print(s3)

s4 = s1.intersection(s2) or s1 & s2  # Encontra a interseção dos dois sets e o operador =>' & '<=
print(s4)

s5 = s1.difference(s2) or s1 - s2 # Encontra a diferença entre os dois sets e o operador =>' - '<=
print(s5)                          # o set qu vem primeiro é o que aparce, ou seja da esquerda para a direita. 

s6 = s1.symmetric_difference(s2) or s1 ^ s2  # Encontra a diferença simétrica entre os dois sets e o operador =>' ^ '<=
print(s6)

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrar_numeros_unicos(lista_de_listas):
    numeros_unicos = set()  # Cria um set vazio para armazenar os números únicos

    for lista in lista_de_listas:
        numeros_unicos.update(lista)  # Adiciona os elementos da lista ao set, removendo duplicatas
    
    return numeros_unicos  # Retorna o set de números únicos
 
for lista in lista_de_listas_de_inteiros:
    print(encontrar_numeros_unicos(lista_de_listas_de_inteiros))  # Imprime cada lista e o set de números único