#Crie um algoritmo, que pede ao usuário 4 notas do semestre da faculdade. Calcule e só mostre a média entre essas notas

n1=int(input('Digite a nota 1'))
n2=int(input('Digite a nota 2'))
n3=int(input('Digite a nota 3'))
n4=int(input('Digite a nota 4'))

media=(n1+n2+n3+n4)/4

print(f'Suas notas foram: {n1}, {n2}, {n3} e {n4}. Sua média foi de: {round(media, 2)}') # round para arredondar numero, 2 = casa decimal

#ou 
print(f'Suas notas foram: {n1}, {n2}, {n3} e {n4}. Sua média foi de: {media:.2f}') # round para arredondar numero

