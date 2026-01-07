texto = input("Informe um texto!")

VOGAIS = "AEIOU"

for l in texto:
    if l.upper() in VOGAIS:
        print(l, end="")
else:
    print() #adiciona quebea de linha
    print("Executa no final")
