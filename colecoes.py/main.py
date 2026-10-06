import operacoes

def main():
    # Leitura das duas coleções de valores
    entrada_a = input("Digite os valores da primeira coleção: ")
    entrada_b = input("Digite os valores da segunda coleção: ")
    
    # Converte a entrada de texto para listas de inteiros
    colecao_a = list(map(int, entrada_a.split()))
    colecao_b = list(map(int, entrada_b.split()))
    
    print("\nResultados:\n")
    
    # 1. Valores distintos de A e B
    a_unicos = operacoes.obter_unicos(colecao_a)
    b_unicos = operacoes.obter_unicos(colecao_b)
    print(f"1. Valores únicos da primeira coleção: {' '.join(map(str, a_unicos))}")
    print(f"2. Valores únicos da segunda coleção: {' '.join(map(str, b_unicos))}")
    
    # 3. Presentes na primeira, mas não na segunda (A - B)
    dif_ab = operacoes.diferenca_a_b(colecao_a, colecao_b)
    print(f"3. Presentes na primeira, mas não na segunda: {' '.join(map(str, dif_ab))}")
    
    # 4. Presentes na segunda, mas não na primeira (B - A)
    dif_ba = operacoes.diferenca_b_a(colecao_a, colecao_b)
    print(f"4. Presentes na segunda, mas não na primeira: {' '.join(map(str, dif_ba))}")
    
    # 5. União (A | B)
    uni = operacoes.uniao(colecao_a, colecao_b)
    print(f"5. Presentes em ao menos uma das coleções: {' '.join(map(str, uni))}")
    
    # 6. Interseção (A & B)
    inter = operacoes.intersecao(colecao_a, colecao_b)
    print(f"6. Presentes em ambas as coleções: {' '.join(map(str, inter))}")
    
    # 7. Diferença Simétrica (A ^ B)
    dif_sim = operacoes.diferenca_simetrica(colecao_a, colecao_b)
    print(f"7. Presentes em uma coleção, mas não na outra: {' '.join(map(str, dif_sim))}")

if __name__ == "__main__":
    main()