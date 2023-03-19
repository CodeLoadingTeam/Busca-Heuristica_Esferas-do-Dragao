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

    for index in range(4):

        numeroTerreno = index + 1

        match linha[index]:
            case 'montanha':   
                pontos = 60
            case 'água':
                pontos = 10
            case 'grama':
                pontos = 1

        print('Terreno ', numeroTerreno, ': ', linha[index], '  ( valor: ', pontos, ')')

    espacamento()
    