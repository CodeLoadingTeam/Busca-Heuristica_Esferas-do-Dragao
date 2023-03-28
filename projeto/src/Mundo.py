from Esferas import Esferas

class Mundo:

    def __init__(self):
        self.__esferas = Esferas()
        self.__matriz = [
            ['G','G','G','G','G','G','G','M','G','M','G','M','G','M','G','G','G','G','G','A','A','A','A','G','G','G','G','G','G','G','G','M','G','M','M','M','M','M','G','G','G','G'],
            ['M','G','M','M','M','M','G','G','G','G','G','M','G','M','G','M','M','M','M','M','A','A','A','G','G','M','M','M','M','G','G','M','G','G','G','G','G','M','G','M','M','M'],
            ['G','G','G','G','G','G','G','M','M','M','M','M','G','M','G','G','G','G','A','A','A','A','A','A','G','G','G','G','M','G','G','M','G','M','M','M','G','M','G','M','M','M'],
            ['G','M','M','M','M','G','G','M','G','G','G','G','G','G','G','G','A','A','A','A','A','A','A','A','A','A','G','G','M','G','G','M','G','G','G','M','G','G','G','G','G','G'],
            ['G','M','G','G','M','G','G','M','G','M','G','M','M','M','G','A','A','A','A','A','A','A','A','A','A','A','A','G','M','M','G','M','M','M','G','M','M','M','M','G','M','M'],
            ['G','M','G','G','M','G','G','G','G','M','G','G','M','G','G','A','A','A','A','A','A','A','A','A','A','A','A','G','G','G','G','G','G','M','G','G','G','G','M','G','G','G'],
            ['G','M','M','G','M','G','G','M','G','M','G','M','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','G','G','M','G','M','M','M','M','G','M','M','M','M'],
            ['G','G','G','G','M','M','M','M','G','M','G','M','A','A','A','A','A','A','A','A','G','G','G','G','A','A','A','A','A','A','G','G','G','G','G','G','G','G','G','G','G','G'],
            ['G','M','G','G','M','G','G','G','G','M','A','A','A','A','A','A','A','A','M','M','M','M','G','G','G','A','A','A','A','A','A','A','G','M','M','M','G','M','M','M','M','M'],
            ['G','M','M','M','M','M','M','G','G','G','A','A','A','A','A','A','G','G','M','G','G','G','G','M','M','G','A','A','A','A','A','A','G','M','G','M','G','M','G','G','G','G'],
            ['G','G','G','M','G','G','G','G','A','A','A','A','A','A','A','A','G','G','M','M','M','M','G','G','G','G','G','G','A','A','A','A','G','M','G','M','G','M','M','G','M','M'],
            ['G','G','M','M','A','A','A','A','A','A','A','A','A','A','A','A','G','G','G','G','G','M','G','M','M','M','G','G','G','A','A','A','G','G','G','G','G','G','G','G','G','G'],
            ['M','M','A','A','A','A','A','A','A','A','A','A','A','A','A','A','G','M','M','G','M','G','M','G','G','G','G','G','A','A','A','A','A','A','G','M','M','M','M','G','M','G'],
            ['A','A','A','A','A','A','G','G','A','A','A','A','A','A','A','A','A','A','G','G','G','M','G','G','G','A','A','A','A','A','A','A','A','A','G','G','G','G','M','G','M','G'],
            ['A','A','A','A','A','A','G','G','A','A','A','A','A','A','A','A','A','A','A','A','G','G','G','G','A','A','A','A','A','A','A','A','A','A','A','A','A','G','M','G','M','G'],
            ['A','A','A','A','A','G','G','M','M','M','G','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','G','A','A','A','A','A','G','M','M','M','M'],
            ['A','A','A','M','G','G','G','M','G','M','G','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','M','G','M','A','A','A','A','G','G','G','G','G'],
            ['A','A','G','M','G','M','M','M','G','M','G','A','A','A','A','A','A','A','A','G','A','A','A','A','A','A','A','A','A','A','M','G','M','A','A','A','A','G','G','G','G','G'],
            ['G','G','M','M','G','G','G','M','G','M','M','A','A','A','A','A','A','A','G','G','G','A','A','A','A','A','A','A','A','A','M','G','M','M','A','A','A','A','G','M','M','G'],
            ['M','M','M','G','G','M','M','M','G','G','G','A','A','A','A','A','A','G','G','I','G','G','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','G','M','M'],
            ['G','G','G','G','G','M','G','G','A','A','A','A','A','A','A','A','A','A','G','G','G','A','A','A','A','A','A','A','A','G','G','G','G','G','A','A','A','A','A','A','G','G'],
            ['M','M','G','M','M','M','G','A','A','A','A','A','A','A','A','A','A','A','A','G','A','A','A','A','A','A','A','A','A','G','M','M','M','M','M','A','A','A','A','A','A','A'],
            ['G','G','G','G','M','G','G','A','A','A','A','M','M','M','A','A','A','A','A','A','A','A','A','A','A','A','A','A','M','M','M','M','G','G','M','A','A','A','A','A','A','A'],
            ['G','M','M','M','M','G','G','A','A','A','G','G','G','M','A','A','A','A','A','A','A','A','A','A','A','A','A','M','G','G','G','G','G','M','A','A','A','G','G','A','A','A'],
            ['G','M','G','G','G','G','M','A','A','A','A','M','M','M','A','A','A','A','A','A','A','A','A','A','A','A','G','M','G','M','M','M','G','M','M','M','G','G','G','G','A','A'],
            ['G','M','G','G','M','M','M','M','G','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','M','M','G','M','G','M','G','G','M','G','M','M','M','G','A','A'],
            ['G','G','G','G','M','G','G','M','G','A','A','A','A','A','A','A','A','M','M','M','A','A','A','A','A','A','G','G','G','M','G','G','G','M','M','G','M','G','M','G','A','A'],
            ['A','G','M','G','M','G','G','G','G','G','G','G','G','A','A','A','G','G','G','G','G','G','A','A','A','A','M','M','G','M','M','M','G','M','G','G','G','G','M','G','A','A'],
            ['A','G','M','G','M','M','M','M','G','G','M','M','G','A','A','A','G','G','M','M','G','G','A','A','A','A','G','M','G','G','G','G','G','G','G','M','M','M','M','G','A','A'],
            ['A','A','A','G','G','G','G','M','G','G','M','G','G','A','A','A','M','G','G','M','M','G','A','A','A','A','G','M','M','M','M','M','G','M','M','G','G','G','A','A','A','A'],
            ['A','A','A','G','M','M','G','G','G','G','G','G','G','A','A','A','A','M','G','G','M','G','A','A','A','A','A','A','M','G','G','G','G','M','G','A','A','A','A','A','A','A'],
            ['A','A','A','A','A','M','G','A','A','A','A','A','A','A','A','A','A','A','A','G','G','G','A','A','A','A','A','A','M','M','M','M','M','M','A','A','A','A','M','M','M','M'],
            ['G','A','A','A','A','M','G','A','A','A','A','A','A','A','A','A','A','A','A','A','G','G','A','A','A','A','A','A','G','G','G','G','G','G','A','A','A','M','M','G','G','G'],
            ['G','G','M','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','M','G','G','M','G'],
            ['G','G','M','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','G','G','G','M','G'],
            ['G','A','A','A','A','G','G','A','A','A','A','A','A','A','A','A','G','G','G','G','G','G','G','G','G','A','A','A','A','A','A','A','A','A','A','A','A','M','M','G','G','G'],
            ['A','A','A','A','A','G','M','A','A','A','A','A','A','A','A','G','G','M','M','M','G','M','M','M','G','G','G','A','A','A','A','A','G','G','G','A','A','A','M','M','M','M'],
            ['A','A','A','A','A','G','G','G','A','A','A','A','A','A','M','G','G','G','G','G','G','M','G','M','G','M','M','A','A','A','A','G','M','G','M','G','A','A','A','A','A','A'],
            ['A','A','A','G','G','G','G','G','A','A','A','A','A','M','M','G','M','G','G','G','G','M','G','M','G','G','G','M','G','A','A','G','M','G','M','G','A','A','A','A','A','A'],
            ['A','A','A','G','M','M','G','M','M','M','G','A','G','M','G','G','M','G','M','M','M','M','G','M','M','M','G','M','G','A','A','G','M','G','M','G','G','G','G','A','A','A'],
            ['A','G','G','G','G','G','G','G','G','M','G','G','G','G','G','G','G','G','M','G','G','G','G','G','G','M','G','M','G','G','G','M','M','G','M','M','G','G','M','G','A','A'],
            ['A','G','M','M','G','G','M','M','G','G','G','G','G','M','G','M','M','G','G','G','M','M','G','M','G','G','G','G','G','M','G','G','G','G','G','G','M','G','G','G','A','A']
        ]

        self.__dimensaoMatriz = len(self.usarMatriz())


    def usarMatriz(self):
        return self.__matriz
    

    def atualizarMatriz(self, x, y, valor):
        self.__matriz[y][x] = valor


    def printarMatriz(self):

        for linha in self.usarMatriz():
            
            for coluna in linha: 
                print(coluna, end= ' ')

            print()

        print()


    def dimensaoDaMatriz(self):
        return self.__dimensaoMatriz
    

    def usarEsferas(self):
        return self.__esferas
