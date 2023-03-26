import random

class Direcional:

    def __init__(self):
        self.sorteador = random
        self.ESQUERDA = 'esquerda'
        self.DIREITA = 'direita'
        self.CIMA = 'cima'
        self.BAIXO = 'baixo'

        self.direcao = [
            self.ESQUERDA, 
            self.DIREITA, 
            self.CIMA, 
            self.BAIXO
        ]


    def proximoPasso(self):
        return self.direcao[self.sorteador.randrange(4)]
