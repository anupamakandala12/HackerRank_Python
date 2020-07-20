#!/usr/bin/env python
# coding: utf-8
Pairs amazon 1
You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.

For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: , , and .

Function Description

Complete the pairs function below. It must return an integer representing the number of element pairs having the required difference.

pairs has the following parameter(s):

k: an integer, the target difference
arr: an array of integers
# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    n=len(arr)
    count1=0
    count2=0
    for i in range(0,n):
        for j in range(i+1, n):
            if(arr[i]-arr[j]==k):
                count1+=1
                print(arr[i],arr[j])
                print('count1 is ',count1)
            elif(arr[j]-arr[i]==k):
                count2+=1
                print(arr[i],arr[j])
                print('count2 is ',count2)
    return(count1+count2)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

