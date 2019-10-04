from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('En que ano voce nasceu : '))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é de maior')
        totmaior += 1
    else:
        print('Essa pessoa é de menor')
        totmenor += 1

print(f'Ao todo temos {totmaior} maiores de idade e {totmenor} menores de idade')
