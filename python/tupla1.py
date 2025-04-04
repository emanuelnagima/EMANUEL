#tuplas são imutaveis
lanche = ('pizza', 'merda' , 'hamburguer' , 'pastel')
print(lanche[1])
print(lanche)
for y, a, in enumerate(lanche):
    print(f'eu vou comer {a}, posição {y}')

carro = ('bmw' , 'celta' , 'toyota' , 'caminhão' , 'ethios')
print(carro)
print(carro[-1])
print(carro[0:2])
print(carro[3])


#função len, usar para contar quantos elementos há
print(len(carro))  

#estrtura de repetição
for c in carro:
    print(f'eu vou comprar este carro: {c}')
print('EU SOU RICOOOOOO')

#pra achar a posição do elemento na estrutura de repetição 
#usar assim: for__in__enumerate(     )             
#ENUMERATE
for e, c in enumerate(carro):
    print(f'eu vou comprar este carro: {c}, na posição {e}')
    





time = ('santos' , 'são paulo' , 'palmeiras' , 'flamengo')
print(time)

for posição, times in enumerate(time):
    print(f'eu vou torcer pelo {times} na posição {posição}')





#para ordenar, utilizar print(sorted(time)) 
#SORTED
print(sorted(time))




#EXEMPLO COM NUMEROS

a=(1,2,5,6,7,8,1)
b=(2,5,6)
print(a,b)

c=a+b
print(c)


#QUANTAS VEZES O NUMERO REPETE? COLOCAR NUMERO DESEJADO ENTRE PARENTESES
#COUNT
print(c.count(6))

#ESTA EM QUAL POSIÇÃO? pegara somente o primeiro número 
#INDEX
print(c.index(5))



#EXEMPLO DE ERROS, sort e adição []
frutas = ('pera', 'morango', 'uva','abacaxi','banana')
frutas.sort
print(frutas)
frutas[2]= 'limão'
print(frutas)





#EXERCICIOS

