#DESAFIO48 TABUADA
'''num = int(input("digite um numero para ver sua tabuada"))
for c in range ( 1, 11):
    print("{} X {:2} = {} ".format(num , c , num * c))'''
#Desafio 50 soma pares
'''cont = 0
soma = 0
for c in range (1,7):
    n = int(input("digite 6 numeros"))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print("voce informou numeros {} pares  e a soma {} ".format(cont,soma))'''

#Desafio 51 razão
'''primeiro = int(input("digite o 1 termo"))
Razao = int(input("digite a razão :"))
decimo = primeiro + (11 - 1) * Razao
for c in range (primeiro, decimo , Razao):
    print(c)
print('fim')'''

#Desafio especial
'''num_Alunos = int(input("digite o numero de alunos da turma "))
cont = 1
soma = 0
while cont <= num_Alunos:
    nota = float(input("digite a nota do aluno {} ".format(cont)))
    soma = soma + nota
    media = soma /num_Alunos
    cont = cont + 1
    if nota < 5.0 :
        print("Aluno {} ".format(cont) , "reprovado")
    else :
        print("Aluno {} ".format(cont) , "aprovado")

print("O total de Alunos avaliados foram {}".format(num_Alunos))
print("a soma das notas é {} e a media da sala é {} : ".format(soma,media))
print("fim")'''

#Desafio 52 numeros primos
'''num = int(input("digite um numero"))
tot = 0
for cont in range ( 1, num + 1):
    if num % cont == 0:
        tot = tot +1
        print('\033[34m' , end = " ")

    else :
        print('\033[m' , end = " ")
    print("{}".format(cont), end=" ")
print("o numero {} foi divisivel {} vezes ".format(num , tot))
if tot == 2:
    print("por iso ele é primo !!! ")
else:
    print("e por isso ele não é primo")'''

'''faça um programa que leia 5 valores e guarde-os em uma lista 
no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes na lista.
'''
#DESAFIO78
'''valores = []
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(int(input(f"digite um valor  para a posição ${cont}: ")))#adicionar minhas posiçoes nos valores
    if cont == 0:                   #se o meu cont for igual a zero
        maior = menor = valores[cont]#tudo aqui vai ser zero
    else:
        if valores[cont] > maior:   #se os valores forem maior?
            maior = valores[cont]   #a variavel (maior) vai receber valores maiores
        if valores[cont]< menor:    #se os valores forem menor?
            menor = valores[cont]   #a variavel (menor) vai receber os valores menores
print("=_ "* 30)
print(f"voce digitou os valores {valores}")
print(f"o maior valor digitado foi {maior} nas posiçoes", end='')
for i , v in enumerate(valores): #indice e valor numerados
    if v == maior:               #se a variavel v = maior
        print(f' {i}....', end='')#aparece o meu indice
print()
print(f"o menor valor digitado foi {menor} nas posiçoes", end='')
for i , v in enumerate(valores):
    if v == menor:
        print(f" {i}....",end='')
print()'''




