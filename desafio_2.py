def verificador_ano_bissexto():
    ano = int(input())
    if (ano % 4 == 0) and (ano % 100 != 0):
        print("SIM")
    elif ano % 400 == 0:
        print("SIM")
    else:
        print("NÃO")

# TOD: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:
# REGRA:

# Um ano é bissexto se:
# 1. Ele é divisível por 4 e não é divisível por 100.
# 2. Ou ele é divisível por 400.

verificador_ano_bissexto()