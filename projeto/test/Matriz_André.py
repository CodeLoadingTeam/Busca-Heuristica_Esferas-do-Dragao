mundo = [
        [60, 60, 1, 1],
        [60, 1, 10, 10],
        [1, 1, 10, 10],
        [1, 10, 10, 10]]

for i in range(4):
    for j in range(4):
        if mundo[i][j] == 60:
            print('-montanha- 60 pontos', end = " ")
        elif mundo[i][j] == 10:
            print('-água- 10 pontos', end = " ")
        elif mundo[i][j] == 1:
            print('-Grama- 1 ponto', end = " ")
    print()
    
