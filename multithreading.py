'''
import time
def cal_cube(no):
    time.sleep(2)
    for i in no:
        print(i*i*i)
def cal_sq(number):
    time.sleep(2)
    for i in number:
        print(i*i)
t=time.time();
arr=[1,2,3]
cal_cube(arr)
cal_sq(arr)
print("Time:", time.time()-t)
'''

'''
import threading
import time
class Hello(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class Hi(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1=Hello()
t2=Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("bye")
'''

'''
import threading
import time
class myThread(threading.Thread):
    def __init__(self,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID=threadID;
        self.name=name;
        self.counter=counter
    def run(self):
        print("starting: "+self.name)
        print_time(self.name,5,self.counter)
        print("Exiting "+self.name)
def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s,%s"%(threadName,time.ctime(time.time())))
        counter-=1
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread1.start()
thread1.join()
thread2.start()
thread2.join()
'''

'''
import threading
import time
class mythread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        print("start it: ",self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()
def print_time(threadname,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s,%s"%(threadname,time.ctime()))
        counter-=1
threadLock=threading.Lock()
#threads=[]
thread1=mythread(1,"thread-1",0.2)
thread2=mythread(2,"thread-2",0.2)
thread1.start()
thread2.start()

#threads.append(thread1)
#threads.append(thread2)
#for t in threads
#    t.join()
thread1,thread2.join()
print("Exiting Main Thread")
'''


'''
import threading
import time
def print_time(threadname,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s,%s"%(threadname,time.ctime()))
        counter-=1
class mythread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID;
        self.name=name;
        self.counter=counter;
    def run(self):
        print("starting: "+self.name)
        threadLock.acquire();
        print_time(self.name,self.counter,4)
        threadLock.release();
threadLock=threading.Lock()
thread1=mythread(1,"thread-1",0.2)
thread2=mythread(2,"thread-2",0.2)
thread1.start()
thread2.start()
thread1,thread2.join()
print("exiting")
'''


import queue
import threading
import time
exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
         queueLock.acquire()
         if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
         else:
            queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print( "Exiting Main Thread")


