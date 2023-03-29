from Mundo import Mundo
from Direcional import Direcional

class Radar:

    def __init__(self, agente_x, agente_y, mundo):
        self.__mundo = mundo # trocar Mundo() para mundo
        # self.__direcao = Direcional()
        self.moverRadar(agente_x, agente_y)

    def moverRadar(self, agente_x, agente_y):
  
        self.superiorEsquerdo = [
            [[agente_y - 3, agente_x - 3], [agente_y - 3, agente_x - 2], [agente_y - 3, agente_x - 1]],
            [[agente_y - 2, agente_x - 3]],
            [[agente_y - 1, agente_x - 3]],
        ]

        self.superiorDireito = [
            [[agente_y - 3, agente_x + 3], [agente_y - 3, agente_x + 2], [agente_y - 3, agente_x + 1]],
                                                                        [[agente_y - 2, agente_x + 3]],
                                                                        [[agente_y - 1, agente_x + 3]],
        ]

        self.inferiorEsquerdo = [
            [[agente_y + 1, agente_x - 3]],
            [[agente_y + 2, agente_x - 3]],
            [[agente_y + 3, agente_x - 3], [agente_y + 3, agente_x - 2], [agente_y + 3, agente_x - 1]]
        ]

        self.inferiorDireito = [
                                                                        [[agente_y + 1, agente_x + 3]],
                                                                        [[agente_y + 2, agente_x + 3]],
            [[agente_y + 3, agente_x + 3], [agente_y + 3, agente_x + 2], [agente_y + 3, agente_x + 1]]
        ]

        self.__verificarEsferas()


    def __verificarEsferas(self):

        for esfera in self.__mundo.coordenadasDasEsferas():

            if esfera[0] in self.superiorEsquerdo[0][0]:
                print(esfera) 
            
            # elif localizacao[y][x] in self.superiorEsquerdo:
            #     print('superiorDireito') 
            
            # elif localizacao[y][x] in self.inferiorDireito:
            #     print('superiorDireito') 
            
            # elif localizacao[y][x] in self.inferiorEsquerdo:
            #     print('superiorDireito') 

                 