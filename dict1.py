# a={'name':'anu','place':'eklm','age':23}
# print(a)
# print(type(a))
# print(len(a))
# print(a['age'])
# for i in a:
#     print(i,a[i])
# a['name']="anu thomas"
# a['phone']=67576576
# print(a)
# derails={}
# addrss=input('enter ur address : ')
# derails={'address':addrss}
# derails['address']=addrss
# c='hiii'
# print(c)


##dictionary

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964 
# }
# print(thisdict)

# print(thisdict['year1'])

#Accessing Items

# # x = thisdict["model1"]
# # print(x)
# x = thisdict.get("model1",'error')
# print(x)

### change values

# # thisdict["year"] = 2018
# thisdict["color"] = 'red'
# print(thisdict)

## to get keys
# for x in thisdict:
#   print(x)

## to get values
# for x in thisdict:
#   print(x, thisdict[x])

## to get values
# for x in thisdict.values():
#   print(x)

## dictionary keyvalue pair
# for x, y in thisdict.items():
#   print(x, y)
# --------------------------------------------------

## checking if key is present in dictionary

# if "Ford" in thisdict:
#     print('Present')
# else:
#     print('Not present')


# print(len(thisdict))

# thisdict["color"]="red"
# print(thisdict)


## pop with key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# c=thisdict.pop("model")
# print(thisdict)
# print(c)
# ## popitem() - last inserted item
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# v=thisdict.popitem()
# print(thisdict)
# print(v)
##delete
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
thisdict.clear()
print(thisdict)



# fruit = {'Apple': 1.99, 'banana': 0.99,
#           'Orange': 1.49, 'pineapple': 3.99,
#           'Grapes': 0.39}
# print(fruit)
# # print(sorted(fruit))
# # print(sorted(fruit.keys()))
# # print(sorted(fruit.values()))
# # print(sorted(fruit.items()))
# print(sorted(fruit.values(), reverse=True))

