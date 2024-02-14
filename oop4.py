class Humen:
    def __init__(self,name,place):
        self.name=name
        self.place=place
        
    def print_details(self):
        print('i am',self.name,'from ',self.place)    
        
        
class Dancer(Humen):
    def __init__(self,tech,form,n,p):
        self.tec=tech
        self.form=form
        Humen.__init__(self,n,p)       
        
    def dance_details(self):
        print('i am ',self.name,'my techer is ',self.tec,'my dance form is ',self.form)           
        
        
anu=Dancer('Shobhana', 'kathak','anu','pta')  
kavya=Dancer('thara', 'mohiniyattam','kavya','kollam')   

print('.....................................................')

kavya.dance_details()      
# kavya.print_details() 
print('////////////////////////////////')
anu.dance_details()      
# anu.print_details()   