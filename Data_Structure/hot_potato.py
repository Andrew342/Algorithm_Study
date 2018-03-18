
from queue import Queue

def hot_potato(name_list,num):
   sim_queue=Queue()
   for name in name_list:
        sim_queue.enqueue(name)

   while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()# for every num, dequeue one

   return sim_queue.dequeue()

_DEBUG=True
if _DEBUG==True:
    import pdb
    pdb.set_trace()

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
