import sys
sys.path.append('/home/ramdas/Work/Learning/dataScienceFromScratch/data_sci_modules/')


from linear_algebra import *
from collections import Counter
import math

## Central tendencies
def mean(v):
    """ calculate the mean of all values in a vector """
    return sum(v)/len(v)

def median(v):
    """ calculate median of a value v """
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2

    if(n % 2 == 1):
        return sorted_v[midpoint]
    else:
        lo = midpoint-1
        hi = midpoint+1
        return (sorted_v[hi] + sorted_v[lo])/2


def quantile(x,p):
    """ return p% from x """
    p_index = int(p*len(x))
    return sorted(x)[p_index]

def mode(x):
    """ return the most common value in x """
    counts = Counter(x)
    max_counts = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_counts]



### Dispersion
def data_range(x):
    """ max of vector - min of vector """
    return max(x)-min(x)

def de_mean(x):
    """ deviation from the mean for each value in input vector """
    x_bar = mean(x)
    return [ x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations)/(n-1)

def standard_deviation(x):
    """ sqrt of variance """
    return math.sqrt(variance(x))

def interquartile_range(x):
    """ value at index for 75% - value at index for 25% """
    return (quantile(x,0.75) - quantile(x,0.25))


## CORRELATION
def covariance (x, y):
    """ How two variables vary in tandem from their means """
    n = len(x)
    return dot(de_mean(x), de_mean(y))/(n-1)

def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y >0:
        return covariance(x,y)/ stdev_x /stdev_y
    else:
        return 0



## Test cases
num_friends = [100,49,41,40,25]
num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)


## Examples for central tendencies
#print(median(num_friends))
#print(quantile(num_friends,0.10))
#print(mode(num_friends))

## Examples for dispersion
#print(data_range(num_friends))
#print(de_mean(num_friends))
#print(variance(num_friends))
#print(standard_deviation(num_friends))


## Examples for correlation
daily_minutes = [110,69,51, 50, 35]
print(covariance(num_friends,daily_minutes))
print(correlation(num_friends,daily_minutes))
