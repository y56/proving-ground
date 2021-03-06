#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:28:12 2019
DSA HW 2
problem 1
@author: y56
"""
def G(A, p, q, r):
    
    print("G", p, q, r)

    if (p > q) or ((q + 1) > r):
        print("Use -inf to discard this term.")
        return -99997

    # grow left from q-1 until p to maximize 
    # grow right from q until r-1 to maximize
    # p <--- q || q+1 ---> r

    leftSum = A[q] 
    leftMax = leftSum
    i = q - 1
    while i >= p:
        leftSum += A[i]
        if leftSum > leftMax:
            leftMax = leftSum
        i -= 1
    
    rightSum = A[q + 1]  
    rightMax = rightSum
    i = q + 2
    while i <= r:
        rightSum += A[i]
        if rightSum > rightMax:
            rightMax = rightSum
        i += 1
        
    return leftMax + rightMax
    
def H(A, p, q, r, l):
    
    print("H", p, q, r, l)

    if (p > q) or ((q + 1) > r) or ((r + 1) > l):
        print("Use -inf to discard this term.")
        return -99998
    
    # grow left from q-1 until p to maximize 
    # grow right from q until r-1 to maximize
    # p <--- q || q+1 ~ r || r+1 ---> l
    
    leftSum = A[q] 
    leftMax = leftSum
    i = q - 1
    while i >= p:
        leftSum += A[i]
        if leftSum > leftMax:
            leftMax = leftSum
        i -= 1
    
    rightSum = A[r + 1]  
    rightMax = rightSum
    i = r + 2
    while i <= l:
        rightSum += A[i]
        if rightSum > rightMax:
            rightMax = rightSum
        i += 1
    
    return leftMax + rightMax + sum(A[q + 1 :r + 1])
    
def F(A, p, l):
    print("F", p, l)

    if p > l:  # should never happen
        print("Use -inf to discard this term.")
        return -99999
    
    if p == l:
        return A[p]
    
    q = int(p + (l - p) * 1 / 3)
    r = int(p + (l - p) * 2 / 3) + 1  # This `+ 1` is crucial.
    # Otherwise, we will never generate A[0]+A[1] to compare with others
    
    print("             p, q, r, l =", p, q, r, l) 
    
    s1 = F(A, p, q)
    s2 = F(A, q + 1, r)
    s3 = F(A, r + 1, l)
    s12 = G(A, p , q, r)
    s23 = G(A, q + 1, r, l)
    s123 = H(A, p, q, r, l)
    
    print([s1, s2, s3, s12, s23, s123])
    
    return max(s1, s2, s3, s12, s23, s123)

A = [2, 13, -3, -2, -2, 4, -6, -10, -14, -17]
print(F(A, 0, len(A) - 1))
