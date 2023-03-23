from Mundo import Mundo
from Direcional import Direcional

class Agente():

    def __init__(self):
        self.x = 3,
        self.y = 2,

        self.mundo = Mundo()
        self.__direcao = Direcional()


    def deslocar(self):

        match self.__direcao.proximoPasso():
           case self.__direcao.ESQUERDA:
               self.x = self.x + -1

           case self.__direcao.DIREITA:
               self.x += 1

           case self.__direcao.CIMA:
               self.y += -1

           case self.__direcao.BAIXO:
               self.y += 1

        self.__armazenarBiomaAtual()
        self.mundo.usarMatriz[self.y][self.x]

    def __armazenarBiomaAtual(self):
        self.bioma = self.mundo.usarMatriz()[self.y][self.x]

    def mostrarMundo(self):
        return self.mundo.printarMatriz()
