class Humen:    
    def study(self):
        print('humen study')
        
class Dancer(Humen):
    def study(self):
        print('dancer study')        
        
class Student(Dancer):    
    def study(self):
        print('student study') 
        # Dancer.study(self)      
        

ram=Student()
ram.study()
# kavya=Student()
