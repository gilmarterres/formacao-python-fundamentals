while True:
    numero = int(input("Informe número:"))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)

#########################3
for numero in range(100):

    if numero % 2 == 0:
        continue

    if numero > 10 and numero < 20:
        continue

    print(numero, end=" ")