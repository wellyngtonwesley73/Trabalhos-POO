valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('=-' * 30)

print(f'A) Você digitou {len(valores)} elementos.')

valores.sort(reverse=True)
print(f'B) Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print('C) O valor 5 faz parte da lista!')
else:
    print('C) O valor 5 não foi encontrado na lista!')