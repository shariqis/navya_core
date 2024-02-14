# a=[25,33,12,19,5]
# # print(a[3])
# # a[3]=55
# print(a)
# a[5]=88


# a=[25,33,12,19,5]
# print(a)

# # a.insert(2,99)
# a.insert(8,99)
# print(a)
# print(a.index(99))
# a.append(77)
# print(a)
# a.extend('77')
# print(a)
# a=[25,33,12,19,5]
# print(a)
# b=[1,2,3]
# # a.append(b)
# a.extend(b)
# print(a)
# a=[25,33,12,19,5]
# print(a)
# a[3]=77
# b=['hai']
# # a.append(b)
# # print(a)
# a.extend(b)
# print(a)


# a=[]

# for i in range(5):
#     e=int(input('enter element : '))
#     a.append(e)
#     print(a)


# for i in range(5):
#     e=int(input('enter element : '))
#     a.insert(i,e)
#     print(a)

# a=[]
# b=[]
# c=[]

# limit=int(input('emter limit : '))
# print('.........list1----')
# for i in range(limit):
#     ele=int(input('enter element : '))
#     a.append(ele)
# print('.........list2----')
# for i in range(limit):
#     ele=int(input('enter element : '))  
#     b.insert(i,ele)  
    
    
# print('a -> ',a)
# print('b -> ',b)

# for i in range(limit):
#     s=a[i]+b[i]
#     c.append(s)

# print('sum- -> ',c)

a=[1,2,3,4,5]  #[5,4,3,2,1]

# print(a[::-1])
r=[]
l=len(a)
for i in range(l-1,-1,-1):
    r.append(a[i])
print(r)