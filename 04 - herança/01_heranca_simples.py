class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass


moto = Motocicleta("preta", "abc-123", 2)
moto.ligar_motor()

carro = Carro("branco", "anu1614", 4)
carro.ligar_motor()

caminhao = Caminhao("azul", "gdf8765", 16)


##6.44