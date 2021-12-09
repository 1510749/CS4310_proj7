import threading
import time
import random

n = 100
buffer = [0 for x in range(n)]


race_condition = "Race Condition Occurred"
def producer():
    next_in = 0
    while(1):
        k1 = random.randint(1,99)
        
        print("k1: " + str(k1))
        for j in range(k1):
            buffer[(next_in + j) % n] += 1
            if(buffer[(next_in + j) % n] >= 3): #IF value reaches 3, just exit because race condition will already have occurred
                return True
        next_in = (next_in + k1) % n
        print("PRODUCED: " + str(buffer))
        t1 = random.randrange(20,99) * .1  #pauses for 2.0-9.9 seconds
        print("TIME1: " + str(t1) + "s" )
        time.sleep(t1)

        




def consumer():
    next_out = 0
    while(1):
        t2 = random.randrange(20, 99) * .1 #pauses for 2.0-9.9 seconds
        print("TIME2: " + str(t2) + "s" )
        time.sleep(t2)
        k2 = random.randint(1,99)
        print("k2: " + str(k2))
        for k in range(k2):
            data = buffer[(next_out + k) % n]
            if (data > 1): # race condition detected; exit
                print(race_condition)
                print("IF: " + str(buffer))
                return True
            else:
                buffer[(next_out + k) % n] = 0
        next_out = (next_out + k2) % n
        print("CONSUMED: " + str(buffer))
            


class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.__flag = threading.Event()
        self.__flag.set()
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Starting " + self.name)
        if (self.threadID == 1):
            producer()
        else:
            consumer()
        print("Exiting " + self.name)

    def pause(self):
        self.__flag.clear()
    def resume(self):
        self.__flag.set()

try:
   thread1 = myThread(1, "Producer")
   thread2 = myThread(2, "Consumer")
   thread1.start()
   thread2.start()
except:
   print("Error: unable to start thread")
