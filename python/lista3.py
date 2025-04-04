#adicionar elemento na lista é .append('     ')
alunos = ['emanuel','marcos','luiz','jean','mariana','ana']
alunos.append('rogerio')
print(alunos)

#OUTRO METODO PARA ADICIONAR: variavel[]='   '
alunos[1]='ivone'

alunos.append('douglas')
alunos.append('alan')
alunos.append('bibiano')
print(alunos)

#para remover da lista é: r.remove('    ')
alunos.remove('luiz')
print(alunos)
print(sorted(alunos))

#remover pelo numero do elemento: pop
alunos.pop(3)
print(alunos)

#deixar mais organizado (estrtura de repetição)
for aluno in (alunos):
    print(aluno)



alunos = ['emanuel','marcos','luiz','jean','mariana','ana']
for c in range(len(alunos)):
    print(c,alunos)

#outros
print(max(alunos))
print(min(alunos))
print(len(alunos))



#Se caso eu tente remover alguem, não estando na lista: usar try e except

#alunos.remove('joão')
#print(alunos)

try:
    alunos.remove('joão')
except:
    print('O joão não foi encontrado!')