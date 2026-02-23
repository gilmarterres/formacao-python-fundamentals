from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV ...")
        print("Desligada")

    def desligar(self):
        print("Desligando TV......")
        print("Desligada")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar condicionado.....")
        print("Ligado!!")

controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleTV()
controle.ligar()
controle.desligar()
#
#10min