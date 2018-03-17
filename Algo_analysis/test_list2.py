
import timeit
from timeit import Timer
pop_zero=Timer("x.pop(0)","from __main__ import x")
pop_end=Timer("x.pop()","from __main__ import x")

#x=list(range(2000000))
#print("pop_zero time is {}".format(pop_zero.timeit(number=1000)))
#x=list(range(2000000))
#print("pop_end time is {}".format(pop_end.timeit(number=1000)))

print("pop (0) pop()")
for i in range(1000000,100000001,1000000):
    x=list(range(i))
    pt=pop_end.timeit(number=1000)
    x=list(range(i))
    pz=pop_zero.timeit(number=1000)
    print("%15.5f,%15.5f" % (pz,pt))
