def obter_unicos(colecao):
    """Retorna os valores distintos de uma coleção."""
    return sorted(list(set(colecao)))

def diferenca_a_b(a, b):
    """Retorna os elementos presentes em A, mas não em B."""
    return sorted(list(set(a) - set(b)))

def diferenca_b_a(a, b):
    """Retorna os elementos presentes em B, mas não em A."""
    return sorted(list(set(b) - set(a)))

def uniao(a, b):
    """Retorna os elementos presentes em A ou em B."""
    return sorted(list(set(a) | set(b)))

def intersecao(a, b):
    """Retorna os elementos presentes em A e em B."""
    return sorted(list(set(a) & set(b)))

def diferenca_simetrica(a, b):
    """Retorna os elementos presentes em exatamente uma das coleções."""
    return sorted(list(set(a) ^ set(b)))