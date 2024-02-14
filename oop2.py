class Humen:
    legs=2  # class variable
    eyes=2
    
    def __init__(self,n,p): # construnctor
        self.name=n  #instance variable
        print(n,'is humen')
    
    def walking(self):
        print(self.name,' can walk  ') 
        return 'hiiii' 
        
    def __del__(self):
        print(self.name,'deleted----------------')    
        
anu=Humen('anu thomas','eklm')    
del anu
kiran=Humen('kiran P','tvm')
print('.....................')
anu.walking()  
n=kiran.walking()
print(n)