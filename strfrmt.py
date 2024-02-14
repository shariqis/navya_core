# print("{} {}  is ".format("Greeshma","She",'kk'))

# print("{0} is {1}".format("She", "Greeshma",'kkkk'))
# print("{1} is {0}".format("She", "Greeshma"))


# print("{0} also called {1}!!".format("GeeksforGeeks", "Geeks")) 


# print("Every {} should know the use of {} {} programming and {}".format("programmer", "Open", "Source", "Operating Systems")) 

# print("Every {3} should know the use of {2} {1} programming and {0}".format("programmer", "Open", "Source", "Operating Systems")) 

# print(" is a {0} science {name} portal for {1}".format("computer","geeks", name ="arun" )) 

# print ("This site is {0:f} securely {1}!!".format(100, "encrypted")) 
  
# print ("My average of this {0} was {1:.3f}".format("semester", 78.2356876)) 
  
# print ("My average of this {0} was {1:.0f}".format("semester", 78.234876)) 
# print ("My average of this {0} was {1:.0f}".format("semester", 78.734876)) 
# print ("My average of this {0} was {1:d}".format("semester", 78.234876)) 


# print("The {0} of 3 is {1:b}".format("binary", 3)) 

# 0-0000
# 1-0001
# 2-0010
# 3-0011
# 4-0100












          
# print("The {0} of 100 is {1:o}".format("octal", 100)) 




limit=int(input('enter limit : '))
l1=[]
l2=[]
d={}
for i in range(limit):
    val=int(input('enter number : '))
    l1.append(val)
    
print(l1)    

for i in l1:
    l2.append(i**2)
    
print(l2)    

for i in range(limit):
    d[l1[i]]=l2[i]
print(d)