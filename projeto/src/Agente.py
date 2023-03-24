from Mundo import Mundo
from Direcional import Direcional

class Agente():

    x = 3
    y = 2
    inicializacao = True

    def __init__(self):

        self.mundo = Mundo()
        self.__direcao = Direcional()


    def deslocar(self):
        
        if self.inicializacao != True:

            self.__restaurarLocalizacaoAnterior()

            match self.__direcao.proximoPasso():
               case self.__direcao.ESQUERDA:
                   self.x += -1

               case self.__direcao.DIREITA:
                   self.x += 1

               case self.__direcao.CIMA:
                   self.y += -1

               case self.__direcao.BAIXO:
                   self.y += 1

        else:
            self.inicializacao = False

        self.localizacaoAnterior = [self.x, self.y]
        self.__armazenarBiomaAtual()
        self.mundo.atualizarMatriz(self.x, self.y, '⌘')


    def __armazenarBiomaAtual(self):
        self.bioma = self.mundo.usarMatriz()[self.y][self.x]


    def __restaurarLocalizacaoAnterior(self):
        x = self.localizacaoAnterior[0]
        y = self.localizacaoAnterior[1]
        self.mundo.usarMatriz()[y][x] = self.bioma

    def mostrarMundo(self):
        return self.mundo.printarMatriz()
