estadoInicial = True
x_inicial, y_inicial = 3, 2

# CIMA = 'cima'
# BAIXO = 'baixo'
# ESQUERDA = 'esquerda'
# DIREITA = 'direita'

def printarMatriz():
    global matriz

    for linha in matriz:

        for coluna in linha: 
            print(coluna, end= ' ')

        print()
    print()


def inicializarAgente():
    global matriz, estadoInicial

    if estadoInicial == True:

        guardarBiomaDoAgente(x_inicial, y_inicial)
        matriz[y_inicial][x_inicial] = '⌘'


def moverAgente(parametro_x, parametro_y):
    global matriz, estadoInicial, bioma, ultimoLocalAgente

    if estadoInicial == False:
        
        x = ultimoLocalAgente[0]
        y = ultimoLocalAgente[1]
        matriz[y][x] = bioma 
        ultimoLocalAgente  = [parametro_x, parametro_y]    
    
    else:
        estadoInicial = False
        ultimoLocalAgente = [x_inicial, y_inicial]
        x = ultimoLocalAgente[0]
        y = ultimoLocalAgente[1]
        matriz[y][x] = bioma  

    guardarBiomaDoAgente(parametro_x, parametro_y)
    matriz[parametro_y][parametro_x] = '⌘'
 

def guardarBiomaDoAgente(x, y):
    global matriz, bioma

    # Salva o bioma que o agente está
    bioma = matriz[y][x]


########################################

matriz = [
    ['M', 'M', 'G', 'G', 'G'],
    ['M', 'G', 'A', 'G', 'G'],
    ['G', 'G', 'A', 'I', 'G'],
    ['G', 'A', 'A', 'A', 'A'],
    ['G', 'A', 'A', 'A', 'A']
]

inicializarAgente()

moverAgente(3, 2)
printarMatriz()


moverAgente(2, 2)
printarMatriz()

moverAgente(1, 2)
printarMatriz()

moverAgente(1, 1)
printarMatriz()

# moverAgente(CIMA)
