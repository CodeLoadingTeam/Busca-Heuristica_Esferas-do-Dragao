class Mundo:

    def __init__(self):
        self.__matriz = [
            ['M', 'M', 'G', 'G', 'G'],
            ['M', 'G', 'A', 'G', 'G'],
            ['G', 'G', 'A', 'I', 'G'],
            ['G', 'A', 'A', 'A', 'A'],
            ['G', 'A', 'A', 'A', 'A']
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
