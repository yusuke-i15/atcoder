# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 21:12:28 2022

@author: 81702
"""

N,M = map(int,input().split())

if N == 1:
    for i1 in range(1,M+1):
        print(i1)
if N == 2:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            print(i1,i2)
if N == 3:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            for i3 in range(i2+1,M+1):
                print(i1,i2,i3)
if N == 4:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            for i3 in range(i2+1,M+1):
                for i4 in range(i3+1,M+1):
                    print(i1,i2,i3,i4)
if N == 5:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            for i3 in range(i2+1,M+1):
                for i4 in range(i3+1,M+1):
                    for i5 in range(i4+1,M+1):
                        print(i1,i2,i3,i4,i5)
if N == 6:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            for i3 in range(i2+1,M+1):
                for i4 in range(i3+1,M+1):
                    for i5 in range(i4+1,M+1):
                        for i6 in range(i5+1,M+1):
                            print(i1,i2,i3,i4,i5,i6)
if N == 7:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            for i3 in range(i2+1,M+1):
                for i4 in range(i3+1,M+1):
                    for i5 in range(i4+1,M+1):
                        for i6 in range(i5+1,M+1):
                            for i7 in range(i6+1,M+1):
                                print(i1,i2,i3,i4,i5,i6,i7)
if N == 8:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            for i3 in range(i2+1,M+1):
                for i4 in range(i3+1,M+1):
                    for i5 in range(i4+1,M+1):
                        for i6 in range(i5+1,M+1):
                            for i7 in range(i6+1,M+1):
                                for i8 in range(i7+1,M+1):
                                    print(i1,i2,i3,i4,i5,i6,i7,i8)
if N == 9:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            for i3 in range(i2+1,M+1):
                for i4 in range(i3+1,M+1):
                    for i5 in range(i4+1,M+1):
                        for i6 in range(i5+1,M+1):
                            for i7 in range(i6+1,M+1):
                                for i8 in range(i7+1,M+1):
                                    for i9 in range(i8+1,M+1):
                                            print(i1,i2,i3,i4,i5,i6,i7,i8,i9)
if N == 10:
    for i1 in range(1,M+1):
        for i2 in range(i1+1,M+1):
            for i3 in range(i2+1,M+1):
                for i4 in range(i3+1,M+1):
                    for i5 in range(i4+1,M+1):
                        for i6 in range(i5+1,M+1):
                            for i7 in range(i6+1,M+1):
                                for i8 in range(i7+1,M+1):
                                    for i9 in range(i8+1,M+1):
                                        for i10 in range(i9+1,M+1):
                                            print(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10)
    