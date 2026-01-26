class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plin plin.....!")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrunnnnn....")

    def get_cor(self):
        return self.cor

b1 = Bicicleta("vermelha", "caloi", 2022, 640)

b1.buzinar()
b1.correr()
b1.parar()

print(b1.ano, b1.cor, b1.modelo)

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar()
print(b2.get_cor())


# parou em 15mim 