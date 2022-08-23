# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 21:02:41 2022

@author: 81702
"""

R,C = map(int,input().split())

if R == 1 or R == 15 or C == 1 or C ==15:
    print("black")
elif (R == 3 or R == 13) and (C >= 3 and C <= 13):
    print("black")
elif (C == 3 or C == 13) and (R >= 3 and R <= 13):
    print("black")
elif (R == 5 or R == 11) and (C >= 5 and C <= 11):
    print("black")
elif (C == 5 or C == 11) and (R >= 5 and R <= 11):
    print("black")
elif (R == 7 or R == 9) and (C >= 7 and C <= 9):
    print("black")
elif (C == 7 or C == 9) and (R >= 7 and R <= 9):
    print("black")
else:
    print("white")
