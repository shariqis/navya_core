# l1=['zero','one','two','three','four']
# l2=['ten','eleven','twelve','thirteen','fourteen']
# l3=['','','twenty','thirty','forty','fifty']

# num=int(input('enter number : '))
# if num<10 and num>=0:
#     print(l1[num])
# elif num>=10 and num<20:
#     n=num%10
#     print(l2[n])  
# elif num>=20 and num<100:
#     ten=num//10
# #     ones=num%10
# #     if ones==0:
# #         print(l3[ten])    
# #     else:
# #         n1=l3[ten]
# #         n2=l1[ones]
# #         print(n1,n2)
# # else:
# #     print('invalid')          
    
    
# phonebook={}
# name=input('enter ur name :')
# email=input('enter ur email : ')
# no_p=int(input('enter number of phn numbers: '))
# p=[]
# for i in range(no_p):
#     phone=int(input('enter ur phone : '))
#     p.append(phone)
# sub={}
# sub['name']=name
# sub['email']=email
# sub['phone']=p
# print(sub)
# phonebook[name]=sub
# print(phonebook)
# # print('...................................')
# name=input('enter ur name :')
# email=input('enter ur email : ')
# phone=int(input('enter ur phone : '))
# sub={}
# sub['name']=name
# sub['email']=email
# sub['phone']=phone
# phonebook[name]=sub
# print(phonebook)

# pb={'A':{'name':'A','p':'333','email':'A@gmail.com'},
#     'B':{'name':'B','p':777,'email':'B@gmail.com'}}
# print(pb['B'])
# print(pb['B']['name'])
# pb['B']['name']="BINU"
# c=pb.pop('B')
# print(pb)
# pb['BINU']=c
# print(pb)

phonebook={}
while True:
    
    choice=int(input("""enter ur choice 
  1. add
  2. View
  3. Update
  4. Delete
  5. Exit
  ::::::   """))
    if choice==1:
        sub={}
        p=[]
        name=input('enter ur name :')
        email=input('enter ur email : ')                
        sub['name']=name
        sub['email']=email
        no_p=int(input('enter number of phn numbers: '))       
        for i in range(no_p):
            phone=int(input('enter ur phone : '))
            p.append(phone)
        sub['phone']=p
        phonebook[name]=sub
    elif choice==2:
        print(phonebook)
        # name=input('enter  name to view :')
        # if name in phonebook:
        #     print(phonebook[name]["name"])
        # else:
        #     print('not exist')  
    elif choice ==3:
        name=input('enter  name to update :')
        ch=int(input('enter choice to update 1-> name 2-> email 3-> phone '))
        if ch==1:
            newename=input('enter ur new name : ')
            phonebook[name]['name']=newename
            details=phonebook.pop(name)
            phonebook[newename]=details
        elif ch==2:
            newemail=input('enter ur new email : ')  
            phonebook[name]['email']=newemail
        elif ch==3:
            c =int(input('enter choice 1-> add 2-> delete'))
            if c==1:                 
                new=int(input('enter ur new num  : '))
                l=phonebook[name]["phone"] 
                l.append(new)
            else:
                new=int(input('enter  num to delete : '))
                if new in phonebook[name]["phone"]:
                    l=phonebook[name]["phone"]
                    l.remove(new)
                    print(l)
                else:
                    print('invalid')    
                
    elif choice==4:
        name=input('enter  name to delete :')
        if name in phonebook:
            del phonebook[name]
        else:
            print('not exist')   
                         
    elif choice==5:
        break    
    else:
        print('invalid')        
    