# Recebe o nome do usúario
nome = input('Ola! Me diga qual o seu nome : ')

#Recebe a idade do usúario
idade = int(input('Qual a sua idade ? '))

# Recebe um número com o tamanho do nome digitado
tm = (len(nome))

# Recebe uma confirmação do usuário
conf = input('Ola {} !! Sua idade é de {} anos ! \nAs informações estão corretas ? (S / N) :  '.format(nome, idade)).upper
s = 's' in conf
print(s)
# Condição 
#ainda não funciona...
if  conf == ('S') :
            print('Que bom que está certo :)')

elif conf == ('N') :
    nome = input('O que deseja alterar ? O nome ou a idade ? ').upper
    if nome == ('NOME') :
       nome2 = input('Digite seu nome : ')
       print(f'Nome alterado !\Ola {nome2} seja bem-vindo !')
   

