import sys

cpf = input("Digite o seu CPF,(somente números): ")

first_char_rep = cpf == cpf[0] * len(cpf)
print("O CPF digitado foi: ", cpf)

cpf = cpf.replace(".","")\
         .replace("-","")\
         .replace(" ","")
    

if first_char_rep:
    print("CPF inválido, todos os dígitos são iguais.")
    sys.exit()

nove_dig = cpf[:9]
count_regres = 10
Result_dig1 = 0

for digito_1 in nove_dig:
    Result_dig1 += int(digito_1) * count_regres
    count_regres -= 1
    digito_1 = (Result_dig1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
dez_dig = nove_dig + str(digito_1)
count_regres2 = 11
Result_dig2 = 0

for digito_2 in dez_dig:
    Result_dig2 += int(digito_2) * count_regres2
    count_regres2 -= 1
    digito_2 = (Result_dig2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

validacao_CPF = f'{nove_dig}{digito_1}{digito_2}'
if cpf == validacao_CPF:
     print(f'O CPF {validacao_CPF}'' é válido.')
else:
     print(f'CPF inválido.')