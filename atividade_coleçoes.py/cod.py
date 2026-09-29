import minhas_funcoes

def formatar_saida(lista):
    """
    Converte os elementos de uma lista para texto separado por espaço.
    """
    texto = ""
    for item in lista:
        texto += str(item) + " "
    return texto.strip()

def main():
    entrada_a = input("Digite os valores da primeira coleção: ")
    entrada_b = input("Digite os valores da segunda coleção: ")

    a = []
    for x in entrada_a.split():
        a.append(int(x))

    b = []
    for x in entrada_b.split():
        b.append(int(x))

    print("\nResultados:")

    distintos_a = minhas_funcoes.valores_distintos(a)
    distintos_b = minhas_funcoes.valores_distintos(b)
    print("1. Valores únicos da primeira coleção:", formatar_saida(distintos_a))
    print("2. Valores únicos da segunda coleção:", formatar_saida(distintos_b))

    res_a_b = minhas_funcoes.diferenca_a_b(a, b)
    print("3. Presentes na primeira, mas não na segunda:", formatar_saida(res_a_b))

    res_b_a = minhas_funcoes.diferenca_b_a(a, b)
    print("4. Presentes na segunda, mas não na primeira:", formatar_saida(res_b_a))

    res_uniao = minhas_funcoes.uniao(a, b)
    print("5. Presentes em ao menos uma das coleções:", formatar_saida(res_uniao))

    res_intersecao = minhas_funcoes.intersecao(a, b)
    print("6. Presentes em ambas as coleções:", formatar_saida(res_intersecao))

    res_dif_sim = minhas_funcoes.diferenca_simetrica(a, b)
    print("7. Presentes em uma coleção, mas não na outra:", formatar_saida(res_dif_sim))

if __name__ == "__main__":
    main()