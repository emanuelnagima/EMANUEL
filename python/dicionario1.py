
amigo2 = {}
amigo2 ['nome']='emanuel'
amigo2 ['idade'] = '21'
amigo2 ['cidade'] = 'santo anastacio'
amigo2 ['altura'] = '1,74'
amigo2 ['estado civil'] = 'solteiro'
print(amigo2)  
print(f'nome: {amigo2["nome"]}')





for y, c in amigo2.items():
    print(f'{y} = {c}')



#outra maneira de fazer

pessoa={'nome':'emanuel', 'idade': '21','sexo': 'masculino'
}
print(pessoa)
print(f'nome: {pessoa["nome"]} , idade: {pessoa["idade"]} e sexo: {pessoa["sexo"]}')

print(pessoa.items())
print(pessoa.keys())
print(pessoa.values())
for v, k in pessoa.items():
    print(f'{v} = {k}')