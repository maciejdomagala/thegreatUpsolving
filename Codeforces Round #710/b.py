
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter
from copy import deepcopy as dc


############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def insr2():
    s = input()
    return(s.split(" "))

def prime_factorization(n):

    if n == 1:
        return [1]

    ans=[]
    i = 2
    cap = sqrt(n)
    while i <= cap:
        if n % i == 0:
            ans.append(i)
            n = n//i
            cap=sqrt(n)
        else:
            i += 1
    if n > 1:
        ans.append(n)
    return ans

def binomial(n, k):
    if n == 1 or n == k:
        return 1

    if k > n:
        return 0       
    else:
        a = math.factorial(n)
        b = math.factorial(k)
        c = math.factorial(n-k)
        div = a // (b * c)
        return div 

#
# r = raw_input()
        
for _ in range(inp()):
    n, k = invr()
    s = raw_input()

    c = 0
    arr = []

    for i, a in enumerate(s):
        if a == '*':
            arr.append(i)

    if len(arr) == 1 or len(arr) == 2:
        print len(arr)
        continue

    i = 0

    while i < len(arr)-1:
        j = i+1

        while j < len(arr) and arr[j]-arr[i]<=k:
            j += 1

        c += 1
        i = j-1

    print c+1