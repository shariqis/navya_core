##file open

# file = open('anu.txt','r') 
# # file = open(r"C:\Users\quest\Desktop\Shari\MyWorks\fileOpp.txt.txt",'r')  # specifying full path
# # file = open(r'D:\new.txt.txt','r') 
# # This will print every line one by one in the file 
# print(file)
# for n in file: 
#     print(n) 
# Python code to illustrate read() mode  
# print(file.read(89)) 
# c=file.read()
# print(c)
# print(len(c))
# # Python code to illustrate read() mode character wise  
# #way to read a file is to call a certain number 
# of characters


# print (file.read(4))



# # # # # Python code to create a file 
# # f=open('bb.txt','w')
# f=open(r'C:\Users\sumesh\Desktop\notes\navya.txt','w')
# # # f = open(r'D:\newbatch\file1.txt','w') 
# f.write("This is the write command 2nd") 
# f.write('\n')
# f.write("This is the write command 3rd") 
# f.write('welcome')
# f.write('\n')
# f.write('good luck')
# f.close() 

# # # # # Python code to illustrate append() mode 
# file = open('anu1.txt','a') 
# file.write("This will add this line to end") 
# file.close()


# # # # # Python code to illustrate with() alongwith write() 
# with open("bb.txt", "r") as f:  # f= open("v.txt", "w")
#     # f.write("Hello World!!!")  

# # # # Python code to illustrate split() function 
# # +++------------')
#     c=f.read()
#     print(c)
#     print(c[1:4])
#     print('----------------------')
# #     for line in data: 
# #         word = line.split('\n') 
# #         print (word) 


f= open("bb.txt", "r")
c=f.readlines()
# print(c)

for i in c:
    print(i)
    v= i.split(' ')
    # for j in i:
    print(v)
    # for j in v:
    #     if len(j)>=4:
    #         print(j)