#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:01:40 2022

@author: usn
"""

def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

arr = [ 2,5,6,9,12,16,18,20,25,28,30]
x = 25

res = search(arr, x)

if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in array")