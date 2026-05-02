numero = int(input('Digite o numero que deseja verificar: '))
contador = 2

if(numero <= 1):
    print(f'O numero {numero} não é primo.')
else:
    numero_primo = True

for contador in range(2, numero):
    if(numero % contador == 0):
        numero_primo = False
        break

if(numero_primo):
    print(f'O numero {numero} é PRIMO!')
else:
    print(f'O numero {numero} NÃO é PRIMO!')
