# from tkinter import *
# import random
# top=Tk()
# for r in range(2):
#     for c in range(2):
#         Label(top,text='Label'+str(r+1)).grid(row=r,column=0)
#         Entry(top,bd=3).grid(row=r,column=1)
# top.mainloop()


# def hello(event):
#     print("hello World")
# B=Button(top,text="Say hello")
# B.bind('<Button-1>',hello)
# B.pack()
# top,mainloop()

# def handler():
#     print("Radio button selected:"+str(var.get()))
# var=StringVar()
# r1=Radiobutton(top,text='male',variable=var,value='Male',command=handler)
# r2=Radiobutton(top,text='Female',variable=var,value="female",command=handler)
# r1.pack()
# r2.pack()
# top.mainloop()


# #Decorators
# # def decorator(fun):
# #     def wrapper(nam):
# #         print("hi")
# #         if nam % 2 == 0:
# #             ret = 'even'
# #         else:
# #             ret = 'odd'
# #         fun(nam)
# #         return ret
# #     print("Decorator is applied")
# #     return wrapper

# # @decorator
# # def myfun(x):
# #     print("The number is =", x)

# # # Calling the decorated function
# # no = 10
# # result = myfun(no)
# # print("It is", result)
