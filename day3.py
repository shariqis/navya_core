# mark=int( input('enter ur mark : '))
# cutoff=int(input('enter ur cutoff'))

# if mark>cutoff:
#     print('pass')
# else:
#     print('fail')    


day=int(input('enter day num : '))
if day==0:
    print('sunday')
elif day==1:
    print('mon')
elif day==2:
    print('tue')
elif day==3:
    print('wed')
elif day==4:
    print('thu')
elif day==5:
    print('fri')
elif day==6: 
    print('sat')
else:
    print('invalid')    
    
    # elif day==6:

num1= int(input('enter num 1: '))                  
num2= int(input('enter num 2: '))                  
num3= int(input('enter num 3: '))

if num1>num2 and num1> num3:
    print('num1 is large')
elif num2>num3:
    print('num2 is large')  
else:
    print('num 3 is large')      
                      