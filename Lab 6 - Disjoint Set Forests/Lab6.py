# -*- coding: utf-8 -*-
"""
Course: CS-2302 Data-Stuctures
Author: Julian Gonzalez
Assignment: Lab 6 
Intstuctor: Olac Fuentes
T.A's: Anindita Nath, Maliheh Zargaran

"""

import matplotlib.pyplot as plt
import numpy as np
import random
import time

######################################################
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
         
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri
####################################################
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

############################################################  
#Create full maze with all adjacent cells are separated by a wall
#Assign each cell to a different set in a disjoint set forest S
#While S has more than one set
#Select a random wall w =[c1,c2]
#If cells c1 and c2 belong to different sets, remove w and join c1’s set and c2’s set
#otherwise do nothing
#Display maze
####################################################
#method that returns True if theres more than one set in the disjoint set forest
# and false otherwise        
def checkSets(S):
    c = 0
    #counts number of sets
    for i in range(len(S)):
        if S[i] == -1:
            c +=1
    if c>1:
        return True
    return False        
         
#Create full maze with all adjacent cells are separated by a wall
def buildMaze(w,row,cols):

    S = DisjointSetForest(row*cols)
    #Assign each cell to a different set in a disjoint set forest S
    while checkSets(S) == True:
        randNum = random.randint(0,len(w)-1)
        #Select a random wall w =[c1,c2]
        randomWall = w[randNum]
        c1,c2 = randomWall[0],randomWall[1]

        if find_c(S,c1) != find_c(S,c2):#If cells c1 and c2 belong to different sets, remove w and join c1’s set and c2’s set
            w.pop(randNum)
#            temp = []
#            for x in range(len(walls)):
#                if walls[x] != d:
#                    temp.append(walls[x])
#            walls=temp
            union(S,c1,c2)
            
    return w

#same as last but with path compression   
def buildMazeC(w,M,N):

    SC = DisjointSetForest(M*N)
    #Assign each cell to a different set in a disjoint set forest S
    while checkSets(SC) == True:
        #Select a random wall w =[c1,c2] 
        randNum = random.randint(0,len(w)-1)
        randomWall = w[randNum]
        c1,c2 = randomWall[0],randomWall[1]
        
        if find_c(SC,c1) != find_c(SC,c2):#If cells c1 and c2 belong to different sets, remove w and join c1’s set and c2’s set
            w.pop(randNum)      
            union_by_size(SC,c1,c2)
            
    return w

M = 10 #rows
N = 10 #columns
standard = wall_list(M,N)
compressed =  wall_list(M,N)

start = time.time()
standardUnion = buildMaze(standard,M,N)
draw_maze(standardUnion,M,N)
end = time.time()
print('Union standard:',end-start)

start2 = time.time()
compressedUnion = buildMazeC(compressed,M,N)
draw_maze(compressedUnion,M,N)
end2= time.time()
print('Union compression:',end2-start2)
          
