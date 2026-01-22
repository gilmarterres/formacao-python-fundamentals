def contar_caracteres(string):
    # Inicializa um dicionário vazio
    contador = {}

    # TODO: Itere através de cada caractere na string string.
    for caractere in string:
        
        # TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
        if caractere in contador:
            # Se já estiver (se a chave existe), incremente o valor
            contador[caractere] += 1
        else:
            # Caso contrário (primeira vez que vemos essa letra), adicione com valor 1
            contador[caractere] = 1

    return contador

# O restante do código de leitura e print permanece igual
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)