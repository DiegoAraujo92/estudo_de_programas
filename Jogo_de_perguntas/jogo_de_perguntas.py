perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2?',
        'opcoes': ['3', '4', '5', '6'],
        'resposta_correta': '4'
    },
    {
         'pergunta': 'Quanto é 6 * 7?',
         'opcoes': ['42', '48', '54', '60'],    
         'resposta_correta': '42'
    },
    {
         'pergunta': 'Quanto é 100 / 25?',
         'opcoes': ['3', '4', '5', '6'],   
         'resposta_correta': '4'
    },
  
]
respostas_certas = ''


print("Bem-vindo ao jogo de perguntas e respostas!"+'\n')

print("Digite 'exit' a qualquer momento para sair do jogo." + '\n')

for pergunta in perguntas:
    print('Pergunta: ' + pergunta['pergunta'] + '\n')
    for i, opcao in enumerate(pergunta['opcoes'], start=1):
        print(f"{i}.) {opcao}" + '\n')
    
        
    

    resposta =  int(input("Digite o número da resposta correta: "))
    if resposta == pergunta['resposta_correta']:
        print("Resposta correta!")
    else:
        print("Resposta incorreta.")

