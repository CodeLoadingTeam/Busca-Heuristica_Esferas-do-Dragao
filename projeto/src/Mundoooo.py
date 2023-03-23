from Matriz import Matriz

class Mundo(Matriz):

    def __init__(self):
        self.__mundo = self.Matriz.recuperaMatriz()


    ### ################################## ###

    def recuperaMundo(self):
        return self.__mundo

mundo = Mundo()
print(mundo.recuperaMundo())
