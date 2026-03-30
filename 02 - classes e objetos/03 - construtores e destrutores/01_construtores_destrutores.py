class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe ....")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def _del_(self):
        print("Removendo a instancia da classe")

    def falar(self):
        print("auu")

def criar_cachorro():
    c = Cachorro("Zeus", "Preto e branco", False)
    print(c.nome)

    

c = Cachorro("Chappie", "amarelo")

c.falar()