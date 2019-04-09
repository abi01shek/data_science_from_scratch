import functools

height_weight_age = [70,170,40,60]
grades = [95,80,75,62]

def vector_add(v,w):
    """ adds corresponding elements"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
    """ subtracts corresponding elements """
    return [v_i-w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    """ sum all corresponding elements of all vectors """
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def vector_sum_reduce(vectors):
    """ do vector sum but with reduce method """
    return(functools.reduce(vector_add,vectors))

def scalar_multiply(c, v):
    """ multiply vector with scalar """
    return [c*v_i for v_i in v]

def vector_mean(vectors):
    """ compute vector whose ith value is mean of ith elements of input vectors """
    n = len(vectors)
    return (scalar_multiply(1/n, vector_sum(vectors)))

def dot(v,w):
    """ compute dot product how far vector v extends in w direction """
    return sum([v_i*w_i for v_i,w_i in zip(v,w)])

def sum_of_squares(v):
    """v_1 *v_1 + ... v_n*v_n """
    return dot(v,v)

import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def squared_distance(v,w):
    """ (v1-w1)**2 + (v2-w2)**2 .... """
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    """ sqrt of squared distance """
    return math.sqrt(squared_distance(v,w))


#print(vector_add(height_weight_age, grades))


## Vector sum
#vectors = [[1,2,3,4,5],[1,2,3,4,5],[2,4,6,8,10]]
#print(vector_sum_reduce(vectors))
#print(vector_mean(vectors))
    
## Scalar multipy
#print(scalar_multiply(4,[1,2,3,4]))
    
## Dot product 
#v = [1,2,3]
#w = [4,5,6]
##print(dot(v,w))
#print(sum_of_squares(v))
#print(magnitude(v))
#print(squared_distance(v,w))





