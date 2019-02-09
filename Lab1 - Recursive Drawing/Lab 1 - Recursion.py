# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 21:11:42 2019

Course: CS-2302 Data-Stuctures
Author: Julian Gonzalez
Assignment: Lab 1 Drawing figures with recursion
Intstuctor: Olac Fuentes
T.A's: Anindita Nath, Maliheh Zargaran
Purpose: The purpose of this program is to draw different figures using matplotlib all done recusively 

"""

import numpy as np
import matplotlib.pyplot as plt
import math

def draw_squares(ax,n,sLeft,sRight,w):
    if n>0:
        sL1 = sLeft/2+w
        sR1 = sRight/2+w
        sL2 = sLeft/2-w
        sR2 = sRight/2-w
        
        ax.plot(sLeft-w,sRight-w,color='k')
        
        draw_squares(ax,n-1,sL1,sR1,w)
        draw_squares(ax,n-1,sL1,sR2,w)
        draw_squares(ax,n-1,sL2,sR1,w)
        draw_squares(ax,n-1,sL2,sR2,w)

def circle(center,rad): #Utulizes the circle function porivided in class # used for question 2 and 4
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w): # Utilizes the draw_circles function provided in class
    if n>0:
        x,y = circle(center,radius)
        ax.plot(radius-x,y,color='k') #Only change from provided code. Subtracting the radius with the x coordinate allows for the figure to shift to the left
        draw_circles(ax,n-1,center,radius*w,w)
        
def draw_binaryTree(ax,n,pLeft,pRight,w):
    if n>0:
        # w shifts the tree lower
        left1 = (pLeft/2)-w
        right1 = (pRight)-w 
        #same as above but used for right side tree recursion
        left2 = (pLeft/2)+w
        right2 = (pRight)-w
    
        ax.plot(pLeft,pRight,color='k')                    
        
        draw_binaryTree(ax,n-1,left1,right1,w)#draws the left side branches
        draw_binaryTree(ax,n-1,left2,right2,w)#draws the right side branches
        
def draw_manyCircles(ax,n,center,radius,w): # same parameters as draw_circles but w can be changed to draw kaleidoscopic figures
    if n>0:
        newRadius = radius//w #uses the current radius size divided by w to create the newer smaller circles 
        draw_manyCircles(ax,n-1,center,newRadius,w)
        
        # this section sets the new cordinates for the recurive circles 
        up=[center[0],(radius)-(center[1]+newRadius)] # center[0] and center[1] are used to determine the x and y coordinates for the circles  
        down=[center[0],-((radius)-(center[1]+newRadius))]   
        right=[(center[0]-(radius-newRadius)),center[1]]
        left=[(center[0]+(radius-newRadius)),center[1]]
        
        #same like the provided draw circles function
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        #newRadius is used to determine the new size of the Recursive circles
        draw_manyCircles(ax,n-1,up,newRadius,w)
        draw_manyCircles(ax,n-1,down,newRadius,w)
        draw_manyCircles(ax,n-1,right,newRadius,w)
        draw_manyCircles(ax,n-1,left,newRadius,w)
      

####################
#Question 1 
        ## I was unable to get the code to run correctly
plt.close("all") 
#a)
orig_size = 100
#p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
p = np.array([[-orig_size, orig_size],[-orig_size,-orig_size],[orig_size,-orig_size],[orig_size,orig_size],[-orig_size,orig_size]])
sLeft = p[:,0]
sRight = p[:,1]
fig, ax = plt.subplots()
##draw_squares(ax,15,sLeft,sRight,orig_size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question1a.png')
#b)
orig_size = 100
#p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
#p = np.array([[-orig_size, orig_size],[-orig_size,-orig_size],[orig_size,-orig_size],[orig_size,orig_size],[-orig_size,orig_size]])
sLeft = p[:,0]
sRight = p[:,1]
fig, ax = plt.subplots()
##draw_squares(ax,15,sLeft,sRight,orig_size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question1b.png')

#c)
orig_size = 100
#p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
#p = np.array([[-orig_size, orig_size],[-orig_size,-orig_size],[orig_size,-orig_size],[orig_size,orig_size],[-orig_size,orig_size]])
sLeft = p[:,0]
sRight = p[:,1]
fig, ax = plt.subplots()
##draw_squares(ax,15,sLeft,sRight,orig_size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question1c.png')


####################
#Question 2 
        
#Only thing that changes between the three calls are n, the number of circles to be drawn and w which modifies the radius size 
#a) 
fig,ax = plt.subplots() 
draw_circles(ax, 8, [100,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question2a.png')

#b)
fig,ax = plt.subplots() 
draw_circles(ax, 15, [100,0], 100,.8)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question2b.png')

#c)
fig,ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question2c.png')

####################
#Question 3 

# Only paramater that changes is the height of the tree n    
#a)
orig_size = 100 # used for lengh of the branches and used as the displacement for the x and y axis coordinates
p = np.array([[-orig_size,-orig_size],[0,0],[orig_size,-orig_size]])#holds tree "branches" with 0,0 being the root of the binary tree
fig, ax = plt.subplots()
pLeft = p[:,0]#used for cordinates of branches
pRight = p[:,1]#used for cordinates of branches
draw_binaryTree(ax,3,pLeft,pRight,orig_size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question3a.png')

#b)
orig_size = 100
p = np.array([[-orig_size,-orig_size],[0,0],[orig_size,-orig_size]])
fig, ax = plt.subplots()
pLeft = p[:,0]
pRight = p[:,1]
draw_binaryTree(ax,4,pLeft,pRight,orig_size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question3b.png')

#c)
orig_size = 100
p = np.array([[-orig_size,-orig_size],[0,0],[orig_size,-orig_size]])
fig, ax = plt.subplots()
pLeft = p[:,0]
pRight = p[:,1]
draw_binaryTree(ax,7,pLeft,pRight,orig_size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question3c.png')

####################
#Question 4 
#plt.close("all") 
## n is the only parameter that changes w or (3) can be changed to effect the way the figure is generated
#a)
fig, ax = plt.subplots() 
draw_manyCircles(ax,3,[100,0],100,3)#change to w to 2 looks cool
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question4a.png')

#b)
fig, ax = plt.subplots() 
draw_manyCircles(ax,4,[100,0],100,3)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question4b.png')

#c)
fig, ax = plt.subplots() 
draw_manyCircles(ax,5,[100,0],100,3)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Question4c.png')
