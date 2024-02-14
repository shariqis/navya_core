#  The try block lets you test a block of 
# code for errors.

# The except block lets you handle the error.

# The finally block lets you execute code, 
# regardless of the result of the try-
# and except blocks.

# x=12
# print(x)

# try:
#     # x=9
#     print(x)
# # except:
# #     print("error occurred"   )
# except NameError as u :
#     print("error occurred" , u)

# try:
#     # v=5
#     print(v)
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
# finally:
#     print('completed')



# try:
#     y=0
#     a=[3,65,4,2]
#     print(a[2])
#     print(y)
#     print(8/2)
  
# except NameError:
#   print("name error went wrong")
# except IndexError:
#     print('out of IndexError ')  
# except :
#     print('error')     
# else:
#     print('nnnnnnnnnnnnnn')
# finally:
#   print("The 'try except' is finished")   


x = -21

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")


x = 'string'
if not type(x) is int:  
  raise IndexError("Only integers are dfsdfsdfsdfdsf")   


# a=[2,5,2,6,4,2]
# print(a[9])