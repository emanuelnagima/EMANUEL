#Crie um algoritmo, que converte Reais em Dólar. Peça ao usuário o valor que ele deseja converter para Dólar. Exemplo: Digitei 10 reais, calcule quantos dólares eu tenho a partir dos 10 reais. Valor atual do Dólar: $5,73

print('Iremos realizar um conversão de real para dolar')
n1=float(input('digite um valor'))

cal=float(n1/5.68)
print(f'O valor de {n1}R$ em dolar será de: \n{round(cal,2)}') #(\n)QUEBRA LINHA 

