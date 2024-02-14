# a="welcome"
# print(a[0:])
# print(a[:3])
# print(a[:5])
# print(a[0:2])
# print(a[1:5:3]) #elco eo
# print(a[:-3])
# print(a[:-5])
# print(a[-1:-5:-1])
# print(a[1:5:-1])
# print(a[::-1])



# var = 'mY Name iS sredhA'
# print(var)
# # print(var.capitalize())
# # print(var.lower())
# # print(var.upper())
# # print(var.title())
# print(var.swapcase())


# #String Comparison functions
#
# var = '76876'
# print(var)
# print(var.islower())
# print(var.isupper())
# print(var.isalpha())
# print(var.isnumeric())
# var='3435dsfsdf#'
# print(var)
# print(var.isalnum())

# a="abc"
# b="mnop"
# print(a)
# print(b)
# s=a[0]+b[0]
# m=a[len(a)//2]+b[len(b)//2]
# l=a[-1]+b[-1]
# print(s+m+l)

# a="Pfda4g243#$%DF"
# #s->3 c->7 u->3 l->4 d->4
# s=0
# c=0
# l=0
# u=0
# d=0
# for i in a:
#     if i.isalpha():
#         c+=1
#         if i.isupper():
#             u+=1
#         else:
#             l+=1   
#     elif i.isnumeric():
#         d+=1
#     else:
#         s+=1
        
# print("spcl -> ", s)        
# print("char -> ", c)        
# print("upper -> ", u)        
# print("lower -> ", l)        
# print("digit -> ", d)  

# a="abc" 
# b="mnopq"   #aobncmde  #aqbpcomn
# b=b[::-1] 
# la=len(a)
# lb=len(b)
# if la<lb:
#     l=lb
# else:
#     l=la    
# s=''
# for i in range(l):
#     if i<la:
#         s+=a[i] 
#     if i<lb:    
#         s+=b[i]
# print(s)
                    


# ## String Padding Functions
# #
# var='Hai'
# print(var)
# # print (var.rjust(10))
# # print (var.rjust(10,'-'))
# # print (var.ljust(10))
# # print (var.ljust(10,'-'))
# # print (var.center(7))
# # print (var.center(8,'*'))
# print (var.zfill(10))            




# # #
# var='******This is a * * good example*****'
# print(var)
# # print (var.lstrip('T'))
# # var='*****This is a good example*****'
# # print (var.rstrip('*'))
# print (var.strip('*'))


# # # Functions To Find A String In Python.
# Var = 'welceome'
# print(Var)
# print(Var.rfind('e',4,2))
# # print( Var.find('e',5,15))
# # print( Var.rfind('p'))
# print( Var.index('e'))
# # print( Var.index('hello'))


# print(r"hai \n welcome")
# print(r"D:\Batch_3_30_Jephin\th.py")
# s="string"
# print(s)
# # print(s.endswith('ing',0,3))

# print(s.startswith('s'))
# # print(s.startswith('u'))
i = 10
f = 1.9296
s = "67"
print('''Hi I am Integer ... My value is %d  
Hi I am float ...      My value is %f 
Hi I am string ...      My value is %s'''
      %(f,i,i))



# a="P@#yn26at^&i5ve" # A->8, U ->1 ,L-7,D->3 , S -> 4
# A=0
# U=0
# L=0
# D=0
# S=0

# for i in a:
#     if i.isalpha():
#         A+=1
#         if i.islower():
#             L+=1
#         else:
#             U+=1
#     elif i.isdigit():
#         D+=1
#     else:
#         S+=1                
# print('A - >',A)
# print('U - >',U)
# print('L - >',L)
# print('D - >',D)
# print('S - >',S)

# s1="abcde"
# s2="uvwxyz"  # aucxez

# f=s1[0]+s2[0]
# l=s1[-1]+s2[-1]
# m1=len(s1)//2
# m2=len(s2)//2
# m=s1[m1]+s2[m2]

# # print(f+m+l)

# s1="abc"
# s2="uvxyz"  # azbycxuv


# l1=len(s1)
# l2=len(s2)

# a=''
# if l1<l2:
#     d=l2-l1  #2
#     print('d',d)
#     v=s2[d:]  #xyz
#     print('v',v)
#     v=v[::-1] #zyx   
#     a=s2[:d]  #uv
#     print('a',a)
#     s2=v+a   #zyxuv
#     print(s2)        
#     l=l2
# else:
#     l=l1    
# s3=''
# for i in range(l):
#     if i<l1:
#         s3=s3+s1[i]
#     if i<l2:    
#         s3+=s2[i]
# print('....................',s3)



# a="xyz"
# b="abcde"

# xeydzc  ba  ab



