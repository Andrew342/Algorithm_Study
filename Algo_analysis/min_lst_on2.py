import sys
import time
import random

def min_list(l):
    start=time.time()
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    end=time.time()
    return l[0],end-start

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



