import threading
import time
import random
import sys

n = 100
buffer = [0 for x in range(n)]


race_condition = "Race Condition Occurred"
def producer():
    next_in = 0
    while(1):
        
        k1 = random.randint(1,99)
        print("k1: " + str(k1))
        for j in range(k1):
            semae.acquire()
            buffer[(next_in + j) % n] += 1
            if(buffer[(next_in + j) % n] >= 3): # IF value reaches 3, just exit because race condition will already have occurred
                return True
            semaf.release()
        next_in = (next_in + k1) % n
        print("PRODUCED: " + str(buffer))
        
        #t1 = random.randrange(20,99) * .1   # Pauses for 2.0-9.9 seconds
        #print("TIME1: " + str(t1) + "s" )
        #time.sleep(t1)



def consumer():
    next_out = 0
    while(1):
        #t2 = random.randrange(20, 99) * .1  # Pauses for 2.0-9.9 seconds
        #print("TIME2: " + str(t2) + "s" )
        #time.sleep(t2)
        
        k2 = random.randint(1,99)
        print("k2: " + str(k2))
        for k in range(k2):
            semaf.acquire()
            data = buffer[(next_out + k) % n]
            if (data > 1): # Race condition detected; exit
                print(race_condition)
                print("IF: " + str(buffer))
                return True
            else:
                buffer[(next_out + k) % n] = 0
            semae.release()
        next_out = (next_out + k2) % n
        print("CONSUMED: " + str(buffer))
        

        


try:
    start = time.time()
    end = start + 10  # Force close after 10 seconds
    semaf = threading.Semaphore(0)
    semae = threading.Semaphore(n)
    thread1 = threading.Thread(target = producer)
    thread2 = threading.Thread(target = consumer)
    thread1.daemon = True # Make threads Daemons so they exit with the program
    thread2.daemon = True
    thread1.start()
    thread2.start()


    while(time.time() <= end):
        running = True # Just to have the program and threads only run for the duration of the timer
except:
   print("Error: unable to start thread")
