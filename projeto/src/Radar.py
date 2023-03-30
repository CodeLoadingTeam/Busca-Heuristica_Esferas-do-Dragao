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

        # self.superiorDireito = [
        #     [[agente_y - 3, agente_x + 3], [agente_y - 3, agente_x + 2], [agente_y - 3, agente_x + 1]],
        #                                                                 [[agente_y - 2, agente_x + 3]],
        #                                                                 [[agente_y - 1, agente_x + 3]],
        # ]

        # self.inferiorEsquerdo = [
        #     [[agente_y + 1, agente_x - 3]],
        #     [[agente_y + 2, agente_x - 3]],
        #     [[agente_y + 3, agente_x - 3], [agente_y + 3, agente_x - 2], [agente_y + 3, agente_x - 1]]
        # ]

        # self.inferiorDireito = [
        #                                                                 [[agente_y + 1, agente_x + 3]],
        #                                                                 [[agente_y + 2, agente_x + 3]],
        #     [[agente_y + 3, agente_x + 3], [agente_y + 3, agente_x + 2], [agente_y + 3, agente_x + 1]]
        # ]

        self.coordenadas = {
            'y': [agente_y - 3, agente_y - 2, agente_y - 1, agente_y + 1, agente_y + 2, agente_y + 3],
            'x': [agente_x - 3, agente_x - 2, agente_x - 1, agente_x + 1, agente_x + 2, agente_x + 3]
        }

        self.__verificarEsferas()


    def __verificarEsferas(self):

        for esfera in self.__mundo.coordenadasDasEsferas():
            
            # if esfera['y'] in self.superiorEsquerdo[0][0]:
            if esfera['y'] in self.coordenadas['y'] and esfera['x'] in self.coordenadas['x']:
                print(esfera['valor']) 
            
            # elif localizacao[y][x] in self.superiorEsquerdo:
            #     print('superiorDireito') 
            
            # elif localizacao[y][x] in self.inferiorDireito:
            #     print('superiorDireito') 
            
            # elif localizacao[y][x] in self.inferiorEsquerdo:
            #     print('superiorDireito') 

                 