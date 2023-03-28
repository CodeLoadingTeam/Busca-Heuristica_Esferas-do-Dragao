from Mundo import Mundo
from Direcional import Direcional

class Radar:

    def __init__(self, agente_x, agente_y, mundo):
        self.__mundo = Mundo() # trocar para mundo
        self.__direcao = Direcional()
        self.moverRadar(agente_x, agente_y)

    def moverRadar(self, agente_x, agente_y):
        self.x0 = agente_x - 3
        self.y0 = agente_y - 3
        self.x0 = agente_x + 3
        self.y0 = agente_y + 3

        self.__verificarEsferas()


    def __verificarEsferas(self):
        # direcoes = self.__direcao.direcao
        
        # for direcao in direcoes:

        #     match direcao:
        #         case self.__direcao.ESQUERDA:
                    
        #             self.x0

        #         case self.__direcao.DIREITA:
        #             self.x1

        #         case self.__direcao.CIMA:
        #             self.y0

        #         case self.__direcao.BAIXO:
        #             self.y0

        for esfera in self.__mundo.coordenadasDasEsferas():
            x, y = 1, 0

            if esfera[x] == self.x0 and self.x0

