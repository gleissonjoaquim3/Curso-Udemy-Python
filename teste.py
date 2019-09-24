# Importa do módulo datatime
import datetime

# Recebe o nome do usúario
nome = input('Ola! Me diga qual o seu nome : ')

#Recebe a idade do usúario
idade = int(input('Qual a sua idade ? '))

# Recebe um número com o tamanho do nome digitado
tm = (len(nome))

# Recebe uma confirmação do usuário
conf = input('Ola {} !! Sua idade é de {} anos ? (S / N) :  '.format(nome, idade)).upper

# Recebe a resposta S ou N
resp = conf

# Condição
if conf == ('S') :
    print('Que bom que está certo :)')
else :
    nome = input ('Qual deseja alterar o nome ou a idade ? ')
    