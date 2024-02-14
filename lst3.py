# remove elements

# vowels = ['a','e','i','o','u']
# print(vowels)
# # vowels[1]=""
# del vowels[1]
# print(vowels)

# vowels = ['a','e','i','o','u']
# print(vowels)
# del vowels[1:3]
# print(vowels)

# vowels = ['a','e','i','o','u']
# print(vowels)
# del vowels
# print(vowels)

# xyz=['b','c','d','f','g','h','j','b']
# print(xyz)
# xyz.remove('u')
# print(xyz)


# consonants=['b','c','d','f','g','h','j']
# b=consonants.remove('b')
# print(consonants) ## raises ValueError
# print(b)
# v=consonants[2]
# print(v)
# consonants=['b','c','d','f','g','h','j']
# print(consonants)
# v=consonants.pop()## removes element at specified index
# print(consonants)
# print(v)


# con=['b','c','d','f','g','h','j']
# con.pop() #### removes element at last index
# print(con)


# s=['a','g','adf',2,3,45,67,7]
# print(s)
# s.clear()
# print(s)
# r=[2,3,4,5,65,76,7,8,'sdsaf','fdsfds','dg']
# print(r)
# r[0:2]=[]
# print(r)
# g=[2,3,1,5,6,4]
# print(sum(g))
# g=[2,3,435,5,6,4]
# g.sort()
# print(g)

# lsta=['fg',0,1,2,3,45,6]
# lsta.reverse()
# print(lsta)

# # g=['t','quest','zebra']
# g=[2,3,1,5,6,4]
# g.sort(reverse=True)
# print(g)

l1=['hello','take']
l2=['dear','sir']
l3=[]
# ['hello dear' , 'hello sir','take dear','take sir']

for i in l1:
    for j in l2:        
        v=i+' '+j
        l3.append(v)
print(l3)