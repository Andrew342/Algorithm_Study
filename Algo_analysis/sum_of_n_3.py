#-*-coding:utf-8-*-
import sys
import time 
from math import pow

def sum_of_n_3(n):
    start=time.time()
    the_sum=(n*(n+1))/2
    end=time.time()
    return the_sum,end-start

#n=1000000

for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n_3(int(sys.argv[1])*pow(10,i)))

