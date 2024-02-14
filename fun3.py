# x=0
# def hi():    
#     global x 
#     x+=1  
#     print(x)
    
# hi()    
# hi()    
# hi()    


# def area(r):
#     a=3.14*r**2
#     return(a)
# rad=int(input('enter radius : '))
# c_a=area(rad)
# print('area -> ',c_a)


# # recur : can be defined as the process 
# # of defininfg something in terms of itself

# # # # ie a fun calls itself directly or indirectly
# # 
# def fact(n):
#     if n==1:      
#         return 1
#     else:
#         print(n)
#         return n*fact(n-1)    
    
# f=fact(5)
# print(f)   



# # higher order  : it contains other fun as
# # a parameter or return a function
# # as a output, ie fun work with another fun
# # can store the func in a variable


# def first(a,b):
#     print('=============')
#     def second(c):
#         print('......')
#         print(a,b,c)
#         s=a+b+c
#         print(s)
#     return second

# val=first(2, 5)
# print(val)
# val(4)


# def add():
#     print (3+7)

# add()    
# print(add)

# ---------------------------

# def list_sum(num_List):
#     if len(num_List) == 1:
#         return num_List[0]
#     else:
#         return num_List[0] + list_sum(num_List[1:])
        
# print(list_sum([2, 4, 5, 6, 7]))  # 24


# --------------------------------------------------------


# def reverse(n, r):
#     if n==0:
#         return r
#     else:
#         return reverse(n//10, r*10 + n%10)

# # Read number
# number = int(input("Enter number: "))  #234  432

# # Function call
# reversed_number = reverse(number,0)

# # Display output
# print("Reverse of %d is %d" %(number, reversed_number))

# -------------------------------------------------------


# Write a Python program to sum recursion lists.
# Test Data: [1, 2, [3,4], [5,6]]
# # Expected Result: 21

# def recursive_list_sum(data_list):
# 	total = 0
# 	for element in data_list:
# 		if type(element) == type([]):
# 			total = total + recursive_list_sum(element)
# 		else:
# 			total = total + element

# 	return total
# print( recursive_list_sum([1, 2, [3,4],[5,6]]))

# ------------------------------------------------------------------

# Write a Python program to get the sum of a non-negative integer.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9

# def sumDigits(n):
#   if n == 0:
#     return 0
#   else:
#     return n % 10 + sumDigits(int(n / 10))

# print(sumDigits(345))

# print(sumDigits(45))


def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

print(fibonacci(3))

# 0,1,1, 2,3,5,8,13,

6+ 4+2

10+8+6+4+2
