from Mundo import Mundo

class Radar:
    
    def __init__(self, mundo):
        self.__mundo = mundo

        self.moverRadar()


    def moverRadar(self, agente_x, agente_y):
        self.x0 = agente_x - 3
        self.y0 = agente_y - 3
        self.x0 = agente_x + 3
        self.y0 = agente_y + 3

        self.__verificarEsferas()


    def __verificarEsferas(self):
        
        for y0 in range(self.y0, self.y1):
            for radar_x0 in range(self.x0, self.x1):

                


radar = Radar()

[19 20 21 22 23 24 25]