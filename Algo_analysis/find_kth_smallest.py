

def find_kth_smallest_num(l,k):
    s=[]
    for i in range(k):
        res=float('inf')
        for item in l:
            if res>item:
                res=item
        if res in l:

            if i!=k-1:
                l.remove(res)
            else:
                 return l[0]
        else:
            print("res is {} and not in l".format(res))

import timeit
import random

for i in range(1000,100001,1000):
    t=timeit.Timer("find_kth_smallest_num(x,random.randint(10,1000))","from __main__ import random,x,find_kth_smallest_num")
    x=[j*random.randint(1,10) for j in range(i)]
    find_time=t.timeit(number=100)


'''if __name__=="__main__":
    l=[1,2,3,4,5,6,7,8,9]
    k=3
    print("the {}th min num is {}".format(k,find_kth_smallest_num(l,k)))'''
