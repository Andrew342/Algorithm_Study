
from queue import Queue

class Printer:
    # Printer needs 3 attributes
    # 1,the print page rate;2,is there any taks now?;3,how long is it need to finished current task?
    def __init__(self,ppm):
        self.page_rate=ppm
        self.current_task=None
        self.time_ramaining=0
    
    # simulate time pass second by second
    def tick(self):
        if self.current_task!=None:
            self.time_remaining=self.time_remaining-1
            if self.time_remaining<=0:
                self.current_task=None
    # return Bolean whether printer is busy or not
    def busy(self):
        if self.current_task!=None:
            return True
        else:
            return False
    # how long a new task will take
    def start_next(self,new_task):
        self.current_task=new_task
        self.time_remaining=new_task.get_pages()*60/self.page_rate

import random

class Task:
    # task needs two attributes:1,start time;2,how many pages need to print
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    # get task time stamp
    def get_stamp(self):
        return self.timestamp
    # get how many pages of this task
    def get_pages(self):
        return self.pages
    # how much time need to wait to start this task
    def wait_time(self,current_time):
        return current_time-self.timestamp

# num_seconds: the period of simulation
# pages_per_minute: the print speed
def simulation(num_seconds,pages_per_minute):
    lab_printer=Printer(pages_per_minute)
    print_queue=Queue()
    waiting_times=[]

    for current_second in range(num_seconds):
        if new_print_task():
            task=Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task=print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait=sum(waiting_times)/len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait,print_queue.size()))

def new_print_task():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)
