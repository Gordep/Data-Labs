# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 19:54:48 2019

@author: Julian
Assignment: Lab 5
Instructor: Fuentes, Olac
T.A: Nath, Anidita
"""
import time
import math
import numpy as np

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T is None:
        T =  BST(newItem)
    elif T.item[0] > newItem[0]:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def IterSearch(T,k):
    while T is not None:
        if T.item[0] == k:## if the current node of the tree is k return current node T
            return T.item[1]
        elif T.item[0] > k:#checks if k is greater than current node item if it is continues to the right of the tree
            T = T.left
        else:#if all other checks fail it will defualt to looking in the left tree
            T = T.right
    print('Could not find k inside the list, inserting k into list')
    T = Insert(T,k)# doesnt actually insert into the main list 
    return T

def height(T):
	if T is not None: #base case
		return 1+max([(height(T.left)),height(T.right)]) 
	

def numNodes(T):
    if T is not None:
        return 1 + numNodes(T.left)+numNodes(T.right)
    return 0 

def similarBST(T,w1,w2):
    ww1 = IterSearch(H,w1)#finds the word in the bst
    ww2 = IterSearch(H,w2)
    top = 0#dot product
    bottom_a = 0#mag 1 
    bottom_b = 0#mag 2
    for i in range(len(ww1)):#does the formula to find magnitude
        top += float(ww1[i]) * float(ww2[i])
        bottom_a += float(ww1[i]) ** 2
        bottom_b += float(ww2[i]) ** 2

    bottom_a = math.sqrt(bottom_a)
    bottom_b = math.sqrt(bottom_b)    
###########################################################
class HashTableC(object):
    def __init__(self,size):  
        self.item = []
        self.numItems = 0#Tracks bumber of items in the entire hash 
        for i in range(size):
            self.item.append([])

def CalFactor(H):#calculates load factor
    return H.numItems / len(H.item)
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    if CalFactor(H) >= 1.0: ## checks the load factor if greater than increase the size of the hash
        for i in range(len(H.item)+1):
            H.item.append([])
        b = h(k,len(H.item))
    
    H.item[b].append([k,l])  ##MIGH NOT NEED L
    H.numItems = H.numItems + 1#increases to keep track
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return H.item[b][i][1]
    return -math.inf

def percentage(H):
    c = 0
    for i in range(len(H.item)):
        if len(H.item[i])==0:
            c = c +1       
    #print(c)
    return c / len(H.item)*100

def similar(H,w1,w2):
    ww1 = FindC(H,w1)#finds the word in the heap with its embedding
    ww2 = FindC(H,w2)
    top = 0#dot product
    bottom_a = 0#mag 1 
    bottom_b = 0#mag 2
    for i in range(len(ww1)):#does the formula to find magnitude
        top += float(ww1[i]) * float(ww2[i])
        bottom_a += float(ww1[i]) ** 2
        bottom_b += float(ww2[i]) ** 2

    bottom_a = math.sqrt(bottom_a)
    bottom_b = math.sqrt(bottom_b)

    return top / (bottom_a * bottom_b)

def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def reCompute(H):
    temp = HashTableC(len(H.item))      
    for i in range(len(H.item)):
        for j in range(len(H.item[i])):
            InsertC(temp,H.item[i][j][0],H.item[i][j][1])
    return temp
#file = "smaller_file.txt"
file = "glove.6B.50d.txt"
size = 10
H = HashTableC(size)
print('Choose implementation:')
c = int(input("(1-Hash || 2-BST)"))

if c == 1:
    print("Building a hash table with chaining")
    start = time.time()
    with open (file,encoding='utf8') as file:## makes the hashtable from a file
        for l in file:
            string = l.split(' ')
            word = l.split(' ')[0]#gets position 0 of L (like a list)
            emb = string[1:-1]#embed from beginning+1 to end of file 
            InsertC(H,word,emb)
    print("Hash Table stats:")
    print("Initial Size:",size)
    print("Final Size:",len(H.item))
    print("Elements in the Table:",H.numItems)
    print("Load Factor:",CalFactor(H))
    print("Percentage of empty list:",percentage(H)) 
    print("Standard deviation of the lengths of the lists:",0)###DO THIS
    Hre = reCompute(H)
    print("\n Reading word file to determine similarities\n")
    with open("similarities.txt",) as compares:
        for line in compares:
            string2 = line.split()
            print(string2[0] + " " + string2[1]+ " ")
            print(str(similar(Hre, string2[0], string2[1])))

    end = time.time()
    print("Running time",end-start )            

if c == 2:
    T = None
    print("Building binary search tree")
    start2 = time.time()
    with open (file,encoding='utf8') as file:## makes the hashtable from a file
        for l in file:
            string = l.split(' ')
            word = l.split(' ')[0]#gets position 0 of L (like a list)
            emb = string[1:-1]#embed from beginning+1 to end of file 
            T= Insert(T,word)
    print("BST stats:")
    print("Num of Node:",numNodes(T))
    print("Height:",height(T))
    end2 = time.time()
    print("Running time of building tree",end2-start2)            
    with open("similarities.txt",) as compares:
        for line in compares:
            string2 = line.split()
            print(string2[0] + " " + string2[1]+ " ")
            print(str(similarBST(T, string2[0], string2[1])))
      
    
else:
    print("not a valid input")
