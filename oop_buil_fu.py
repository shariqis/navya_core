####################  getattr() Function

# class Person:
#     name = "John"
#     age = 36
#     country = "Norway"

# v=Person()
# # print(v.name1)

# x = getattr(v, 'name','not exist')
# print(x)


# ###################### delattr 

# class Person:
#     name='John'
#     age=36
#     country='India'
# print(Person.age)   
# # # # # # x = getattr(Person, 'age','not present')
# # # # # # print(x) 
# # # # # # print(Person.name)    
# delattr(Person,'age')

# print(Person.age) 

# # a=Person()
# # print(a.age)
# # b=Person()
# # print(b.age)
# # delattr(Person, 'age')
# # print(b.age)

# ########################## hasattr() Function 
# # The hasattr() function returns True if the specified object
# #  has the specified attribute,
# #  otherwise False.

# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"

# x = hasattr(Person, 'age1')
# print(x)


# ####################### setattr() Function

# # The setattr() function sets the value of the specified attribute
# #  of the specified object.

# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"

# x = getattr(Person, 'age')
# print(x)
# setattr(Person, 'age1', 40)
# # setattr(Person, 'age', 22)
# # # # print('.............')
# # # # # # The age property will now have the value: 40
# x1 = getattr(Person, 'age')
# print(x1)
# x = getattr(Person, 'age1',"not exist")
# print(x)
# # setattr(Person, 'age1', 40)
# # y = getattr(Person, 'age1',"not exist")
# # print(y)


# ######################### issubclass() Function

# # The issubclass() function returns True if the specified object is 
# # a subclass of the specified object, otherwise False.


# class MyParent:
#   age = 36

# class myChild(MyParent):
#   name = "John"
#   age = 9

# x = issubclass(myChild,MyParent)

# print(x)



# ############################## super() Function

# # The super() function is used to give access to methods and 
# # properties of a parent or sibling class.

# # # The super() function returns an object that represents the parent class.

# class A:
#     def __init__(self):
#         print('welcome')

#     def show(self):
#         print('show')  

# class A1:
#     def __init__(self):
#         print('welcome1')

#     def show1(self):
#         print('show1')         
          

# class B(A,A1):

#     def __init__(self):
#         print('my b')
#         super().__init__()
#         super().show()
#         super().show1()
#         # A.__init__(self)

#     # def forContructor(self):
#     #     super().__init__()  
 

#     def display(self):
#         print('display')  
#         super().show()  

# # v= B()
# # # v.forContructor()
# # # v.display()  


# class A:
#     def __init__(self):
#         print('welcome')       
        
# obj=A()       
# # c= isinstance(obj,A)
# # print(c)
# v=isinstance(5.7,float)
# print(v)
# # print(type(obj))

# a=8
# print(type(a))

# c=isinstance("hai",(float,int,dict,list,str))
# print(c)



# class A:
#     def __init__(self):
#         print('welcome')

#     def show(self):
#         print('show')  

# class A1(A):
#     def __init__(self):
#         print('welcome1')

#     def show1(self):
#         super().show()
#         print('show1')   
        
# a=A1()
# a.show1()        



class cuper:
    _b="apple"
    var1=None #public
    _var2=None # protected
    __var3=None # private
    
    def __init__(self,v1,v2,v3):
        self.var1=v1
        self._var2=v2
        self.__var3=v3
    
    def displayPublic(self):  # public function
        print('pubic vaar... ', self.var1)            
        
    def _displayProtected(self):
        print('Protected vaar... ', self._var2)    
        
    def __displayPrrivate(self):
        print('Private vaar... ', self.__var3)
        
    def accessPri(self):
        self.__displayPrrivate()    
        

a=cuper('public', 'prot', 'pri')        


# print(a._b)
# a.displayPublic()
# a._displayProtected()
# a.accessPri()
# a.__displayPrrivate()
print(a.var1)
print(a._var2)
print(a.__var3)
