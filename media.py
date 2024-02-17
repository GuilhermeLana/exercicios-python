lista_numeros = [5,10,15]
soma = 0

for num in lista_numeros:
    soma += num;

try:
    media = soma / len(lista_numeros)
    print(f'A média dos numeros é: {media}')
except ZeroDivisionError:
    print('A lista não pode estar vazia')
