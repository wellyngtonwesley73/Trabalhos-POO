num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

for v in num:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('=-' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')