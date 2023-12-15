# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:25:20 2023

@author: rcres
"""

xpos = ypos = 1
num = [xpos, ypos]

def func(val):
    val[0] = 5

print(xpos)
func(num)
print(num)


def func2():
    return True,2


xpos,ypos = func2()
print(xpos)
print(ypos)

