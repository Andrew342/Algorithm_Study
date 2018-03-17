
import timeit
import random

for i in range(10000,1000001,20000):
    t=timeit.Timer("x.get(%d)" % i,"from __main__ import random,x")
    x={j:None for j in range(i)}
    get_time=t.timeit(number=1000)
    p=timeit.Timer("x[%d]=1" % i,"from __main__ import random,x")
    x={j:None for j in range(i)}
    set_time=p.timeit(number=1000)
    print("%d,%10.8f,%10.8f" % (i,get_time,set_time))
