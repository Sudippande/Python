from tkinter import *
root=Tk()
root.title("This is my first GUI!")
root.geometry("300x200+10+10")

#for button
def Add():
    print("Button clicked !")
B1=Button(root,text='click me',bg='red',command=Add)

#label
l1=Label(root,text="Enter name",fg='blue',font=('Helvetica',16))

e1=Entry(root,fg='black',bd=3)
e1.insert(0,"My name is sudip")


#using pack
l1.pack(fill=X,padx=10)
e1.pack(fill=X,padx=10)
B1.pack(fill=X,padx=10)


root.mainloop()