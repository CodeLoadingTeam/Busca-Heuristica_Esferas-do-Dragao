mundo = [
    [60, 60, 1, 1],
    [60, 1, 10, 10],
    [1, 1, 10, 10],
    [1, 10, 10, 10]
]

tradutor = {60 : "Montanha",
            10 : "Água",
            1 : "Grama"}

for linha in mundo:
    print()
    for colunas in linha:
        if colunas in tradutor:
            print(tradutor[colunas])
            
        # if colunas == 60:
        #     print("Montanha") 
        # elif colunas == 10:
        #     print("Água")
        # else:
        #     print("Grama")
