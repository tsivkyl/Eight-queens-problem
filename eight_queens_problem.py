# numpy är ej kritiskt men gör utskriften väsentligt mycket snyggare
import numpy


bräde = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

#rad

def rad_okej(y):
    if 1 not in bräde[y]: return True

#kolumn

def kolumn_okej(x):
    for rad in bräde:
        if rad[x] == 1:
            return False
    return True

#diagonal 

def minus_minus(y,x):
    while y>0 and x>0:
        y,x = y -1, x -1
        if 1 == bräde[y][x]:
            return False
    return True

def plus_plus(y,x):
    while y<7 and x<7:
        y,x = y +1, x +1
        if 1 == bräde[y][x]:
            return False
    return True

def minus_plus(y,x):
    while y>0 and x<7:
        y,x = y -1, x +1
        if 1 == bräde[y][x]:
            return False
    return True

def plus_minus(y,x):
    while y>7 and x>0:
        y,x = y +1, x -1
        if 1 == bräde[y][x]:
            return False
    return True

#

def diagonal_okej(y,x):
    if minus_minus(y,x) and plus_plus(y,x) and minus_plus(y,x) and plus_minus(y,x):
        return True
    else: 
        return False

#slutsats

def koordinat_okej(y, x):
    if rad_okej(y) and kolumn_okej(x) and diagonal_okej(y,x):
        return True
    else:
        return False

#minne

antal = 0   

#backtrack

def main():
    global bräde, antal
    for y_koordinat in range(8):
        if 1 not in bräde[y_koordinat]:
            for x_koordinat in range(8):
                if koordinat_okej(y_koordinat, x_koordinat):
                    bräde[y_koordinat][x_koordinat] = 1
                    main()
                    bräde[y_koordinat][x_koordinat] = 0
            return

    print(numpy.array(bräde))
    print()
    antal += 1
    
main()
print(antal)
input()