import os
import random

if not os.path.exists("girds"):
    os.mkdir("grids")
    print("Directory " , "grid" ,  " Created ")



for i in range(50):
    fileN = "grids/gird" + str(i)
    
    grid = []
    for row in range(100):
        grid.append([])
        for column in range(100):
            grid[row].append(0)

    for raw in range(31):
        for colum in range(31):
            grid[random.randrange(0,100)][random.randrange(0,100)]=1

    f = open(fileN, "w")
    for row in range(100):
        for column in range(100):
            f.write(str(grid[row][column]))
        f.write("\n")
    f.close()
           