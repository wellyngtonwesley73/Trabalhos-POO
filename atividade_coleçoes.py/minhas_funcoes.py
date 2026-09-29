def ordenar_lista(lista):
    """
    Ordena uma lista numérica em ordem crescente sem utilizar sorted().
    Usa o algoritmo simples de Ordenação por Seleção (Selection Sort).
    """
    lista_copia = lista.copy()
    n = len(lista_copia)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista_copia[j] < lista_copia[min_idx]:
                min_idx = j
        lista_copia[i], lista_copia[min_idx] = lista_copia[min_idx], lista_copia[i]
    return lista_copia

def valores_distintos(colecao):
    unicos = []
    for item in colecao:
        if item not in unicos:
            unicos.append(item)
    return ordenar_lista(unicos)

def diferenca_a_b(a, b):
    resultado = []
    for item in a:
        if item not in b and item not in resultado:
            resultado.append(item)
    return ordenar_lista(resultado)

def diferenca_b_a(a, b):
    resultado = []
    for item in b:
        if item not in a and item not in resultado:
            resultado.append(item)
    return ordenar_lista(resultado)

def uniao(a, b):
    resultado = []
    for item in a:
        if item not in resultado:
            resultado.append(item)
    for item in b:
        if item not in resultado:
            resultado.append(item)
    return ordenar_lista(resultado)

def intersecao(a, b):
    resultado = []
    for item in a:
        if item in b and item not in resultado:
            resultado.append(item)
    return ordenar_lista(resultado)

def diferenca_simetrica(a, b):
    resultado = []
    for item in a:
        if item not in b and item not in resultado:
            resultado.append(item)
    for item in b:
        if item not in a and item not in resultado:
            resultado.append(item)
    return ordenar_lista(resultado)