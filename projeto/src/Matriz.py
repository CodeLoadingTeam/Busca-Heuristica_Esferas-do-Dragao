class Matriz:

    __tamanhoVetor = 4

    def __init__(self):
        self.__matriz = [self.__preencheColunas() for _ in range(self.__tamanhoVetor)]


    ### ########################################################################## ###

    def __preencheColunas(self):
        vetor = []

        for _ in range(self.__tamanhoVetor):
            vetor.append(1)

        return vetor

    def recuperaMatriz(self):
        return self.__matriz
