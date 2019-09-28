# Recebe o nome do usúario
nome = input('Ola! Me diga qual o seu nome : ')
#Recebe a idade do usúario
idade = int(input('Qual a sua idade ? '))
# Printa o nome e idade do usuário
print(f'Ola {nome} !! Sua idade é de {idade} anos !')
#Recebe resposta da pergunta
resp = str(input('Seu nome e idade estão corretos ? (S / N) ? '))
#Condição para resposta negativa
if  resp == 'N' :
    nome1 = input('O que deseja alterar ? (NOME / IDADE) ? ')
    if nome1 == 'NOME':
        nome2 = input('Digite seu nome : ')
        print(f'Muito bem {nome2} ! Seu nome foi alterado !' )
    if nome1 == 'IDADE' :
        nome3 = input('Digite dua idade : ')
        print(f'Muito bem {nome} ! Sua idade foi alterada para {nome3} anos !' )
#Necessita de melhorias
#    if nome1 != 'NOME' and 'IDADE' :
#       print('Não endenti...')
else :
    print('Que bom que está certo :)')
print('tenha um Bom Dia !! ')
    


