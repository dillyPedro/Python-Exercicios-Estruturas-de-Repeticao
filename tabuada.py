numero = int(input('Digite o numero para a tabuada: '))

contador = 1

for contador in range(1, 11):
    tabuada = numero * contador
    print(f'{numero} * {contador} = {tabuada}')
    contador += 1
