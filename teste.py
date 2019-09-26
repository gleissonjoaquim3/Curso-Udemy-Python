# Recebe o nome do usúario
nome = input('Ola! Me diga qual o seu nome : ')
#Recebe a idade do usúario
idade = int(input('Qual a sua idade ? '))
# Printa o nome e idade do usuário
print(f'Ola {nome} !! Sua idade é de {idade} anos !')

resp = str(input('Seu nome e idade estão corretos ? (S / N) ? '))
# Condição
#ainda não funciona...
if  resp == 'S' :
            print('Que bom que está certo :)')
else :
    resp1 = input('O que deseja alterar ? (Nome / Idade) ? ')
#Ainda não funciona
if resp1 == 'Nome' :
    nome1 = input('Digite seu nome : ')
    print(f'Muito bem {nome1} ! Seu nome foi aterado !')
else  :
    nome2 = input('Digite sua idade : ')
    print(f'Muito bem {nome1} ! Sua {nome2} foi aterado !')


