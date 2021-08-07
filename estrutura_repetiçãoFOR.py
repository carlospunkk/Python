'''n = int (input("digite numero"))
for cont in range (0 , n):#o meu cont vai receber de 0 até o numero digitado
    print(cont)'''

#estrutura for aqui coloco as informações do inicio
'''i = int(input("digite inicio "))
f = int(input("fim"))
p = int(input("passo"))
for cont in range (i , f+1 , p):
    print(cont)
print("final")'''
#soma dos valores
'''s = 0
for c in range (0,4):
    n = int(input("digite o numero"))#repete essa ação 4 vezes 
    s += n
print("a soma dos valores {}".format(s))'''

'''#exercicios46
from time import sleep
for c in range (10, -1, -1):
    print(c)
    sleep(0.5) #contagem regressiva
print(" estoura fogos !!!")'''

#exercicio 47
'''for c in range ( 0 , 52, 2):
   print(c)
print("os numeros pares são ")
'''


#exercicio48acumuladores
'''soma = 0
cont = 0
for c in range (1,501,2):
 if  c % 3 == 0:
    cont += 1 # conta todos os numeros impares fazendo um loop
    soma += c #soma todos os numeros impares  e acumula todos aqui a cada loop ele somou
print("a soma de todos os numeros solicitados é {}".format(soma))
print("a quantidade de numeros somados é {}".format(cont))

print("fim!!!!!")'''
'''soma = 0
for numero in range (10):
    if numero % 2 == 0:
        soma += numero
        print (numero)'''

'''nverificados = 0 # qtd de numeros verificados inicia 0
nmultiplos = 0   # qtd numeros multiplos inicia 0
for numeros in range(20): #numeros recebe de 1 até 20 posiçoes
    nverificados +=1# conta 20 vezes
    if numeros % 3 == 0:#condição pegue todos os numeros divisiveis por 3 e repita nmultiplos
        nmultiplos +=1
print(nverificados)
print(nmultiplos)'''

'''#fatorial
numero =  int(input("digte o numero fatorial que quer descobrir "))
fatorial = 1
for termo in range(1 , (numero + 1)):
    fatorial *= termo
print("o fatorial de {}  : é {} ".format(numero ,fatorial ))'''
#somando duas listas
'''A =[2 , 3 , 4]
B = [5 , 6 , 7]
C = []
for indice in range(3):
    C.append(A[indice]+B[indice])
print(C)'''
#numeros primos
'''NumPrimos = []
for numero in range (20):
    div = 0
    for divisor in range ( 1,  numero + 1 ):
     if (numero % divisor) == 0:
        div = div + 1
if div == 2:
       NumPrimos.append(numero)
print(NumPrimos)'''
'''s = 0
for c in range (0,4):
    n = int(input("digite numero"))
    s += n
print(s)'''


'''quantidade =0                       # recebe 0
soma =0                             # recebe 0
for c in range (0,2):               #inicio 0 e termina no 2 o laço
    n = int(input("digite numero")) #entrada de dados
    quantidade += 1                 # aqui conta a quantidade de vezes do laço
    soma = soma + n                  # aqui soma ( n  digitado duas vezes )


print ("a quantidade de posiçoes é : ", quantidade)
print (" soma é {}".format(soma))'''
'''verificados =0
multiplos = 0
for numero in range (19):
    verificados += 1
    if numero % 3 == 0:
        multiplos += 1
print("verificados" , verificados)
print("multiplos ", multiplos)'''








