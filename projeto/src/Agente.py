from Mundo import Mundo
from Direcional import Direcional
from Radar import Radar

class Agente:

    x = 19
    y = 19
    inicializacao = True


    def __init__(self):
        self.mundo = Mundo()
        self.__direcao = Direcional()
        self.radar = Radar(self.x, self.y, self.mundo)


    def deslocar(self):
        
        if self.inicializacao != True:
            self.__restaurarLocalizacaoAnterior()
            self.__proximoPasso()
            self.radar.moverRadar(self.x, self.y)

        else:
            self.inicializacao = False

        self.localizacao = [self.x, self.y]
        self.__armazenarBiomaAtual()
        self.mundo.atualizarMatriz(self.x, self.y, '⌘')
        


    def __armazenarBiomaAtual(self):
        self.__bioma = self.mundo.usarMatriz()[self.y][self.x]


    def __restaurarLocalizacaoAnterior(self):
        x = self.localizacao[0]
        y = self.localizacao[1]
        self.mundo.usarMatriz()[y][x] = self.__bioma


    def __proximoPasso(self):
        
        while True:
            passo_x, passo_y = self.x, self.y
            extremidadeInicial, extremidadeFinal = 0, self.mundo.dimensaoDaMatriz()

            direcaoSorteada = self.__direcao.escolherPasso()

            match direcaoSorteada:
                case self.__direcao.ESQUERDA:
                    passo_x += -1

                case self.__direcao.DIREITA:
                    passo_x += 1

                case self.__direcao.CIMA:
                    passo_y += -1

                case self.__direcao.BAIXO:
                    passo_y += 1

            if (passo_x > extremidadeInicial and passo_x < extremidadeFinal) and (passo_y > extremidadeInicial and passo_y < extremidadeFinal):
                self.x = passo_x
                self.y = passo_y
                break


    def mostrarMundo(self):
        return self.mundo.printarMatriz()


a = Agente()
a.deslocar()
