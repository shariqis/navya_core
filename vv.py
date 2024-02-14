

# a=[]
word = ['cat', 'car', 'fear', 'center']

# def aa(list1):
#     l=[]
#     for i in list1:
#         if i[0:2]=='ca':
#             # l.append(i)
#             l=l+[i]
#     print(l)

for i in word:
    c=i[0:2]
    if c== "ca":
        a+=[i]


# d=[i for i in a if i[0]=="c" and i[1]=='a' ]

d=[i for i in word if i[:2]=="ca" ]
print(d)

# aa(['cat', 'car', 'fear', 'center'])
