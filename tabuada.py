numero = int(input('Informe um número: '))
lista_tabuada = [1,2,3,4,5,6,7,8,9,10]

for tab in lista_tabuada:
    resultado = numero * tab
    print(f'{numero} * {tab} = {resultado}')
