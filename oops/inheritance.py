#this is a single inheritnce
# class A:
#     def parentMethod(self):
#         print("This is a parent class .")
# class B(A):
#     def childMethod(self):
#         print("This is a child Class .")
# c=B()
# c.childMethod()
# c.parentMethod()

#multiple Inhertitance
# class A:
#     def parentMethod(self):
#         print("This is a parent class .")
# class B:
#     def childMethod(self):
#         print("This is a child Class .")
# class c(A,B):
#     def multiple_inher(self):
#         print("This is a last child class from multiple parent class")
# d=c()
# d.multiple_inher()


# class division:
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def divide(self):
#       return self.n/self.d
# class modulus:
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def mod_divide(self):
#       return self.n%self.d
      
# class div_mod(division,modulus):
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def div_and_mod(self):
#       divval=division.divide(self)
#       modval=modulus.mod_divide(self)
#       return (divval, modval)
# x=div_mod(10,3)
# print(x.div_and_mod())

# multilevel inheritance
# class name:
#     def info(self):
#         print("This is a name class.")
# class nam(name):
#     def rec_get(self):
#         print("This is a nam class.")
# class na(nam):
#     def re_set(self,b):
#         print(":-",b)
# x=na()
# x.re_set("hi")
# x.rec_get()
# x.info()
 

# super () allows to access method and attribute of parent
# class ParentDemo:
#     def __init__(self,maf):
#         self.ma=maf

#     def show(self):
#         print('this is crazy dude '+self.ma)

# class child(ParentDemo):
#     def __init__(self, maf):
#         super().__init__(maf)


# obj=child("child is")
# obj.show()