'''lanche = ('hamburguer', 'suco', 'pizza' , 'pudim')
for comida in lanche:
    print(f"eu vou comer {comida}")
print('comi pra caramba !!!!')'''
#ex:2
'''lanche = ('hamburguer', 'suco', 'pizza' , 'pudim', 'batata')
for cont in range (0 , len(lanche)):
    print(f"eu vou comer {lanche [cont]}")'''
#ex:3
'''lanche = ('hamburguer', 'suco', 'pizza' , 'pudim', 'batata')
for cont in range (0 , len(lanche)):
    print(f"eu vou comer {lanche [cont]} na posição {cont}")'''
#ex:4
'''lanche = ('hamburguer', 'suco', 'pizza' , 'pudim', 'batata','abacate')
for pos , comida in enumerate(lanche):
    print (f"eu vou comer {comida}na posição {pos}")'''
#ex:5
'''lanche = ('hamburguer', 'suco', 'pizza' , 'pudim', 'batata','abacate')
print(sorted(lanche))'''
#ex:6
'''a= ( 2, 5 , 4)
b =( 5, 8, 1, 2)
c = b + a
print(c.count(8))'''
#ex:7
'''a= ( 2, 5 , 4)
b =( 5, 8, 1, 2)
c = b + a
print(c)
print(c.index( 5, 1))'''
#ex:8
'''galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):#digite 3 nomes e armazena em c
    dado.append(str(input('Nome: ')))#dados recebe os nomes digitados
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:#se a idade for maior que 21 / senão idade vai ser menor
        print(f"{p[0]} é maior de idade")
        totmai+=1# conte os maiores de idade
    else:
        print(f"{p[0]} é menor de idade")
        totmen+=1#conte os menores de idade
print(f"temos {totmai} maiores e {totmen} menores de idade")'''





