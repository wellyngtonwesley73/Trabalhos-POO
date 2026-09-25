from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))

ano_atual = datetime.now().year
dados['idade'] = ano_atual - nasc

dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    
    anos_contribuicao = dados['contratacao'] - nasc
    dados['aposentadoria'] = anos_contribuicao + 35

print('-=' * 15)

for k, v in dados.items():
    if k == 'salario':
        print(f'  - {k} tem o valor R$ {v:.2f}')
    else:
        print(f'  - {k} tem o valor {v}')