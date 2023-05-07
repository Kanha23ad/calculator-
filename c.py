from tkinter import*
def btnClicked(number):
    global val
    val = val +str(number)
    entry_value.set(val)

def dtnClear():
    global val
    val =''
    entry_value.set('')

def btn_Equals():

    try:

        global val
    
        result = str(eval(val))
        entry_value.set(val + "=" + result)
        val=''
    except:
        entry_value.set('Error')
        val=''

    print(f' History : \n {entry_value.get()}')
    
        
    with open("history.txt","r+") as f:
        f.write("\n")
        f.write(f' History : \n {entry_value.get()}')
        f.write("\n")
        f.close()
root = Tk()



        
        
root.title("Calculator")
root.iconbitmap(r'D:\Tkinter login\.vscode\c.ico')
root.geometry("387x658")
root.resizable(0,0)



 

frame = Frame(root,bg = "#212121",width=500,height=900).place(x=0,y=0)
val = ""
entry_value = StringVar()
entry = Entry(frame,width=15,font=("Arial Bold ",30),textvariable=entry_value,borderwidth=9,border=9,relief=SUNKEN,bd=25).place(x=0,y=0)




b =Button(frame,text="1",font=("Arial Bold",23,"bold"),width=4,height=2,bg='#57a1f8',fg="#fff",command=lambda:btnClicked (1)).place(x=10,y=110)

b =Button(frame,text="2",font=("Arial Bold",23,"bold"),width=4,height=2,bg="#57a1f8",fg="#fff",command=lambda:btnClicked (2)).place(x=105,y=110)
b =Button(frame,text="3",font=("Arial Bold",23,"bold"),width=4,height=2,bg='#3697f5',fg="#fff",command=lambda:btnClicked (3)).place(x=200,y=110)
b=Button(frame,text="4",font=("Arial Bold",23,"bold"),width=4,height=2,bg='#3697f5',fg="#fff",command=lambda:btnClicked (4)).place(x=10,y=217)
b =Button(frame,text="5",font=("Arial Bold",23,"bold"),width=4,height=2,bg='#3697f5',fg="#fff",command=lambda:btnClicked (5)).place(x= 105,y=217)
b =Button(frame,text="6",font=("Arial Bold",23,"bold"),width=4,height=2,bg='#3697f5',fg="#fff",command=lambda:btnClicked (6)).place(x=201,y=217)
b =Button(frame,text="7",font=("Arial Bold",23,"bold"),width=4,height=2,bg='#3697f5',fg="#fff",command=lambda:btnClicked (7)).place(x=10,y=324)
b =Button(frame,text="8",font=("Arial Bold",23,"bold"),width=4,height=2,bg ='#3697f5',fg="#fff",command=lambda:btnClicked (8)).place(x=105,y=324)
b =Button(frame,text="9",font=("Arial Bold",23,"bold"),width=4,height=2,bg = '#3697f5',fg="#fff",command=lambda:btnClicked (9)).place(x=201,y=324)
b =Button(frame,text="0",font=("Arial Bold",23,"bold"),width=4,height=2,bg='#3697f5',fg="#fff",command=lambda:btnClicked (0)).place(x=105,y=430)
b =Button(frame,text="C",font=("Arial Bold",23,"bold"),width=4,height=2,bg="orange",fg="#fff",command=lambda:dtnClear()).place(x=10,y=536)



b =Button(frame,text="+",font=("Arial Bold",23,"bold"),width=4,height=2,bg='orange',fg="#fff",command=lambda:btnClicked ("+")).place(x=295,y=110)
b =Button(frame,text="-",font=("Arial Bold",23,"bold"),width=4,height=2,bg='orange',fg="#fff",command=lambda:btnClicked ('-')).place(x=295,y=217)
b =Button(frame,text="*",font=("Arial Bold",23,"bold"),width=4,height=2,bg='orange',fg="#fff",command=lambda:btnClicked ('*')).place(x=295,y=324)
b=Button(frame,text="/",font=("Arial Bold",23,"bold"),width=4,height=2,bg='orange',fg="#fff",command=lambda:btnClicked ('/')).place(x=295,y=430)
b =Button(frame,text="=",font=("Arial Bold",23,"bold"),width=4,height=2,bg="orange",fg="#fff",command=btn_Equals).place(x=201,y=430)
b =Button(frame,text=".",font=("Arial Bold",23,"bold"),width=4,height=2,bg="#3697f5",fg="#fff",command=lambda:btnClicked ('.')).place(x=10,y=430)
b =Button(frame,text="**",font=("Arial Bold",23,"bold"),width=4,height=2,bg='orange',fg="#fff",command=lambda:btnClicked ('**')).place(x= 105,y=536)
b =Button(frame,text="(",font=("Arial Bold",23,"bold"),width=4,height=2,bg='orange',fg="#fff",command=lambda:btnClicked ('(')).place(x= 201,y=536)
b =Button(frame,text=")",font=("Arial Bold",23,"bold"),width=4,height=2,bg='orange',fg="#fff",command=lambda:btnClicked (')')).place(x= 295,y=536)






root.mainloop()
