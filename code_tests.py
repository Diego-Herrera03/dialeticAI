a =[[1], [2], [3], [4], [5], [6], [7], [8]]

pares = []
impares = []

for i in range(0, len(a)):
    if i % 2 == 0:
        pares.append(a[i])

    else:
        impares.append(a[i])

print(pares)

print(impares)
