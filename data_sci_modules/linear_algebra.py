import math
import functools

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


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def squared_distance(v,w):
    """ (v1-w1)**2 + (v2-w2)**2 .... """
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    """ sqrt of squared distance """
    return math.sqrt(squared_distance(v,w))

