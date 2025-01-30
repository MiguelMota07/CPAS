ver, hor = map(int, input().split())

tabuleiro1 = []
tabuleiro2 = []
pos1 = None
pos2 = None

def defenir():
    global pos1, pos2
    for x in range(hor):
        for y in range(ver):
            if tabuleiro1[x][y] == 2:
                pos1 = (x,y)
                pos2 = (x,y)
                return

def verificar(jogador, nMovimentos):
    global pos1, pos2, tabuleiro1, tabuleiro2
    for n in range(nMovimentos):
        if jogador == 1:
            posy = pos1[0]
            posx = pos1[1]
            if posy+1 < hor and tabuleiro1[posy+1][posx+0] == 1 or 9:
                tabuleiro1[posy][posx] = 0
                pos1 = (posy+1,posx+0)
                if tabuleiro1[posy+1][posx+0] != 1:
                    return True
            elif posy-1 >= 0 and tabuleiro1[posy-1][posx+0] == 1 or 9:
                tabuleiro1[posy][posx] = 0
                pos1 = (posy-1,posx+0)
                if tabuleiro1[posy-1][posx+0] != 1:
                    return True
            elif posx+1 < ver and tabuleiro1[posy+0][posx+1] == 1 or 9:
                tabuleiro1[posy][posx] = 0
                pos1 = (posy+0,posx+1)
                if tabuleiro1[posy+0][posx+1] != 1:
                    return True
            elif posx-1 >= 0 and tabuleiro1[posy+0][posx-1] == 1 or 9:
                tabuleiro1[posy][posx] = 0
                pos1 = (posy+0,posx-1)
                if tabuleiro1[posy+0][posx-1] != 1:
                    return True
            else:
                return False
        else:
            posy = pos2[0]
            posx = pos2[1]
            if posy+1 < hor and tabuleiro2[posy+1][posx+0] == 1 or 9:
                tabuleiro2[posy][posx] = 0
                pos2 = (posy+1,posx+0)
                if tabuleiro2[posy+1][posx+0] != 1:
                    return True
            elif posy-1 >= 0 and tabuleiro2[posy-1][posx+0] == 1 or 9:
                tabuleiro2[posy][posx] = 0
                pos2 = (posy-1,posx+0)
                if tabuleiro2[posy-1][posx+0] != 1:
                    return True
            elif posx+1 < ver and tabuleiro2[posy+0][posx+1] == 1 or 9:
                tabuleiro2[posy][posx] = 0
                pos2 = (posy+0,posx+1)
                if tabuleiro2[posy+0][posx+1] != 1:
                    return True
            elif posx-1 >= 0 and tabuleiro2[posy+0][posx-1] == 1 or 9:
                tabuleiro2[posy][posx] = 0
                pos2 = (posy+0,posx-1)
                if tabuleiro2[posy+0][posx-1] != 1:
                    return True
            else:
                return False

for i in range(ver):
    matrix = [list(map(int, input().split()))]
    tabuleiro1.append(matrix[0])
    tabuleiro2.append(matrix[0])

defenir()

while True:
    mov1, mov2 = map(int, input().split())

    if verificar(1,mov1):
        print('FIM')
        print('JOGADOR 1')
        exit()
    else:
        print(f"{pos1[0]} {pos1[1]}")
    if verificar(2,mov2):
        print('FIM')
        print('JOGADOR 2')
        exit()
    else:
        print(f"{pos2[0]} {pos2[1]}")