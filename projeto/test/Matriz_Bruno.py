def espacamento():
    print()

def recuperaMundo():
    
    matriz = [
        ['montanha', 'montanha', 'grama', 'grama'],
        ['montanha', 'grama',  'água',  'água'],
        ['grama', 'grama',  'água',  'água'],
        ['grama', 'água',  'água',  'água']
    ]

    return matriz


### ######################################## ###

for linha in recuperaMundo():

    for indice in range(4):

        numeroTerreno = indice + 1

        match linha[indice]:
            case 'montanha':   
                pontos = 60
            case 'água':
                pontos = 10
            case 'grama':
                pontos = 1

        print('Terreno ', numeroTerreno, ': ', linha[indice], '  ( valor: ', pontos, ')')

    espacamento()
