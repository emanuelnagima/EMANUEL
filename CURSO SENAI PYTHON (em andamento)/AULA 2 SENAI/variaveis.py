#Comentario em python é #

#tipos de variaveis

idade = 21 
peso = 85.40
chuva = False #boleanos
nome = ('emanuel')
sexo = ('Masculino')

# o type descreve o tipo de variavel que é 
print(type(nome))

#Primeira forma
print('meu nome é:', nome)

#Segunda forma (melhor forma) com "F"de "formatado"
print(f"Meu nome é: {nome}")

#Concatenação, junção de variaveis. EMANUEL, NÃO USE ASSIM
print("Meu nome é:",nome,"e a idade é", idade)

#Concatenação, junção de variaveis com "F"de "formatado"
print(f'Meu nome é {nome}, tenho {peso}kg e tenho {idade} anos de idade. Sou do sexo {sexo}')
print(f'Hoje vai chover: {chuva}')


