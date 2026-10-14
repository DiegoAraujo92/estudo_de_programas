import copy


pessoa = {
    'nome': 'Armando',
    'sobrenome': 'Araujo',
    'idade': 30,
}
#                 Comandos uteis para dicionários
#print(len(pessoa))  # 2
#print(list(pessoa.keys()))  # ['nome', 'sobrenome']
#print(list(pessoa.values()))  # ['Armando', 'Araujo']
#print(list(pessoa.items()))  # [('nome', 'Armando'), ('sobrenome', 'Araujo')]

pessoa.setdefault('idade', None)  # Se não ouver a chave
                                  # 'idade', adiciona com valor None

for key, value in pessoa.items():
    print(key, value), 

d1 = {'c1': 1,
      'c2': 2,
      'l1': [1, 2, 3],
}

# Shallow copy (cópia rasa) - cria uma cópia do dicionário,
#  mas se houver objetos mutáveis dentro, ele não entra nos
# sub-niveis, entra apenas no primeiro objeto. 

d2 = copy.copy(d1) # Cria uma cópia rasa de d1 na variavel d2

# d2 = copy.deepcopy(d1) # Cria uma cópia profunda
# de d1 na variavel d2, entrando em todos os sub-niveis
# do dicionário.


d2['c1'] = 10  # Modifica o valor da chave 'c1' em d2
d2['l1'][1]= 10

print(d1)  
print(d2)  

# .get(chave, chave_nao_encontrada) Retorna o valor da chave
#  dentro do dicionário, caso a chave não exista, retorna
#  o valor default passado como segundo argumento.

print(d1.get('c1' , 'Chave não encontrada'))  

nome = pessoa.pop('nome', 'Chave não encontrada')  # Remove a chave 'nome' do dicionário
print(nome)
print(pessoa)

pessoa.update(nome='Armando')
print(pessoa)