from Mundo import Mundo
from Direcional import Direcional
from Radar import Radar

class Agente:

    x = 19
    y = 19
    inicializacao = True


    def __init__(self):
        self.__mundo = Mundo()
        self.__direcao = Direcional()
        self.radar = Radar(self.x, self.y, self.__mundo)


    def deslocar(self):
        
        if self.inicializacao != True:
            self.__restaurarLocalizacaoAnterior()
            self.__proximoPasso()

        else:
            self.inicializacao = False

        self.localizacao = [self.x, self.y]
        self.__armazenarBiomaAtual()
        self.__mundo.atualizarMatriz(self.x, self.y, '⌘')
        self.radar.moverRadar(self.x, self.y)


    def __armazenarBiomaAtual(self):
        self.__bioma = self.__mundo.usarMatriz()[self.y][self.x]


    def __restaurarLocalizacaoAnterior(self):
        x = self.localizacao[0]
        y = self.localizacao[1]
        self.__mundo.usarMatriz()[y][x] = self.__bioma


    def __proximoPasso(self):
        
        while True:
            passo_x, passo_y = self.x, self.y
            extremidadeInicial, extremidadeFinal = 0, self.__mundo.dimensaoDaMatriz()

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
        return self.__mundo.printarMatriz()


a = Agente()
# print(a.radar.superiorEsquerdo[0][0])
a.deslocar()
# print(a.radar.superiorEsquerdo)
# print(a.radar.superiorDireito)
# print(a.radar.inferiorEsquerdo)
# print(a.radar.inferiorDireito)
