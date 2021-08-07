'''num = [2,5,9,1]
num [1] = 3 #trocando a posicao 1 por 3 que seria o numero 5 da lista
num.append(7)#adicionando o valor 7
num.sort()#coloca em ordem
del num[2]#aqui deleta um item da lista
num.insert( 1 , 0 )# insere um numero na posição 1 , insere o numero 0
num.pop()      #elimina o ultimo elemento da lista
print (num)
print(f"essa lista tem {len(num)} elementos")# o len mostra quantos elementos tem tem'''
'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for p , v in enumerate(valores) :
    print(f'na posição {p} encontrei o valor {v}...')'''
'''
valores = []
for cont in range(0,5):
    valores.append(int(input("digite um valor: ")))#acrescentei um valor em (valores) e repete esta ação 5 vezes
#print(f' voce digitou ${valores}')

for c , v in enumerate(valores):#aqui vai enumerar todos os valores até 5
    print(f"na posição {c}encontrei o valor {v}") #mostro a  minha posição c e o valor adicionado nela
print("cheguei ao final da lista")'''
'''a = [1,3,4]
b = a[:]# AQUI UTILIZEI [:] PARA CRIAR UMA COPIA NA LISTA B / sem isso ele cria uma ligação
b[1]=8
print(f"lista A {a}")
print(f"lista B {b}")'''

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






