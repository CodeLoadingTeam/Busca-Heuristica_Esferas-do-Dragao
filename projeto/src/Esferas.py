import random

class Esferas:
    localizacoes = []

    def __init__ (self):
        self.sorteador = random

        self.ESFERA1 ='Esfera 1'
        self.ESFERA2 ='Esfera 2'
        self.ESFERA3 ='Esfera 3'
        self.ESFERA4 ='Esfera 4'
        self.ESFERA5 ='Esfera 5'
        self.ESFERA6 ='Esfera 6'
        self.ESFERA7 ='Esfera 7'
    
        self.esferas = {	
            self.ESFERA1,
            self.ESFERA2,
            self.ESFERA3,
            self.ESFERA4,
            self.ESFERA5,
            self.ESFERA6,
            self.ESFERA7
        }
        
        self.gerarLocalizacoes()

    def gerarLocalizacoes (self):
        for _ in self.esferas:
            self.localizacoes.append(
                [
                    self.eixo(),
                    self.eixo(),
                    True
                ])


    def eixo (self):
        return self.sorteador.randrange(42)

# esfera = Esferas()
# print(esfera.localizacoes)