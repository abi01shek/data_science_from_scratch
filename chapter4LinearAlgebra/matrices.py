#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:53:06 2019

@author: ramdas
"""
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A,i):
    return(A[i])
    
def get_column(A,j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """ create a matrix with num rows and num columsn following the function entry_fn """
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]


def is_diagonal(i,j):
    """ return 1 if i==j else return 0 """
    return 1 if i==j else 0

### Matrices
A = [[1, 2, 3], # A has 2 rows and 3 columns
     [4, 5, 6]]
B = [[1, 2],
     [3, 4],
     [5, 6]]

print(shape(A))
print(get_column(B,1))
    
print(make_matrix(4,4,is_diagonal))

