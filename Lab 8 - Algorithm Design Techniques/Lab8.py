# -*- coding: utf-8 -*-
"""
Course: CS-2302 Data-Stuctures
Author: Julian Gonzalez
Assignment: Lab 8
Intstuctor: Olac Fuentes
T.A"s: Anindita Nath, Maliheh Zargaran

"""
import random
import math
import numpy as np
import time
from mpmath import * #not needed
#import mpmath #not needed

#used to find which trig identities are equal
def discover(iden):
    x = 200
    for i in range(x):
        y = random.randint(0,len(iden)-1)#random number from 0 to length of the Trig identity list
        z = random.randint(0,len(iden)-1)
        if y != z: #check if the idicies are not equal
            if testIden(iden[y],iden[z]):#call testIden function
                print(f"Try {i}. {iden[y]} and {iden[z]} are equal")

def testIden(f1,f2,tries=1000,tolerance=0.0001):#used code provided in class modified to work for trig identities
    for i in range(tries):
        t = random.uniform(-math.pi,math.pi)#throws never used error ignore#random num from -pi to pi to be used by the identities
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True

def subsetsum(S,last,goal):#modified version of given class code (only changed the range of last-1 )
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last-1]) # Take S[last] #changed to last-1
    if res:
        subset.append(S[last-1])#changed to last-1
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]
    
def subPartition(S): 
    sumS = sum(S) #first get the sum of the entire list
    if sumS % 2 != 0:# check if sum of s is odd if yes then return false cannout have two equal subsets with odd sum 
        return False 
    
    return subsetsum (S,len(S), sumS // 2) #call subsetsum function given to us in class (subset with half of the total sum)

        
trigIden = ["sin(t)","cos(t)","tan(t)","sec(t)","-sin(t)","-cos(t)","-tan(t)",
            "sin(-t)","cos(-t)","tan(-t)","sin(t)/cos(t)","2*sin(t/2)*cos(t/2)",
            "sin(t)*sin(t)","1-(cos(t)*cos(t))","(1-cos(2*t))/2","1/cos(t)"
            ]
start = time.time()
discover(trigIden)
end = time.time()
print('Time:',end-start)

print()

S = [3,2,1,3,3]#[2, 4, 5, 9, 12]#[3, 1, 1, 2, 2, 1]#[1, 3, 5, 9, 12]

start1 = time.time()
tup= subPartition(S)#have to use tuple
end1 = time.time()
print('Time:',end1-start1)


s1= tup[1]#take the array out of the tuple
s2 = S.copy() #copy of old array used for finding other partion

if tup[0]:
    for i in s1:
        s2.remove(i)#removes the first occurance of a number from subset one
    print(f"{tup[0]} there exist a partition {s1} and {s2} in {S}")
    
else:
    print(f"{tup[0]} there exist no partition")


