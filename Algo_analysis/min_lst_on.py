import sys
import time
import random

def min_list(l):
    res=float('inf')
    start=time.time()
    for num in l:
        if num<res:
            res=num
    end=time.time()
    return res,end-start

def get_list(n):
    # produce a random list contains n nums
    l=[]
    for i in range(n):
       l.append(random.randint(0,n))
    return l

_DEBUG = False
if _DEBUG == True:
    import pdb
    pdb.set_trace()

l=get_list(int(sys.argv[1]))
#print("the list is {}".format(l))
print("the min num is %d and required time is %10.7f" % min_list(l))



