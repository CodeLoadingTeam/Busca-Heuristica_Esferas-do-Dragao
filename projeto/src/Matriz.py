class Matriz:

    __tamanhoVetor = 42

    def __init__(self):
        self.__matriz = [self.__preencheColunas() for _ in range(self.__tamanhoVetor)]


    ### ########################################################################## ###

    def __preencheColunas(self):
        vetor = []

        for _ in range(self.__tamanhoVetor):
            vetor.append('A')

        return vetor

    def recuperaMatriz(self):
        return self.__matriz
    
mundo = Matriz()

for linha in mundo.recuperaMatriz():

    for coluna in linha: 
        print(coluna, end= ' ')

    print()
    
