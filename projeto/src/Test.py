# matriz = [
#     [['A','l'], ['A',''], ['A',''], ['A','']],
#     [['A',''], ['A',''], ['A',''], ['A','']],
#     [['A',''], ['A',''], ['A',''], ['A','']],
#     [['A',''], ['A',''], ['A',''], ['A','']]
# ]

def printaMatriz():
    global matriz

    for linha in matriz:

        for coluna in linha: 
            print(coluna, end= ' ')

        print()
    print()


def moveAgente(parametro_x, parametro_y):
    global matriz, biomaAux, ultimoPasso

    if '⌘' not in matriz:
        guardaBiomaDoAgente(parametro_x, parametro_y)

        matriz[parametro_y][parametro_x] = '⌘'
        ultimoPasso = [parametro_y, parametro_x]
        return

    x = ultimoPasso[0]
    y = ultimoPasso[1]

    matriz[y][x] = ultimoPasso

    matriz[parametro_y][parametro_x] = '⌘'
    ultimoPasso = [parametro_y, parametro_x]
     

def guardaBiomaDoAgente(x, y):
    global matriz, biomaAux

    # Salva o bioma que o agente está
    biomaAux = matriz[y][x]


########################################

matriz = [
    ['M', 'M', 'G', 'G', 'G'],
    ['M', 'G', 'A', 'G', 'G'],
    ['G', 'G', 'A', 'I', 'G'],
    ['G', 'A', 'A', 'A', 'A'],
    ['G', 'A', 'A', 'A', 'A']
]

moveAgente(2, 3)
printaMatriz()

moveAgente(2, 4)
printaMatriz()
