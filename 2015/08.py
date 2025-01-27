vagoes = []
n = 1

while True:
    peso = int(input())
    if peso == 0:
        break
    vagoes.append((peso, n))
    n += 1

# Ordenar por peso (decrescente) e por número do vagão (decrescente) em caso de empate
vagoes.sort(key=lambda x: (-x[0], x[1]))

# Imprimir os números dos vagões ordenados
for _,numero in vagoes:
    print(numero)