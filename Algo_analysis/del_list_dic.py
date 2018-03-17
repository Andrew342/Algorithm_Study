
import timeit
import random

for i in range(10000,1000001,20000):
   # t=timeit.Timer("del x[random.randrange(len(x)-1)]","from __main__ import random,x")
    t= timeit.Timer("del x[random.randrange(len(x)-1)]", "from __main__ import random, x") # this not working with dic,because the key might be deleted in last operation. While it's ok for list. The list index is continutous.
    #x=list(range(i))
    #lst_time=t.timeit(number=1000)
    #t=timeit.Timer("del x[0]","from __main__ import random,x")
    x={j:None for j in range(i)}
    d_time=t.timeit(number=1000)
    #print("%d,%10.3f,%10.3f" % (i,lst_time,d_time))
    #print("%d,%10.3f" % (i,lst_time))
    print("%d,%10.3f" % (i,d_time))
