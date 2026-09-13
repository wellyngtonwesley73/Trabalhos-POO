times = (
    "Flamengo", "Palmeiras", "Athletico-PR", "Fluminense", "Bahia",
    "Cruzeiro", "Atlético-MG", "Red Bull Bragantino", "São Paulo",
    "Vitória", "Corinthians", "Botafogo", "Grêmio", "Vasco", "Internacional",
    "Chapecoense", "Juventude", "Fortaleza", "Criciúma", "Cuiabá"



)


print("A) Os 5 primeiros colocados:")
print(times[0:5])
print("-" * 40)


print("B) Os últimos 4 colocados:")
print(times[-4:])
print("-" * 40)


print("C) Times em ordem alfabética:")
print(sorted(times))
print("-" * 40)


posicao_chape = times.index("Chapecoense") + 1
print(f"D) O time da Chapecoense está na {posicao_chape}ª posição.")