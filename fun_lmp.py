#  lambda arguments: expression



# x=lambda a,b,c:return b
# print(x(2,1,4))


# x1=lambda a:10+a
# print(x1(9))


# x2=lambda a,b,c: print(a)

# print(x2(3,2,1))
# # print(a)


# def squr(a):
#     c=a**2
#     return c
# v=add(5)
# print(v)


# def myfun(n):
#     return lambda a:a*n  # lambda a:a*2



# d=myfun(2)
# print(d(5))

# t=myfun(3)
# print(t(5))



# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
# final_list = list(filter(lambda x: (x%2 == 0) , li)) 
# print(final_list) 


# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
# final_list = list(map(lambda x: x*2 , li)) 
# print(final_list) 



# from functools import reduce
# li = [5, 8, 10, 20, 50, 100] 
# sum = reduce((lambda x, y: x -y), li) 
# print (sum)

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print(subject_marks)
