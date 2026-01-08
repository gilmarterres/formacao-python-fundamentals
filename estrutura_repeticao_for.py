# texto = input("Informe um texto!")
texto = ""
VOGAIS = "AEIOU"

for l in texto:
    if l.upper() in VOGAIS:
        print(l.upper(), end="")
else:
    print() #adiciona quebea de linha
    #print("Executa no final")


for numero in range(0, 51, 5):
    print(numero, end="-")