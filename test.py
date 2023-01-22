#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Trygve Botnen
# Created Date: 2023-01-22
# ---------------------------------------------------------------------------
# Revison history
"""
Tests various numpy flips and rotations on a 4x4 matrix
"""

import numpy 
    
test_board= [
    ["a","b","c", "d"],\
    ["e","f","g", "h"],\
    ["i","j","k", "l"],\
    ["m","n","o", "p"],\
    ]
test_board= numpy.array(test_board)
print("Test board:")
print(test_board)

transformed_board=numpy.flip(test_board,0) 
print("# Mirror on horisontal axis:")
print(transformed_board)

transformed_board=numpy.flip(test_board,1) 
print("Mirror on vertical axis:")
print(transformed_board)

transformed_board=numpy.rot90(test_board,1)
print("Rotated 90 degrees:")
print(transformed_board)

transformed_board=numpy.rot90(test_board,2)
print("Rotated 180 degrees:")
print(transformed_board)

transformed_board=numpy.rot90(test_board,3)
print("Rotated 270 degrees:")
print(transformed_board)


print("# Mirror on horisontal axis AND rotated 90 degrees= Mirror on SW-NE diagonal")
transformed_board= numpy.rot90(numpy.flip(test_board,0),1)  
print(transformed_board)

print("Mirror on vertical axis AND rotate 90 degrees= Mirror on NW-SE diagonal:")
transformed_board= numpy.rot90(numpy.flip(test_board,1),1) 
print(transformed_board)

print("Mirror on horizontal axis and rotate 180 degrees= Mirror on vertical axis:")
transformed_board= numpy.rot90(numpy.flip(test_board,0),2)  
print(transformed_board)

print("Mirror on horizontal axis and rotate 270 degrees=Mirror on NW-SE diagonal") 
transformed_board= numpy.rot90(numpy.flip(test_board,0),3)  
print(transformed_board)

print("Mirror on vertical axis and rotate 270 degrees=Mirror on SW-NE diagonal") 
transformed_board= numpy.rot90(numpy.flip(test_board,1),3)  
print(transformed_board)
