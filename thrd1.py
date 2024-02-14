import threading
import time
a=[1,2,3,4]
def cube(a1):
    for i in a1:
        print("cube of : ",i**3)
        time.sleep(1)        
def square(a):
     for i in a:
        print("square of : ",i**2)
        # print('---')
        print(threading.currentThread())        
        # print('===')
        time.sleep(1)# # # # # creating thread 
t1 = threading.Thread(target=cube,args=(a,))
t2 = threading.Thread(target=square,args=(a,))# # # #  # starting thread 1 
t1.start()# # # #  # starting thread 2
t2.start()
t1.setName("cube thread")
t2.setName("squre thread")
print(threading.enumerate())
# # # # #   # wait until thread 1 is completely executed 
t1.join()
# # # # #  # wait until thread 2 is completely executed
t2.join()
# # # # #  # both threads completely executed 
# # # # # print("Program executed!!!!!!!")


# cube(a)
# square(a)