def principal():
    print('executando a funcao principal')

    def funcao_interna():
        print('executando a funcao interna')

    def funcao2():
        print('executando a funcao interna 2')

    funcao_interna()
    funcao2()

principal()