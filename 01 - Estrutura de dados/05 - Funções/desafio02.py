def elementos_comuns(lista1, lista2):
    # 1. Convertemos as listas de strings para listas de inteiros usando map
    # 2. Convertemos imediatamente para conjuntos (set) para remover duplicatas e permitir operações matemáticas
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    
    # 3. A função intersection retorna apenas o que existe em ambos
    # 4. Convertemos de volta para lista, pois o desafio pede uma lista como saída
    return list(set1.intersection(set2))

# Leitura das listas (Entrada de dados)
lista1 = input().split()
lista2 = input().split()

# Verifica se todos os elementos das listas são numéricos (dígitos)
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")

