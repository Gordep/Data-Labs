# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:07:47 2019

@author: Julian
"""


import matplotlib.pyplot as plt

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
def draw_BinaryTree(ax,x,y,s,w,T):#x,y coordinates, then a scaler s for the whole tree and w for the width of it, T being th BST
    if T is not None:
        c= plt.Circle([x,y], 1.5, color='k', fill=False)#uses matplotlib circle function to draw a circle for each node
        ax.add_artist(c)#adds the circle into the figure
        ax.text(x-.7, y-.5, T.item, size=6) #prints the valute of the current node
        if T.left is not None:#prints the left side of the tree
            xL=[x,x-(s*s)]
            yL=[y-1.5,y-w]
            ax.plot(xL,yL,color='k')
            
            draw_BinaryTree(ax,x-(s*s),y-w-1.5,s-1,w,T.left)
        if T.right is not None:#prints the right side of the tree
            xR = [x,x+(s*s)]
            yR = [y-1.5,y-w]
            ax.plot(xR,yR, color='k')
            draw_BinaryTree(ax,x+(s*s),y-w-1.5,s-1,w,T.right) 
            
def IterSearch(T,k):
    while T is not None:
        if k == T.item:## if the current node of the tree is k return current node T
            return T
        elif k > T.item:#checks if k is greater than current node item if it is continues to the right of the tree
            T = T.right
        else:#if all other checks fail it will defualt to looking in the left tree
            T = T.left
    print('Could not find k inside the list, inserting k into list')
    T = Insert(T,k)# doesnt actually insert into the main list 
    return T

def insertBBT(B):
    if len(B) != 0:#checks the length of the B list if its 0 it returns
        pivot = len(B)//2#The mid point of the list evertime used for inserting at every recusive call
        temp = BST(B[pivot])#creates the binary tree with the root being pivot 
        temp.right = insertBBT(B[pivot+1:])#call to insert to the right of the binary tree
        temp.left = insertBBT(B[:pivot])#call to insert to the left of the Binary tree
        
        return temp #returns the completed tree
    
def extractor(T,List):
    if T is not None:
        extractor(T.left,List)### traverses all the way to the left side of the tree(smalles varible)
        List.append(T.item) #adds the current node item into the list
        extractor(T.right,List)### starts to traverse the right side of the tree then adds on the the list
        
def printAtDepth(T,d):
    if T is not None:
        if d == 0:# prints the items at depth d
            print(T.item)
        else:
            printAtDepth(T.left,d-1)#goes to the left subtree to print items at depth d 
            printAtDepth(T.right,d-1)#goes to the right subtree to print items at depth d 
# Code to test the functions above
  

T = None
A = [10,4,15,2,8,1,3,5,9,7,12,18]
for a in A:
    T = Insert(T,a)   
#####################################
print('------------------------------------------')
print("Question 1")
#1)
print("Printing Binary Tree...")
fig, ax = plt.subplots()    
draw_BinaryTree(ax,0,0,4.5,15,T) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

######################################
print('------------------------------------------')
print("Question 2")
#2) Iterative search
s= 15 ## change to find desired value
x = IterSearch(T,s).item
msg = 'Looking for ' + repr(s) + ': ' + repr(x)
print(msg)

#####################################
print('------------------------------------------')
print("Question 3")
#3) Build a balanced  binary tree with sorted list
B = [1,2,3,4,5,6]
T2 = insertBBT(B)
print("Printing Binary Tree...")
fig, ax = plt.subplots()    
draw_BinaryTree(ax,0,0,4.5,15,T2) #DONT FORGET TO USE DRAG TO TO LOOK AT WHOLE FIGURE
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

#####################################
print('------------------------------------------')
print("Question 4")
#4)Extract elements of BST into a sorted list
emptyList = []
extractor(T,emptyList)
print(emptyList)

####################################
print('------------------------------------------')
print("Question 5")
#5)Print depths
depth = 2 ##choose which depth to print out
msg2 = 'Keys at depth ' + repr(depth) + ': '
print(msg2)
printAtDepth(T,depth)




