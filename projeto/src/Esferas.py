import random

class Esferas:

    localizacoes = []

    def __init__(self):
        self.sorteador = random

        self.ESFERA1 = 'Esfera 1'
        self.ESFERA2 = 'Esfera 2'
        self.ESFERA3 = 'Esfera 3'
        self.ESFERA4 = 'Esfera 4'
        self.ESFERA5 = 'Esfera 5'
        self.ESFERA6 = 'Esfera 6'
        self.ESFERA7 = 'Esfera 7'
    
        self.esferas = {	
            self.ESFERA1,
            self.ESFERA2,
            self.ESFERA3,
            self.ESFERA4,
            self.ESFERA5,
            self.ESFERA6,
            self.ESFERA7
        }
        
        self.__gerarLocalizacoes()


    def __gerarLocalizacoes(self):

        for esfera in self.esferas:
            self.localizacoes.append(
                [
                    self.__sortearY(),
                    self.__sortearX(),
                    esfera
                ])


    def __sortearY(self):
        self.__sortearPosicaoNoEixo()


    def __sortearX(self):
        self.__sortearPosicaoNoEixo()


    def __sortearPosicaoNoEixo(self):
        return self.sorteador.randrange(42)
