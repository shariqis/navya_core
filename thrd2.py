#Creating our own thread 
from threading import Thread
import time

 #Create a class as sub class to Thread class  
class MyThread(Thread):
#Override the run() method of Thread    
    def cube(self,b):
        # c= b
        for i in b:
            # print('--------',i)
            print("cube of : ",i**3)
            time.sleep(1)

    def run(self):
        # for i in range(1, 6):
        #     print(i)
        #     time.sleep(3)
        # print('/////////////////////////')
        a=(1,2,3,4)
        self.cube(a)
        # self.sq(a)
    
        # def sq(self,b):
    #     # c= b
    #     for i in b:
    #         # print('--------',i)
    #         print("sq of : ",i**2)
    #         time.sleep(1)    

    
class MyThread1(Thread):
#Override the run() method of Thread    

    def square(self,d):
    #     c=self.d
        for i in d:
            # print('--------',i)
            print("square of : ",i**2)
    #         print('---')
                
    #         print('===')
            time.sleep(2)# 
    def run(self):
        # for i in range(1, 6):
        #     print(i)
        #     time.sleep(3)
        a=(1,2,3,4)       
        self.square(a)
    

#Create an instance of MyThread class  
t1 = MyThread()
# t2= MyThread1()
#Start running the thread t1  
t1.start()
# t2.start()
#Wait till the thread completes its job  
t1.join()
# t2.join()



