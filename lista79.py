numeros = []

while True:
    n = int(input('Digite um valor: '))
    

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    
    resposta = input('Quer continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break


numeros.sort()

print('=-' * 30)
print(f'Você digitou os valores: {numeros}')