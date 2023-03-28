from Agente import Agente

class Radar:

    def __init__(self):
        self.__agente = Agente()

        self.moverRadar()


    def moverRadar(self):
        self.x0 = self.__agente.x - 3
        self.y0 = self.__agente.y - 3
        self.x0 = self.__agente.x + 3
        self.y0 = self.__agente.y + 3

        self.__verificarEsferas()


    def __verificarEsferas():

        for radar_y0 in range(y, y-3, -1):
            for radar_x0 in range(x, x-3, -1):
                


radar = Radar()

[19 20 21 22 23 24 25]