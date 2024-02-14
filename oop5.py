# from abc import ABC ,abstractmethod 
# class Polygen(ABC):
#     def details(self):  # non abstract mthd
#         print('hiiiiiiiiii')
#     @abstractmethod    
#     def area(self):  # abstract mthd
#         pass    
        
        
# class Triangle(Polygen):
#     def area(self):
#         print('tri area')
        
        
# class Rectangel(Polygen):
#     pass        
# t1=Triangle()
# r=Rectangel()
       
    

class Humen:
    def study(self):
        print('humen study')       
        
class Student(Humen):

        
    def study(self):
        print('student study111') 
    def study(self,a ,b):
        print('student study111')      
            
anu=Student()    
anu.study()          