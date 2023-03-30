import random
# from Mundo import Mundo
class Esferas:

    localizacoes = []

    def __init__(self, matrizMundo):
        self.__matrizMundo = matrizMundo
        self.sorteador = random

        self.ESFERA1 = '➀'
        self.ESFERA2 = '➁'
        self.ESFERA3 = '➂'
        self.ESFERA4 = '➃'
        self.ESFERA5 = '➄'
        self.ESFERA6 = '➅'
        self.ESFERA7 = '➆'
    
        self.esferas = [
            # self.ESFERA1,
            # self.ESFERA2,
            # self.ESFERA3,
            # self.ESFERA4,
            # self.ESFERA5,
            # self.ESFERA6,
            self.ESFERA7
        ]
        
        self.__gerarLocalizacoes()


    def __gerarLocalizacoes(self):

        for esfera in self.esferas:
            # x_sorteado, y_sorteado = self.__sortearPosicaoNoEixo(), self.__sortearPosicaoNoEixo()
            # self.localizacoes.append(
            #     [
            #        'y': y_sorteado,
            #        'x': x_sorteado,
            #        'valor': esfera,
            #        'bioma': self.__matrizMundo[y_sorteado][x_sorteado]
            #     ])

            x_sorteado, y_sorteado = 16, 22
            self.localizacoes.append(
                {
                    'y': y_sorteado,
                    'x': x_sorteado,
                    'valor': esfera,
                    'bioma': self.__matrizMundo[y_sorteado][x_sorteado]
                })


    def __sortearPosicaoNoEixo(self):
        return self.sorteador.randrange(42)
