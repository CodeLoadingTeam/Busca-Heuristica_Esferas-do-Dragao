estadoInicial = True

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
        x, y = 3, 2
        estadoInicial = False

        guardarBiomaDoAgente(x, y)
        matriz[y][x] = '⌘'

def moverAgente(parametro_x, parametro_y):
    global matriz, estadoInicial, biomaAtual, ultimoPasso
    
    # x = ultimoPasso[0]
    # y = ultimoPasso[1]

    # matriz[y][x] = biomaAtual

    guardarBiomaDoAgente(parametro_x, parametro_y)

    matriz[parametro_y][parametro_x] = '⌘'

    matriz[parametro_y][parametro_x] = '⌘'
    ultimoPasso = [parametro_x, parametro_y]
     

def guardarBiomaDoAgente(x, y):
    global matriz, biomaAtual

    # Salva o bioma que o agente está
    biomaAtual = matriz[y][x]


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
