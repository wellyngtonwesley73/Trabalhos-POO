valores = list()
for cont in range(0,5):
    valores.append(int(input('digite um valor:')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista.')


