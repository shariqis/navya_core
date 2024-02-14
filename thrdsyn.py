
import threading
x = 0
# lock
def increment(lock):
    global x      
    for i in range(100000):
        lock.acquire()
        x+=1
        # print(x)
        lock.release()  
         


          
def main_task():
    global x
    x = 0
    lock = threading.Lock()
    # t1 = threading.Thread(target=increment)
    # t2 = threading.Thread(target=increment)
    t1 = threading.Thread(target=increment,args=(lock,))
    t2 = threading.Thread(target=increment,args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

for i in range(10): 
    main_task()        
    print("Iteration {0}: x = {1}".format(i,x)) 








