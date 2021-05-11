'''c= 1
while c < 10 :# enquanto o c for menor que 10 faça o c receber + 1
    print(c)
    c = c +1
print ('fim')'''
'''n=1
soma = 0
while n != 0:
    n= int(input("digite numero"))
    soma = soma + n
print(n)
print("para sai digite 0 , a soma total é {}".format(soma))'''

'''r = 's'
while r =='s':
    n =int(input('digite um numero'))
    r =str(input("quer continuar s/n")).lower()
print("fim")'''

n = 1
par = impar = 0
while n != 0 :
    n = int(input("digite um valor "))
    if n !=0:
     if  n % 2 == 0:
         par = par +1
     else:
        impar = impar +1
print("voce digitou numeros pares {} e {} numeros impares".format(par,impar))
