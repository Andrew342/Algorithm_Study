

def find_kth_smallest_num(l,k):
    s=[]
    res=float('inf')
    for i in range(k):
        for item in l[i:]:
            if res>item:
                res=item
    return l[k-1]


import timeit
import random
for i in range(100,1001,100):
    t=timeit.Timer("find_kth_smallest_num(x,k)","from __main__ import random,x,k,find_kth_smallest_num")
    x=[j*random.randint(1,10) for j in range(i)]
    k=random.randint(10,len(x))
    find_time=t.timeit(number=100)
    print("the {} th num is {} required time {}".format(k,find_kth_smallest_num(x,k),find_time*(10000/i)))


'''
if __name__=="__main__":
    import random
    for i in range(30):
        l=[j for j in range(100)]
        k=random.randint(0,100)
        #l=[1,2,3,4,5,6,7,8,9]
        #k=3
        _DEBUG=False
        if _DEBUG==True:
            import pdb
            pdb.set_trace()
        print("the {}th min num is {}".format(k,find_kth_smallest_num(l,k)))'''
