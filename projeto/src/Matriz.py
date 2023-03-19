#import numpy as np

class Matriz:

    def __init__(self):
        self.__matriz = [[1,2] for _ in range(42)]


    def recuperaMatriz(self):
        return self.__matriz
    
    print(
        len(recuperaMatriz())
    )