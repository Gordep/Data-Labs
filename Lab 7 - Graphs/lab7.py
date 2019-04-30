# -*- coding: utf-8 -*-
"""
Course: CS-2302 Data-Stuctures
Author: Julian Gonzalez
Assignment: Lab 7 
Intstuctor: Olac Fuentes
T.A's: Anindita Nath, Maliheh Zargaran

"""

import matplotlib.pyplot as plt
import numpy as np
import random
import time
import queue

######################################################
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
        
def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w    

######################################################
#Implementation of Search psuedocode given in class
def breadthFirstSearch(G,v): #used class pseudocode 
    visited = [False] * len(G)#initialize visited False with length of G
    prev = [-1] * len(G)#initialize prev -1 with length of G
    #print(visited,prev)
    Q = queue.Queue()#may need to fix
    Q.put(v)
    visited[v] = True
    while not Q.empty():
        u = Q.get()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.put(t)
    return prev

def depthFirstSearchS(G,v): #same as breadthFirstSearch but using list as a stack
    visited = [False] * len(G)#initialize visited False with length of G
    prev = [-1] * len(G)#initialize prev -1 with length of G
    S = [] #create stack "list"
    S.append(v)
    visited[v] = True
    while len(S) != 0:
        u = S.pop()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                S.append(t)
    return prev

def depthFirstSearchR(G,source):#used class pseudocode
    visited = [False] * len(G)#initialize visited False with length of G
    prev = [-1] * len(G)#initialize prev -1 with length of G
    visited[source] = True
    for t in G[source]:
        if not visited[t]:
            prev[t]=source
        depthFirstSearchR(G,t) ##dont know if need to return anything?
    #return prev
##################################################

def ModbuildMazeC(SC,w,numCells,numRemove):#modified version of BuildMazeC used in lab6
    counter = 0 #used to remove user specifc amount of walls
    while counter <  numRemove:  
        #Assign each cell to a different set in a disjoint set forest S
        #Select a random wall w =[c1,c2] 
        randNum = random.randint(0,len(w)-1)
        randomWall = w[randNum]
        c1,c2 = randomWall[0],randomWall[1]
        if counter < (numCells -1 ):            
            if find_c(SC,c1) != find_c(SC,c2):#If cells c1 and c2 belong to different sets, remove w and join c1’s set and c2’s set
                w.pop(randNum)      
                union_c(SC,c1,c2)
                counter += 1
        else:
            w.pop(randNum)      
            counter +=1
                
    return w


def adjMaze(newWalls,walls,cells):
    L = [[] for i in range(cells)]
    for w in walls:
        if w not in newWalls: #checks for wall 
            L[w[0]].append(w[1]) # insert adjacency one way
            #L[w[1]].append(w[0]) # used when want to see all edges if not used sometimes cannot find path to end
    return L

####################################################

row = 4
col = 3
numCells = row * col#number of total cells

wallList = wall_list(row,col)
#draw_maze(wallList,row,col,cell_nums=True)#cell_nums=True

dsf = DisjointSetForest(numCells) 

print("The maze contains %d cells, How many cells do you want to remove?" % (numCells))
numRemove = int(input())

if numRemove < numCells-1:
    print(" A path from source to destination is not guaranteed to exist")
if numRemove == numCells-1:
    print("There is a unique path from source to destination")
if numRemove > numCells-1:
    print("There is at least one path from source to destination")

#start = time.time()
tempWalls = wallList.copy()

newWalls= ModbuildMazeC(dsf,tempWalls,numCells,numRemove)

#end = time.time()
#print('Time:',end-start)
draw_maze(newWalls,row,col,cell_nums=True)


adjList = adjMaze(newWalls,wallList,numCells)#may not work depending on generated graph
print(adjList)

print(breadthFirstSearch(adjList,0))#0 for bottom left corner
print(depthFirstSearchS(adjList,0))
print(depthFirstSearchR(adjList,0))

