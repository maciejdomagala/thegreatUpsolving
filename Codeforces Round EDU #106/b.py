
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter
from copy import deepcopy as dc
# from statistics import median, mean


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

def small_divisor(n):

    if n % 2 == 0:
        return 2

    i = 3
    while i*i <= n:
        if n%i == 0:
            return i
        i += 2

    return n 

for _ in range(inp()):
    s = insr()
    f = False
    fout = True

    for i in range(1, len(s)):
        if s[i-1] == s[i] and s[i] == '1':
            f = True
        if s[i-1] == s[i] and s[i] == '0' and f == True:
            print 'NO'
            fout = False
            break

    if fout:
        print 'YES'
