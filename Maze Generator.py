# -*- coding: utf-8 -*-'

import numpy
import random
from Point import Point
from PIL import Image

#Function
def validate_maze(grid, path, xpos, ypos, index):
    for i2 in range(index[0],len(path),1):
        if grid[path[i2].x][path[i2].y+1] != 3:
            if grid[path[i2].x][path[i2].y+2] == 0:
                xpos = path[i2].x
                ypos = path[i2].y+1
                index[0] = i2+1
                return False, xpos, ypos
        if grid[path[i2].x][path[i2].y-1] != 3: 
            if grid[path[i2].x][path[i2].y-2] == 0:
                xpos = path[i2].x
                ypos = path[i2].y-1
                index[0] = i2+1
                return False, xpos, ypos
        if grid[path[i2].x-1][path[i2].y] != 3: 
            if grid[path[i2].x-2][path[i2].y] == 0:
                xpos = path[i2].x-1
                ypos = path[i2].y
                index[0] = i2+1
                return False, xpos, ypos
        if grid[path[i2].x+1][path[i2].y] != 3: 
            if grid[path[i2].x+2][path[i2].y] == 0:
                xpos = path[i2].x+1
                ypos = path[i2].y
                index[0] = i2+1
                return False, xpos, ypos
    
    return True, 0, 0

#Variables
size = 27
grid = numpy.zeros((size, size))
anchor = []
path = []
color = [
    (0, 0,255), #Blue
    (0, 0, 0), #Black
    ]


for x in range(size):
    grid[x][0] = 3
    grid[x][size-1] = 3
for y in range(size):
    grid[0][y] = 3
    grid[size-1][y] = 3

        
#Set Anchor Points. range(start, stop, increment)
for x in range(2,size-2,2):
    for y in range(2,size-2,2):
        grid[x][y] = 1
        anchor.append(Point(x,y))
        
        # anchor.append(copy.copy(temp)) hace una copia. Requiere import copy
        # anchor.append(temp) directamente hace pass temp, como un pointer.

"""
for i in range(len(anchor)):
    anchor[i].coordinate()
"""
    
for i in range(len(anchor)):
    rdir = random.randint(1, 4)
    nxt = 0
    
    while nxt != 1 and nxt != 3:
        if rdir == 1:
            anchor[i].y += 1
            grid[anchor[i].x][anchor[i].y] = 1
            nxt = grid[anchor[i].x][anchor[i].y+1]
        elif rdir == 2:
            anchor[i].y -= 1
            grid[anchor[i].x][anchor[i].y] = 1
            nxt = grid[anchor[i].x][anchor[i].y-1]
        elif rdir == 3:
            anchor[i].x -= 1
            grid[anchor[i].x][anchor[i].y] = 1
            nxt = grid[anchor[i].x-1][anchor[i].y]
        elif rdir == 4:
            anchor[i].x += 1
            grid[anchor[i].x][anchor[i].y] = 1
            nxt = grid[anchor[i].x+1][anchor[i].y]

#versus xpos, ypos = 1, 2
xpos = ypos = 1
finished = False
index1 = 0
index2 = [0]

while finished != True:
    grid[xpos][ypos] = 2
    path.append(Point(xpos,ypos))
    if grid[xpos][ypos+1] == 0:
        ypos += 1
    elif grid[xpos][ypos-1] == 0:
        ypos -= 1
    elif grid[xpos-1][ypos] == 0:
        xpos -= 1
    elif grid[xpos+1][ypos] == 0:
        xpos += 1
    else:
        for i in range(index1, len(path), 1):
            if grid[path[i].x][path[i].y+1] == 0:
                xpos = path[i].x
                ypos = path[i].y+1
                break
            elif grid[path[i].x][path[i].y-1] == 0:
                xpos = path[i].x
                ypos = path[i].y-index1
                break
            elif grid[path[i].x-1][path[i].y] == 0:
                xpos = path[i].x-1
                ypos = path[i].y
                break
            elif grid[path[i].x+1][path[i].y] == 0:
                xpos = path[i].x+1
                ypos = path[i].y
                break
            elif i == len(path)-1:
                finished, xpos, ypos = validate_maze(grid, path, xpos, ypos, index2)
                break

"""
for y in range(size):
    print()
    for x in range(size):
        print(int(grid[x][y]), end = ' ')
        
print(bool(finished))
"""

#Render image
maze = Image.new("RGB", (size,size))
for x in range(size):
    for y in range(size):
        if grid[x][y] == 2 or grid[x][y] == 0:
            c_index = 1
        elif grid[x][y] == 1 or grid[x][y] == 3:
            c_index = 0
        maze.putpixel((x, y), color[c_index])
            
#maze.save("maze.png")
maze.show()

#Definir el maze verifier para que haga return true or false... (easier para escapar de los nested for loops).
