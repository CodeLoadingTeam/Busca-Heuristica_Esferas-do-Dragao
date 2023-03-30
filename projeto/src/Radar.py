# from Mundo import Mundo

class Radar:

    def __init__(self, agente_x, agente_y, mundo):
        self.__mundo = mundo
        self.moverRadar(agente_x, agente_y)

    def moverRadar(self, agente_x, agente_y):

        self.coordenadas = {
            'y': [agente_y - 3, agente_y - 2, agente_y - 1, agente_y + 1, agente_y + 2, agente_y + 3],
            'x': [agente_x - 3, agente_x - 2, agente_x - 1, agente_x + 1, agente_x + 2, agente_x + 3]
        }

        self.__verificarEsferas()


    def __verificarEsferas(self):

        for esfera in self.__mundo.coordenadasDasEsferas():

            if esfera['y'] in self.coordenadas['y'] and esfera['x'] in self.coordenadas['x']:
                
                self.__mundo.usarMatriz()[esfera['y']][esfera['x']] = esfera['valor']
                print(esfera['valor'])
