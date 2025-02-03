ver, hor = map(int, input().split())

tabuleiro1 = []
tabuleiro2 = []
pos1 = None
pos2 = None

startpos = None
def defenir():
    global startpos
    for y in range(ver):
        for x in range(hor):
            if tabuleiro1[y][x] == 2:
                startpos = (y, x)

def verificar(jogador, nMovimentos):
    global pos1, pos2, tabuleiro1, tabuleiro2
    for n in range(nMovimentos):
        if jogador == 1:
            if pos1 is None:
                pos1 = startpos
                continue

            posy = pos1[0]
            posx = pos1[1]
            if posy + 1 < ver and tabuleiro1[posy + 1][posx] in (1, 9):
                tabuleiro1[posy][posx] = 0
                pos1 = (posy + 1, posx)
                if tabuleiro1[posy + 1][posx] == 9:
                    return True
            elif posy - 1 >= 0 and tabuleiro1[posy - 1][posx] in (1, 9):
                tabuleiro1[posy][posx] = 0
                pos1 = (posy - 1, posx)
                if tabuleiro1[posy - 1][posx] == 9:
                    return True
            elif posx + 1 < hor and tabuleiro1[posy][posx + 1] in (1, 9):
                tabuleiro1[posy][posx] = 0
                pos1 = (posy, posx + 1)
                if tabuleiro1[posy][posx + 1] == 9:
                    return True
            elif posx - 1 >= 0 and tabuleiro1[posy - 1][posx] in (1, 9):
                tabuleiro1[posy][posx] = 0
                pos1 = (posy, posx - 1)
                if tabuleiro1[posy][posx - 1] == 9:
                    return True
        else:
            if pos2 is None:
                pos2 = startpos
                continue

            posy = pos2[0]
            posx = pos2[1]
            if posy + 1 < ver and tabuleiro2[posy + 1][posx] in (1, 9):
                tabuleiro2[posy][posx] = 0
                pos2 = (posy + 1, posx)
                if tabuleiro2[posy + 1][posx] == 9:
                    return True
            elif posy - 1 >= 0 and tabuleiro2[posy - 1][posx] in (1, 9):
                tabuleiro2[posy][posx] = 0
                pos2 = (posy - 1, posx)
                if tabuleiro2[posy - 1][posx] == 9:
                    return True
            elif posx + 1 < hor and tabuleiro2[posy][posx + 1] in (1, 9):
                tabuleiro2[posy][posx] = 0
                pos2 = (posy, posx + 1)
                if tabuleiro2[posy][posx + 1] == 9:
                    return True
            elif posx - 1 >= 0 and tabuleiro2[posy - 1][posx] in (1, 9):
                tabuleiro2[posy][posx] = 0
                pos2 = (posy, posx - 1)
                if tabuleiro2[posy][posx - 1] == 9:
                    return True

for i in range(ver):
    matrix = [list(map(int, input().split()))]
    tabuleiro1.append(matrix[0])

tabuleiro2 = [list(linha) for linha in tabuleiro1]

defenir()

while True:
    mov1, mov2 = map(int, input().split())

    if verificar(1,mov1):
        print('FIM')
        print('JOGADOR 1')
        exit()
    else:
        print(f"{pos1[0]+1} {pos1[1]+1}")
    if verificar(2,mov2):
        print('FIM')
        print('JOGADOR 2')
        exit()
    else:
        print(f"{pos2[0]+1} {pos2[1]+1}")