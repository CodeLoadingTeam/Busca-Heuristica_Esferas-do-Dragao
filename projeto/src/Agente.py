from Mundo import Mundo

class Agente():

    def __init__(self):
        self.atualizarLocalizacao(3, 2)
        self.mundo = Mundo()

    def atualizarLocalizacao(self, x, y):
        self.x = x
        self.y = y

    def armazenarBiomaAtual(self, x, y):
        global mundo
        self.bioma = self.mundo.usarMatriz()[y][x]
