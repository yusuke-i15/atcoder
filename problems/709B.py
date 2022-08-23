# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:06:27 2022

@author: 81702
"""
import numpy as np

a,b,d = map(int,input().split())

cos = np.cos(np.deg2rad(d))
sin = np.sin(np.deg2rad(d))

rot_x = (a * cos) - (b * sin)
rot_y = (a * sin) + (b* cos)
print("{} {}".format(rot_x,rot_y))