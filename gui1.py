from tkinter import *
from tkinter.ttk import * 

window=Tk()
window.title('welcome ')
window.geometry('400x400')
window.maxsize(500,500)
window.minsize(100,100)

# lbl1=Label(window,text="hai welcome")  #, bg="green", fg="red"
# lbl1.grid(row=1,column=3)
# lbl2=Label(window,text="hello")
# lbl2.grid(row=1,column=6)
# lbl3=Label(window,text="welcome")
# lbl3.grid(row=2,column=4)
# lbl4=Label(window,text="hw r u ")
# lbl4.grid(row=3,column=2)
# lbl5=Label(window,text="hw")
# lbl5.grid(row=13,column=3)

# e1= Entry(window)
# e1.grid(column=3, row=6)

# def hi():
#     # print('hiiiiiiiiiiiiiii')
#     # e1.focus()
    
#     # print(c)
#     # name=input('enter ur name : ')   
#     # c=e1.get()
#     # l=len(c)
    
#     # e1.insert(l,' '+name)
#     # e1.insert(END,name)
    
    
#     # lbl1.configure(text="Button was clicked !!")
#     e1.delete(0,3)
    
    

# btn= Button(window,text="submit", command=hi)
# btn.grid(column=7,row=8)

# ----------------combobox-------------------------------------------------------
# from tkinter.ttk import * 
# combo = Combobox(window)
# combo['values']= ('Select' ,1, 2, 3, 4, 5, "Text",'anu',234)

# combo.current(0) #set the selected item by setting index position

# combo.grid(column=0, row=3)

# def checkCombo():    
#     a=combo.get()
#     print(a)
    
# btncombo = Button(window, text="Click Me get combo",command=checkCombo)
# btncombo.grid(column=2, row=4)

# ------------------messagebox-----------------------------------------------------------


# from tkinter import messagebox

# def msgclicked():
#     # messagebox.showinfo('Message title', 'Message content')
#     # messagebox.showwarning('Message title', 'Message content')  #shows warning message
#     messagebox.showerror('Message title', 'Message content')    #shows error message

# btn = Button(window,text='Click here for msg', command=msgclicked)
# btn.grid(column=0,row=12)

# ---------------------check box--------------------------------




# # # # # # Add a Checkbutton widget (Tkinter checkbox)

# # chk_stateN = BooleanVar()

# # chk_stateN.set(True) #set check state
# # chkN = Checkbutton(window, text='Choose checkbox', var = chk_stateN)
# # # chkN = Checkbutton(window, text='Choose checkbox')
# # chkN.grid(column=0, row=8)

# # # # chkN.instate(['selected'])  # returns True if the box is checked


# # # # # # # # next method
# chk_state1 = IntVar()
# chk_state1.set(0) #uncheck
# # # # chk_state1.set(1) #check
# chk = Checkbutton(window, text='hai', var=chk_state1)
# chk.grid(column=0, row=9)
# # chk1 = Checkbutton(window, text='Choose notesssss', var=chk_state1)
# # chk1.grid(column=0, row=6)

# def check_chkbtn():    
#     # a=chk.state()
#     # print(a)
#     print(chk.instate(['selected']))
# btnchk = Button(window, text="Click ",  command=check_chkbtn)
# btnchk.grid(column=0, row=7)



# ------------Radiobutton-----------------------------------------------

# selected = IntVar()
# # selected1 = IntVar()   
# selected1 = StringVar()   
# rad1 = Radiobutton(window,text='First', value=1,variable=selected ) #  
# rad2 = Radiobutton(window,text='Second', value=2 ,variable=selected  )  #  

# rad3 = Radiobutton(window,text='eng', value=11, variable=selected1 ) #  
# rad4 = Radiobutton(window,text='mal', value=22, variable=selected1 )  #  

# def clicked():
#    print(selected.get())
#    print(selected1.get())

# btn = Button(window, text="Click Me radio", command=clicked)
# rad1.grid(column=0, row=9)
# rad2.grid(column=1, row=9)
# rad3.grid(column=2, row=10)
# rad4.grid(column=3, row=10)
# btn.grid(column=4, row=11)



# -------------------------------------------------------------------


# # # # # ## Add a ScrolledText widget (Tkinter textarea)
# # # # # To set scrolledtext content, you can use the insert method like this:
# # # # txt1.insert(INSERT,'You text goes here')
# # # # # # Delete/Clear scrolledtext content
# # # # # # To clear the contents of a scrolledtext widget, you can use delete method like this:

# from tkinter import scrolledtext
# txt1 = scrolledtext.ScrolledText(window,width=15,height=10)
# # # # # # # Set scrolledtext content
# txt1.grid(column=0,row=10)
# def dele():
#     txt1.insert(1.2,'You text goes here')
#     # txt1.delete(1.3)
#     # txt1.delete(2.2,END)
#     # print(txt1.get(1.0,2.3))
# btn1 = Button(window, text="Click Me to del", command=dele,width=50)
# btn1.grid(column=0, row=11)


# ----------------------------------------------------------------------


# from tkinter.ttk import Progressbar

# bar = Progressbar(window, length=450)
# bar['value'] = 80
# bar.grid(column=0, row=13)


# --------------------------------------------------

 # menu

# from tkinter import Menu # menu bar


# menu = Menu(window)
# new_item = Menu(menu)
# new_item.add_command(label='New')

# # # menu.add_cascade(label='File', menu=new_item)
# # # window.config(menu=menu)
# def n():
#    print('haiii')   
# def ss():
#     print('hello..............')   



# -------------------------------------

# from tkinter import Menu # menu bar
# menubar= Menu(window)
# filemenu= Menu(menubar)
# filemenu.add_command(label='New', command=n)
# filemenu.add_command(label='open')
# filemenu.add_command(label='save')
# filemenu.add_separator()
# filemenu.add_command(label='close')
# menubar.add_cascade(label='File', menu=filemenu)
# # # window.config(menu=menubar)
# editmenu= Menu(menubar)
# editmenu.add_command(label='aa', command=ss)
# editmenu.add_command(label='bb')
# menubar.add_cascade(label='edit', menu=editmenu)


# window.config(menu=menubar)

txt1=Entry(window,width=40)
txt1.grid(row=0,column=1,columnspan=3)

def one():
    check()
    txt1.insert(END,"1")
def two():
    txt1.insert(END,"2")
def three():
    txt1.insert(END,"3")
def plus():
    check_op()
    txt1.insert(END,"+")
def minus():
    check_op()
    txt1.insert(END,"-")
def zero():  
    check()    
    txt1.insert(END,"0")
        
def check():
    a=txt1.get()
    if len(a)==1 and a[0]=="0":
        txt1.delete(0,END)                
    
def eql(): 
    
    
   
    a=txt1.get()
    o=eval(a)
    txt1.delete(0,END)
    txt1.insert(0,o)
    
    
def check_op():
    a=txt1.get() 
    if a[-1] in '+-*/':
        txt1.delete(len(a)-1) 

btn1=Button(window,text="1",command=one)
btn1.grid(row=1,column=1)
btn2=Button(window,text="2",command=two)
btn2.grid(row=1,column=2)
btn3=Button(window,text="3",command=three)
btn3.grid(row=1,column=3)
btn0=Button(window,text="0",command=zero)
btn0.grid(row=1,column=4)

btnp=Button(window,text="+",command=plus)
btnp.grid(row=2,column=1)
btnm=Button(window,text="-",command=minus)
btnm.grid(row=2,column=2)
btne=Button(window,text="=",command=eql)
btne.grid(row=2,column=3)







window.mainloop()


