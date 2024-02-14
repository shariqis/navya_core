a=[1,3,2,1,3,5,6,3]
d={}
for i in a:
    if i in d:
        # d[i]=d[i]+1
        d[i]+=1
    else:
        d[i]=1    
        
print(d)
for a in d:
    print(a ,'occurence = ', d[a])      