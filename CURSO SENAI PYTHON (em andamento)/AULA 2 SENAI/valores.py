valor_pi=3.14
print(valor_pi)

valor_pi=input('Digite o novo valor de valor_pi')
print(valor_pi)


nome=str(input('digite seu nome')) #string = texto. Há tbm a string literal para números
idade=int(input('digite sua idade')) #inteiro = 21
peso=float(input('digite seu peso')) #float = 68.5 
altura=float(input('digite sua altura')) # float = 1.75

print(nome)
print(idade)
print(peso)
print(type(peso))
print(f'Você é o {nome}e tem {idade} de idade? Altura de {altura} e peso de {peso}kg, correto?')