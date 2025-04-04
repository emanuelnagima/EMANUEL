print('OLÁ AMIGO!')
nome = input('QUAL O SEU NOME?')
print('SEJA MUITO BEM VINDO', nome)
N1 = float(input('DIGITE SUA SUA NOTA1'))
N2 = float(input('DIGITE SUA NOTA2 AGORA'))
print('{} SUAS NOTAS ENTÃO FORAM {} E {} CORRETO?'.format(nome, N1, N2))


print('IREMOS REALIZAR SUA MÉDIA DAS NOTAS, OK?{}'.format(nome))
media=(N1+N2)/2
print('SUA MEDIA FOI DE: {}'.format(media))
if media>= 6:
    print('Parabêns, vc foi aprovado')
else:
    print('Que triste, vc foi reprovado')


    #print formatado (f'{nome})
print(f'Voce tirou {N1} na nota1 e {N2} na nota 2, realizando a media aritmética e calculando, {nome}, você tirou {media}')
    


