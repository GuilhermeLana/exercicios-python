pessoas = [{'nome':'Guilherme','idade':30,'cidade':'Diadema'},
          {'nome':'Julia','idade':28,'cidade':'Blumenau'}]

def listarPessoas():
    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = f'{pessoa['idade']} anos'
        cidade = pessoa['cidade']
        print(f'{nome.ljust(20)} | {idade.ljust(20)} | {cidade}')
    print()

listarPessoas()

for pessoa in pessoas:
    if pessoa['nome'] == 'Guilherme':
        pessoa['idade'] = 31
        pessoa.update({'profissao':'DEV'})
    print(pessoa)

print('Alterada idade do Guilherme\n')
listarPessoas()

for pessoa in pessoas:
    if pessoa['nome'] == 'Julia':
        pessoas.remove(pessoa)


print('Removida Julia\n')
listarPessoas()

