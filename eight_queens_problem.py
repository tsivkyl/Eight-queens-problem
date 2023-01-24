# numpy är ej kritiskt men gör utskriften väsentligt mycket snyggare
import numpy


bräde = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

valid_solutions=[]   # All valid solutions (boards) are added to this array of boards

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
# Filter out symmetrical and rotated solutions

def print_result(doc, solutions):
     print(doc, "number of remaining solutions=", len(solutions))

def remove_mirrors_and_rotations(valid_solutions):

    doc= "Mirror on horizontal axis"
    solutions= filter_solutions(valid_solutions, 0, 0) 
    print_result(doc, solutions)

    doc= "Mirror on vertical axis"
    solutions= filter_solutions(solutions, 0, 1)
    print_result(doc, solutions)

    doc= "Mirror on SW-NE diagonal, Method 1"
    solutions=filter_solutions(solutions, 2, 0, 1)
    print_result(doc, solutions)

    doc= "Mirror on NW-SE diagonal, Method 1:"
    solutions=filter_solutions(solutions, 2, 1, 1) 
    print_result(doc, solutions)

    doc= "Rotate 90 degrees"
    solutions=filter_solutions(solutions, 1, 1)         
    print_result(doc, solutions)

    doc= "Rotate 180 degrees"
    solutions=filter_solutions(solutions, 1, 2)
    print_result(doc, solutions)

    doc="Rotate 270 degrees"
    solutions=filter_solutions(solutions, 1, 3)
    print_result(doc, solutions)

    doc="Mirror on SW-NE diagonal, Method 1"
    solutions=filter_solutions(solutions, 2, 0, 1)
    print_result(doc, solutions)
  
    doc="Mirror on NW-SE diagonal, Method 1"
    solutions=filter_solutions(solutions, 2, 1, 1)
    print_result(doc, solutions)

    doc="Mirror on NW-SE diagonal, method 2"
    solutions=filter_solutions(solutions, 2, 0, 3)
    print_result(doc, solutions)

    doc="Mirror on SW-NE diagonal, method 2"
    solutions=filter_solutions(solutions, 2, 1, 3)
    print_result(doc, solutions)

    return solutions

def filter_solutions(solutions, t_function, k, l=1):
    # t_function
    #     0     Flip= Reverse the order of elements in the solutions array along the given axis(=k).
    #           k=0 flips the entries in each column in the up/down direction. Rows are preserved, but appear in a different order than before.
    #           k=1 flips the entries in each row in the left/right direction. Columns are preserved, but appear in a different order than before.
    #     1     Rotate the solutions array by 90 degrees, k times.
    #     2     Flip and rotate the solutions array
    
    global valid_solutions

    solutions_length=len(solutions)

    passed_solutions=[]

    for i in range(solutions_length):

        if (t_function==0):
            transformed_board=numpy.flip(solutions[i],k)  #
        elif (t_function==1):
            transformed_board=numpy.rot90(solutions[i],k)
        elif (t_function==2):
            transformed_board= numpy.rot90(numpy.flip(solutions[i],k),l)
        else: 
            raise NameError('Illegal transform function') 
        transformed_board_found=False
        for j in range(i+1,solutions_length):
            compare= transformed_board==solutions[j]
            if compare.all():
                transformed_board_found=True
                break
        if not transformed_board_found: 
            passed_solutions.append(valid_solutions[i])
        if transformed_board_found: 
            pass
    return passed_solutions



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
    valid_solutions.append(numpy.array(bräde))

    
main()
print("number of valid solutuions=",antal)
#input()
remove_mirrors_and_rotations(valid_solutions)