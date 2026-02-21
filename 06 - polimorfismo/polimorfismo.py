class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar..")

class Avestruz(Passaro):
    def voar(self):
        print("Aveztruz não pode voar...")



#exemplo ruim do uso da herança
class Aviao(Passaro):
    def voar(self):
        print("Aviao está decolando...")

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(Aviao())