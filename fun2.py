# def add(*a):
#     # print(a)
#     s=0
#     for i in a:
#         s+=i
#         # print(i)
#     return s
# a=add(3,2,3,5,2,0,12)    
# print(a)


# # def details(name,place):
# #     print('name -> ',name)
# #     print('place -> ',place)
# def details(**data):
#     print('data -> ',data)
    
    
# details(place='eklm',name='anu',phn=65767)    



# def add(*a):  
#     print(a)  
#     s=0
#     for i in a:
#         for j in i:
#             s+=j
#     return s

# limit=int(input('enter items number  : '))
# prices=[]
# for i in range(limit):
#     p=int(input('enter price : '))
#     prices.append(p)

# print(prices)
# total=add(prices)
# print(total)



# def add(n1,n2):
#     print(n1+n2)

# def calcul():
#     num1=int(input('enter num1 : '))
#     num2=int(input('enter num2 : '))
#     add(num1,num2)

# calcul()    

# def hai():
#     # return 'hello'

#     return 'haiii'
    
# c=hai()
# print(c)

def total_sum(**itm):
    print(itm)
    print(type(itm))
    total=0
    for i in itm.values():
        total+=i
    return total           

a={"apple":40,"banan":30}
    
amount=total_sum(**a)    
print('toat l amout : ',amount)