def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo antes de executar")

    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo")


##ola_mundo = meu_decorador(ola_mundo)
ola_mundo()





##26min decoradores parte 1