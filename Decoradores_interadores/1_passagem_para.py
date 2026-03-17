def mensagem(nome):
    print("Ecexutando nome")
    return f'oi {nome}'

def mensagem_longa(nome):
    print('executando menssagem longa')
    return f'olá tudo bem com voce {nome}?'

def executar(funcao, nome):
    print ("executando executar")
    return funcao(nome)

executar(mensagem, "joao")
executar(mensagem_longa, "joao")


##14,20