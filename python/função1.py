a = 4
b = 5
s = a+b
print(f' Os valores digitados foram: {a} e {b} = {s}')

#função utilizada para boas práticas e programação limpa e organizada


#1 - identificar programa principal (ação)
#2 criar variavel e parametrizar(parametros)
#def___( ):


def soma(a,b):
    s=a+b
    print(f'{a}+{b}={s}')


soma(4,9)
soma(8,9)
soma(2,1)



#com modularização

def lerintpositivo(msg):


    num=0
    while num<=0:
        try:
            num=int(input(msg))
        except:
            print('Valor inválido. Tente novamente')
    return num

idade=lerintpositivo()
