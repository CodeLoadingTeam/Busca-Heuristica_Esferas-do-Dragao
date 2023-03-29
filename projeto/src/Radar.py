from Mundo import Mundo
from Direcional import Direcional

class Radar:

    def __init__(self, agente_x, agente_y, mundo):
        self.__mundo = Mundo() # trocar Mundo() para mundo
        # self.__direcao = Direcional()
        self.moverRadar(agente_x, agente_y)

    def moverRadar(self, agente_x, agente_y):
  
        self.superiorEsquerdo = [
            [[agente_x - 3, agente_y - 3], [agente_x - 2, agente_y - 3], [agente_x - 1, agente_y - 3]],
            [[agente_x - 3, agente_y - 2]],
            [[agente_x - 3, agente_y - 1]],
        ]

        self.superiorDireito = [
            [[agente_x + 3, agente_y - 3], [agente_x + 2, agente_y - 3], [agente_x + 1, agente_y - 3]],
                                                                        [[agente_x + 3, agente_y - 2]],
                                                                        [[agente_x + 3, agente_y - 1]],
        ]

        self.inferiorEsquerdo = [
            [[agente_x - 3, agente_y + 1]],
            [[agente_x - 3, agente_y + 2]],
            [[agente_x - 3, agente_y + 3], [agente_x - 2, agente_y + 3], [agente_x - 1, agente_y + 3]]
        ]

        self.inferiorDireito = [
                                                                        [[agente_x + 3, agente_y + 1]],
                                                                        [[agente_x + 3, agente_y + 2]],
            [[agente_x + 3, agente_y + 3], [agente_x + 2, agente_y + 3], [agente_x + 1, agente_y + 3]]
        ]

        self.__verificarEsferas()


    def __verificarEsferas(self):

        for localizacao in self.__mundo.coordenadasDasEsferas():

            if 16 in self.superiorEsquerdo[0][0]:
                print('superiorEsquerdo') 
            
            # elif localizacao[y][x] in self.superiorEsquerdo:
            #     print('superiorDireito') 
            
            # elif localizacao[y][x] in self.inferiorDireito:
            #     print('superiorDireito') 
            
            # elif localizacao[y][x] in self.inferiorEsquerdo:
            #     print('superiorDireito') 

                 