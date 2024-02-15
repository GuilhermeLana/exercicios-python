x = int(input('Informe a coordenada x: '))
y = int(input('Informe a coordenada y: '))

if x > 0 and y > 0:
    print('As coordenadas correspondem ao Primeiro Quadrante')
elif x < 0 and y > 0:
    print('As coordenadas correspondem ao Segundo Quadrante')
elif x < 0 and y < 0:
    print('As coordenadas correspondem ao Terceiro Quadrante')
elif x > 0 and y < 0:
    print('As coordenadas correspondem ao Quarto Quadrante')
else:
    print('As coordenadas correspondem ao eixo')