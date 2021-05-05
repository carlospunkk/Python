'''nome = str(input('digite seu nome'))
if nome == 'gustavo':
    print("que nome lindo voce tem")
elif nome == ' pedro ' or nome == 'maria' or nome == 'joaquin':
    print("voces foram os escolhidos")
else:
    print("seu nome é bem normal")
print("se ja bem vindo {}".format(nome))'''

#desafio36
import random

'''valor_Casa = float (input('digite aqui o valor da casa'))
salario = float(input('digite aqui o seu salario'))
anos = float (input('digite em quantas parcelas vc vai pagar'))
valor_prestação =valor_Casa /( anos * 12)
minimo = salario *30 / 100
print ("para pagar uma casa de R$ {:.2f} em {} anos".format(valor_Casa , anos))
print("a prestação será de {:.2f}".format(valor_prestação))
if valor_prestação <= minimo :
    print("emprestimo concedido!!")
else:
    print("emprestimo negado !!!")'''

#desafio37 convertendo numeros
'''numero = int(input('digite um numero inteiro '))
print('''''')
opcao = int(input("sua opção"))
if opcao == 1:
    print("{} o valor convertido para binário  é igaul a {} ".format(numero, bin(numero)))
elif opcao == 2:
    print("o {} valor convertido para Octal é {} ".format(numero, oct(numero)))
elif opcao == 3 :
    print("o {} valor convertido para hexadecimal é{} ".format(numero, hex(numero)))
else:
    print("digite uma opção valida ")'''

'''#desafio39
from datetime import date
atual  = date.today().year
nasc = int(input("digite sua data de nascimento"))
idade = atual - nasc
print("quem nasceu em {} anos tem {} anos  no ano {} atual ".format(nasc , idade , atual))
if idade == 18 :
    print("voce tem {} anos em {} no ano atual se aliste agora !!!! ".format(idade , atual))
elif idade < 18 :
    saldo = 18 - idade
    print("voce ainda não tem  18 anos ainda falta {} anos para o alistamento ".format(saldo))
elif idade > 18 :
    saldo = idade - 18

    print("voce já passou do prazo do alistamento , e está atrasado em {} anos!!!".format(saldo))
    '''
#desafio 40
'''n1 = float(input("digite sua primeira nota  "))
n2 = float(input('digite sua nota '))
media = (n1+n2)/2
if media <= 5.0 :
    print('reprovado {}'.format(media))
elif media >=5  and media <7:
    print("recuperação {} media".format(media))
elif media > 7.0 :
    print('aprovado {} media'.format(media))'''



'''from datetime import date
atual = date.today().year
idade = int(input("digite a sua idade "))
nasc = ( atual - idade)
if idade >= 1 and idade <9 :
    print("voce é mirim sua idade é {} e voce nasceu no ano de {}".format(idade,nasc))
elif idade >=9 and idade <=14 :
    print("sua categoria é infantil {} e voce nasceu no ano de {}".format(idade,nasc))
elif idade >=14 and idade <=20:
    print("sua categoria é senior {} e voce nasceu no ano de {}".format(idade,nasc))
elif idade >= 20 :
    print('sua categoria é  master e voce nasceu no ano de {}'.format(idade,nasc))'''

#comando for
'''lista = [10,15,16,17,18,19,20]
for valor in lista:
    print(valor)'''
#com string (contagem de caracteres de uma frase)
'''frase = ('a ligeira raposa marrom ataca o cão preguiçoso')
qtd_letras = 0 #inicia com 0 letras
for letra in frase :# a variavel letra recebe a variavel frase enquanto isso incremente na qtd_letras
    qtd_letras +=1
    print(" a frase possui "+ str(qtd_letras) + "letras.")'''
#variavel acumuladora
'''dados = [[ 1 , 2, 3 ], [4 , 5 , 6 ], [7 , 8 , 9 ]]
soma = 0
qtd = 0
for valor in dados:
    soma += valor
    qtd += 1
    print(soma)
    print(qtd)
media = soma /qtd
print(media)'''






























