# -*- coding: utf-8 -*-
"""
Course: CS-2302 Data-Stuctures
Author: Julian Gonzalez
Assignment: Lab 2 
Intstuctor: Olac Fuentes
T.A's: Anindita Nath, Maliheh Zargaran
"""
import random
#Node Functions#######################################
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next        
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions###########################################
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.length +=1
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        L.length +=1
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()
    
def Prepend(L,x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.length+=1
    else:    
        L.head=Node(x,L.head)   
        L.length+=1
    
def getLength(L):
    temp = L.head
    count = 0
    while temp is not None:
        count+=1
        temp = temp.next
    return count
def search(L,i):
    cur = L.head
    count = 0
    
    while count != i:
        cur = cur.next
        count += 1
    return cur.item


#########################################################################
## BubbleSort
    
def bubbleSort(L):
    unsorted = True 
    while unsorted:#loops until the list has done every comparison it can
        temp = L.head 
        unsorted = False
        while temp.next is not None:
            if temp.item > temp.next.item:#swaps the the current item from the list if it is greater then the next tiem
                temp2 = temp.item
                temp.item = temp.next.item
                temp.next.item = temp2
                unsorted = True#keeps in the while loop as something was swapped
            temp = temp.next
                        
#############################################################
## MergeSort
def mergeSort(L):
    if L.length > 1:
        left = List()
        right = List()
        left,right=split(L,left,right)#calls the split function
        
        mergeSort(left)#
        mergeSort(right)
        
        temp = left.head
        temp2 = right.head
        while temp != None and temp2 != None:#this sorts the left and right list compared to each other 
            if temp.item < temp2.item:
                Append(L, temp.item)
                temp = temp.next
            else:
                Append(L, temp2.item)
                temp2 = temp2.next
        
        merge(L,temp,temp2)#merges left and right lists
        
            
def split(L,left,right):
    temp = L.head
    i=0
    while i < getLength(L)//2:#while loop to create a left list that is half the size of the L list
        Append(left, temp.item)
        Remove(L, temp.item)#removes from List so when right list is created it wont have left list numbers
        temp = temp.next
        i+=1
    while temp is not None:#while loop to add to right list from the remains of L list
        Append(right,temp.item)
        Remove(L,temp.item)
        temp = temp.next
        
    return(left,right)

def merge(L,left,right): 
    while left is not  None:#adds the items from the left list into the L list
        Append(L,left.item)
        left = left.next    
    while right is not None:#add the items from the right list to the L list 
        Append(L,right.item)        
        right = right.next      
#############################################################
## QuickSort
def quickSort(L):
    if L.length > 1:
        pivot = L.head.item#Item to be compared too
        left = List()
        right = List()
        temp = L.head.next
        while temp is not None:#sorts left and right list according to the pivot
            if temp.item < pivot:
                Append(left,temp.item)
            else:
                Append(right,temp.item)
            temp = temp.next
        #recusive calls to sort the lists again from less than pivot and greater and pivot
        quickSort(left)
        quickSort(right)
        
        if IsEmpty(left):#makes the pivot the last element of the left list
            Append(left,pivot)
        else:
            Prepend(right,pivot)#makes the pivot the first element of the right list
            
        if IsEmpty(left):#if somehow the left list becomes completly empty this makes the right list head and tail the equal to L
            L.head = right.head
            L.tail = right.tail     
        left.tail.next = right.head#merges the two list by having the tail of the left list the head of the right list
        L.head = left.head#makes parameter L head equal to left list head
        L.tail = right.tail#makes parameter L tail equal to right list tail

#############################################################
# ModQuickSort
def modQuickSort(L,m):    
    if L.length > 0:
        pivot = L.head.item#Item to be compared too
        left = List()
        right = List()
        temp = L.head.next
        while temp is not None:#sorts left and right list according to the pivot
            if temp.item < pivot:
                Append(left,temp.item)
            else:
                Append(right,temp.item)
            temp = temp.next
            
        if m==getLength(left) or (m==0 and m==getLength(left)):
            return pivot
        if m > getLength(left):
            return modQuickSort(right, m-getLength(left)-1)
        if m <= getLength(left):
            return modQuickSort(left, m)
##        if m < left.length:
##            return modQuickSort(left,m)
##        elif m==0 and m==getLength(left):
##            return pivot
##        elif m == left.length:
##            return pivot
##        else:          
##            return modQuickSort(right,m-left.length-1)
        
            
#############################################################

def newList(n):#function to create a list of n length with random ints in range of 1 to 100
    L = List()
    for x in range(0,n):
        num = random.randint(1,100)
        Append(L,num)

    return L    
L1 = List()
L2 = List()
L3 = List()
L4 = List()      
  
L1=newList(5)
L2=newList(5)
L3=newList(5)
L4=newList(5)

print('Bubble sort for list 1')
print('Unsorted List 1:', end=' ')
Print(L1)
bubbleSort(L1)
print('Sorted List 1:', end=' ')
Print(L1)
print('Median is',end=' ')
print(search(L1, L1.length // 2))

print()

print('Merge Sort for list 2')
print('Unsorted List 2:', end=' ')
Print(L2)
mergeSort(L2)
print('Sorted List 2:', end=' ')
Print(L2)
print('Median is',end=' ')
print(search(L2, getLength(L2) // 2))


print()

print('Quick Sort for list 3')
print('Unsorted List 3:', end=' ')
Print(L3)
quickSort(L3)
print('Sorted List 3:', end=' ')
Print(L3)
print('Median is',end=' ')
print(search(L3, L3.length // 2))

print()

print('Better Quick Sort for list 4')
print('Unsorted List 4:', end=' ')
Print(L4)
modQuickSort(L4,getLength(L4) // 2)
print('Sorted List 4:', end=' ')
Print(L4)
print('Median is',end=' ')
print(search(L4, L4.length // 2))




            
            
            
            
            
            
            
            
            
            
            
            
