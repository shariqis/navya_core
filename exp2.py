# class Lessthan10(Exception):
#     def __str__(self):
#         return "Enter NUmber greater than 10"
        
# try:
#     # a1=5/0
    
#     a=int(input("Enter the number greater than 10: "))
#     if a<10:
#         raise Lessthan10()
#     # b=int(input("Enter the number: "))    

# except ZeroDivisionError :
#     # print(ZeroDivisionError)
#     print("Enter a non zero value")
# # except ValueError as c:
# #     print(c)
# #     print("Enter a number")
# except Lessthan10 as t:
#     print(t)
#     print('mmmmmmmmmmmmmmm')
# else:
#     print("HELOOWORLD")
# finally:
#     print("finally")



x = "hello"

# # if condition returns True, then nothing happens:
# assert x == "hello1"

# #if condition returns False, AssertionError is raised:
assert x == "goodbye",'invalid'



