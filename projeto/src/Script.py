ESQUERDA = 'esquerda'
DIREITA = 'direita'
CIMA = 'cima'
BAIXO = 'baixo'

sentidos = [ESQUERDA, DIREITA, CIMA, BAIXO]

def deslocar(self, sentido):
    passo_x, passo_y = 0, 0

    match sentido:
        case self.ESQUERDA:
            passo_x = -1
        case self.DIREITA:
            passo_x = 1
        case self.CIMA:
            passo_y: -1
        case self.BAIXO:
            passo_y = 1

    atualizaAgenteNaMatriz(passo_x, passo_y)

def atualizaAgenteNaMatriz(passo_x, passo_y):
    global x, y

    x += passo_x
    y += passo_y


    