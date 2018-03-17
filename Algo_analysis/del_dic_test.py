
import timeit
import random

_DEBUG = True
if _DEBUG == True:
    import pdb
    pdb.set_trace()

for i in range(10000,1000001,20000):
   # t=timeit.Timer("del x[random.randrange(len(x)-1)]","from __main__ import random,x")
    #t= timeit.Timer("del x[random.randrange(len(x)-1)]", "from __main__ import random, x")
    #x=list(range(i))
    #lst_time=t.timeit(number=1000)
    #t=timeit.Timer("del x[0]","from __main__ import random,x")
    x={j:None for j in range(i)}
    for j in range(len(x)-1):
        del x[j]
    #d_time=t.timeit(number=1000)
    #print("%d,%10.3f,%10.3f" % (i,lst_time,d_time))
    #print("%d,%10.3f" % (i,lst_time))
    #print("%d,%10.3f" % (i,d_time))
