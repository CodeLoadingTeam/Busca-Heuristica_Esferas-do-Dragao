from Agente import Agente
import time as t
import sys


sys.setrecursionlimit(100000)


agente = Agente()

def executar():

    limparPrint()


    for esfera in agente.mundo.coordenadasDasEsferas():
        if esfera['aparicao'] == 'visivel':

            agente.mostrarMundo()
            esfera['aparicao'] = 'visualizada'
            t.sleep(2)


    agente.deslocar()
    agente.mostrarMundo()
    t.sleep(0.001) 

    executar()


def limparPrint():
    print("\033c", end="")


executar()
