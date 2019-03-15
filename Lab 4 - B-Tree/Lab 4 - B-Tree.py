# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:22:29 2019

@author: Julian
Assignment: Lab 4
Instructor: Fuentes, Olac
T.A: Nath, Anidita

Purpose is to further expand the capablities of given B-tree code
"""
# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Last modified February 28, 2019
import math

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
def height(T):##used code that was provided on class page
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
                
def Extractor(T,L):
    if T.isLeaf:
        return L.extend(T.item)#extend add the items if used append the list would be added
    for i in range(len(T.child)):##for loop to iterate through th entire b tree
        Extractor(T.child[i],L)    

def LargestAtDepth(T,d):
    if d==0:# base case for the depth 
        return T.item[-1]
    if T.isLeaf:#if we reach a leaf before reaching 0 for the depth return negative infinity 
        return -math.inf
    else:
        return LargestAtDepth(T.child[-1], d-1)#searches the right most side of the tree for the largest item 
    
def SmallestAtDepth(T,d):
    if d==0 :# base case for the depth 
        return T.item[0]
    if T.isLeaf:#if we reach a leaf before reaching 0 for the depth return negative infinity
        return -math.inf
    else:
        return SmallestAtDepth(T.child[0],d-1)#searches the left most side of the tree for find the smallest item

def NumAtDepth(T,d):
    if d ==0:# base case for the depth 
        c = 0
        for t in T.item:#iterates the current node and counts the number of items in that depth 
            c += 1
        return c
    if T.isLeaf:# 
        return -math.inf #if we reach a leaf before reaching 0 for the depth return negative infinity
    if not T.isLeaf:#if not leaf we iterate through the whole tree to find the current depth
        c = 0
        for i in range(len(T.child)):
            c += NumAtDepth(T.child[i],d-1)
        return c #returns items the the depth 
    return -math##i dunno what this does?
            
def PrintAtDepth(T,d): # Prints all items in b-tree with root T that have depth d
    if d ==0:
        for i in T.item:#prints the items of the current depth 
            print(i,end=' ')
    if not T.isLeaf:#iterates the tree to find the correct depth 
        for i in range(len(T.child)):
            PrintAtDepth(T.child[i],d-1)
def FullNodes(T):
    c = 0
    if len(T.item) == T.max_items:#if current node is equal to the max items return add one to counter
        c +=1
    if T.isLeaf: #if the current node is a leaf return count 
        return c
    for i in range(len(T.child)):#iterates the whole tree 
        c += FullNodes(T.child[i])
    return c# final return for the final amount of full nodes

def FullLeafs(T):
    c = 0
    if len(T.item) == T.max_items and T.isLeaf:#checks the len of current node against max items then checks if its a leaf 
        c +=1
    if T.isLeaf:# if the first case is not met and is a tree return cound 
        return c
    for i in range(len(T.child)):#iterate through the entire tree 
        c += FullNodes(T.child[i])
    return c    
        
def FindDepth(T,k):
    if k in T.item:# base case if k is in the node of t
        return 0
    if T.isLeaf:#base case to check if t is a leaf
        return -1
    if k >T.item[-1]:#case to search through the right side of the Tree
        d = FindDepth(T.child[-1],k)
        if d == -1:#after searching will return -1 if d==-1 
            return -1
        return 1+d #if not return d 
    for i in range(len(T.item)):#for loop to search rest of the tree 
        if k <T.item[i]:
            d = FindDepth(T.child[i],k)
            if d == 0:
                return d+1   
    if d<0:
        return -1
    return d+1
        
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
#L = [1,2,3,4,5,1,1,1,1,1,6,6,6,6,6,6,2]
#L = [1,2,3,4,5,6,3,3,3,1,4,5,6,5,4,4,4,5,7,8,4,9,10,11,12,13,14,15]   
T = BTree()    
for i in L:
    #print('Inserting',i)
    Insert(T,i)
    #PrintD(T,'') 
    #Print(T)
    #print('\n####################################')
PrintD(T,'') 
#1
print('\n####################################')
print(height(T))    

#2
print('\n####################################')
emptyList = []
Extractor(T,emptyList)
print(emptyList)

#3
print('\n####################################')
print(SmallestAtDepth(T,1))

#4
print('\n####################################')
print(LargestAtDepth(T,1))

#5
print('\n####################################')
print(NumAtDepth(T,1))

#6
print('\n####################################')
PrintAtDepth(T,1)

#7
print('\n####################################')
print(FullNodes(T))

#8
print('\n####################################')
print(FullLeafs(T))
#9
print('\n####################################')
print(FindDepth(T,105)) 
