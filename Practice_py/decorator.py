# def hello(func):                                                                                            
#     def inner():                                                                                            
#         print("Hello ")                                                                                     
#         func()                                                                                              
#     return inner                                                                                            
                                                                                                            
# def name():                                                                                                 
#     print("Alice")                                                                                          
                                                                                                            
                                                                                                            
# obj = hello(name)                                                                                           
# obj()

# def who():                                                                                                  
#     print("Alice")                                                                                          
                                                                                                            
# def display(func):                                                                                          
#     def inner():                                                                                            
#         print("The current user is : ", end="")                                                             
#         func()                                                                                              
#     return inner                                                                                            
                                                                                                            
# if __name__ == "__main__":                                                                                  
#     myobj = display(who)                                                                                    
#     myobj()


#     #decorators 
# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("First line Good morning ")
#         fx(*args, **kwargs)
#         print("last line Thank you for using this function")
#     return mfx
    
# @greet
# def hello():
#     print("Hello Wolrd !")

# @greet
# def add(a,b):
#     print(a+b)

# hello()
# add(3,3)


#getter and setter 

# class myclass:
#     def __init__(self,value):
#         self._value=value
    
#     def show(self):
#         print(f"Values is : {self._value}")

#     @property#getter
#     def ten_value(self):
#         return 10*self._value
    
#     @ten_value.setter
#     def ten_value(self,new_val):
#         self._value=new_val/10
    
# obj=myclass(10)
# obj.ten_value=67
# print(obj.ten_value)
# obj.show()

#iterator
a=[1,2,4,5]
iterator=a.__iter__()
print(iterator.__next__())

#Geneerator uses yield keywards
def my_gen():
    yield 1
    yield 2
    yield 3
gen=my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))