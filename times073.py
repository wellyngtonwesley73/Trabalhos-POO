qtde = int(input("Digite a quantidade de times: "))
times = []
for i in range(qtde):
    time = input(f"Digite o nome do {i + 1}º time: ")
    times.append(time)


print("Times:")
print(times)

posicao = int(input("Digite a posicao primeiros colocados: "))
print(f"A) Os {posicao} colocados:")
print(times[:posicao])
print("-" * 40)


posicao = int(input("Digite a posicao dos ultimos colocados:"))

print("B) Os últimos {posicao} colocados:")
# forma mais geral
i = len(times) - posicao
print(times[i:])

#print(times[-posicao:]) # pythonico

print("-" * 40)

print("C) Times em ordem alfabética:")
print(sorted(times))
print("-" * 40)


time = input("Digite o nome do time para saber sua posição: ")
if time in times:
    posicao_chape = times.index(time) + 1
    print(f"D) O time {time} está na {posicao_chape}ª posição.")
else:
    print(f"D) O time {time} não está no campeonato.")

