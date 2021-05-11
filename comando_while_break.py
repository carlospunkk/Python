'''cont = 1
while cont <= 10:
    print(cont, " ", end=" ")
    cont += 1
print("acabou")'''

'''num = 0
s = 0
while True :
    num = int(input("digite um numero"))
    if num == 999:
        break
    s += num
#print("a soma é {}".format(s))
print(f'a soma é {s}')'''
'''
#Desafio 66
num = 0
soma = 0
cont = 0
while True :
    num = int(input("digite os numeros"))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f"a soma dos numeros são {soma} e a quantidade de numeros somados foram {cont}")'''

'''
#Desafio67_tabuada
while True:
    num = int(input("escolha a tabuada "))
    if num < 0 :
       break
    for c in range (1,11):
        print(f"a tabuada de {num} X {c} = {num *c}")
print("acabou volte sempre")'''

# Desafio 68
'''
from random import randint
v = 0
while True :
    jogador = int (input("diga um valor "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input("escolha Par ou Impar ")).strip().upper()[0]
    print(f"voce jogou {jogador} eo computador {computador} total de {total}")
    if tipo == 'P':
        if total % 2 == 0 :
          print("voce ganhou ")
          v+=1
        else:
          print("voce perdeu")
          break
    elif tipo == 'I':
     if total % 2 ==1:
          print(" vc venceu ")
          v +=1
     else:
          print("vc perdeu")
          break

print("vamos jogar novamente")
print(f"game over vc venceu tantas vezes {v}")'''
#-------programa-papel-de-parede-------------
from math import ceil
largura = float (input("digite a largura da sua parede"))
altura = float (input("digite a altura da sua parede"))
preco_rolo = float (input("digite o preço do rolo"))
valor_instalação = 109.90
m2 = largura*altura
quantidade_rolo = m2 / 4
total = (preco_rolo * ceil(quantidade_rolo))
sub_total = (ceil(quantidade_rolo) * valor_instalação)
s = total + sub_total


print("o total da compra é  R$ {} ".format(s))
print("a sua medida é {:.2f} m²".format(m2))
print(" e a quantidade necessaria de rolos é {} ".format(ceil( quantidade_rolo)))













