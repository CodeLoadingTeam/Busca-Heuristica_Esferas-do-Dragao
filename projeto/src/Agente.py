from Mundo import Mundo
from Direcional import Direcional

class Agente():

    x = 19
    y = 19
    inicializacao = True


    def __init__(self):

        self.__mundo = Mundo()
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

        self.localizacao = [self.x, self.y]
        self.__armazenarBiomaAtual()
        self.__mundo.atualizarMatriz(self.x, self.y, '⌘')


    def __armazenarBiomaAtual(self):
        self.__bioma = self.__mundo.usarMatriz()[self.y][self.x]


    def __restaurarLocalizacaoAnterior(self):
        x = self.localizacao[0]
        y = self.localizacao[1]
        self.__mundo.usarMatriz()[y][x] = self.__bioma


    def mostrarMundo(self):
        return self.__mundo.printarMatriz()
