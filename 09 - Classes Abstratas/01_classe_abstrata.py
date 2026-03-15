from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV ...")
        print("Desligada")

    def desligar(self):
        print("Desligando TV......")
        print("Desligada")

    @property
    def marca(self):
        return "Philco"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar condicionado.....")
        print("Ligado!!")

    def desligar(self):
        print("Desligando ar condicionado.....")
        print("Desligado!!")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
#