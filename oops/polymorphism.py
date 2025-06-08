#polymorphism means many form.One interface ,multiple behaviors
# class A:
#     def speak(self):
#         print("Bark")
# class B:
#     def speak(self):
#         print("Meaw")
# c=[A(),B()]
# for d in c:
#     d.speak()

#self use na grada hamle without instance call garnu parxa like A.speak() but self halda instance create garnu parxa.

# 2 Demonstrate polymorphism using method overriding.
class Animal:
    def make_sound(self):
        print("oue !")

class Dog(Animal):
    def make_sound(self):
        print("Wolf !")

class Cat(Animal):
    def make_sound(self):
        print("Meow !")

#this is a polymorpic function
def animal_sound(c):
    c.make_sound()

c=[Dog(),Cat()]
for e in c:
    animal_sound(e)


#use of a super function is shown here.
# class a:
#     def __init__(self,b,s):
#         self._b=b
#         self._s=s
#     def info(self):
#         return self._b+self._s
    
# class c(a):
#     def add(self,f):
#         return f+super().info()
# e=c(5,5)
# f=e.add(5)
# print(f)

    

# from abc import ABC , abstractmethod
# class Animal(ABC):
#     #Abstract base class
    
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "ello"

# class Cat(Animal):
#     def make_sound(self):
#         return'Meow'
# d=Dog()
# e=Cat()
# print(d.make_sound())
# a=Animal()
# a.make_sound()



#abstrat method real life example on Payment Processing System.
# from abc import ABC, abstractmethod
 
# class paymentProcessor(ABC):

#     @abstractmethod
#     def pay(self,amount):
#         pass

# class CreditCardPayment(paymentProcessor):
#     def pay(self,amount):
#         print(f"Processing your credit card amount {amount}")

# class paypalpayment(paymentProcessor):
#     def pay(self,amount):
#         print(f"processing your paypal payment of {amount}")

# def pro_pa(self,amount):
#     self.pay(amount)

# c=CreditCardPayment()
# p=paypalpayment()


# pro_pa(c,104)
# c.pay(100)
# p.pay(300)


#operator overloading is done in 3 ways in python asma auta class ma same fun lekhda error aurxa like java js ma bako jsto hudai na asma.
#1. using Default Arguments
# class demo:
#     def show(self,a=None):
#         if a is not None:
#             print("One parameter ",a)
#         else:
#             print("No parameter")

# obj=demo()
# obj.show()
# obj.show(100)

#2. using *args for multiple argument
# class demo:
#     def show(self,*args):
#         for b in args:
#             print(b)
      

# obj=demo()
# obj.show()
# obj.show(100)
# obj.show("apple",10,"sudip")

a=[None,None,None,8]
if all(a):
    print("All items is there !")
elif any(a):
    print("Atlest one items is there !")

else:
    print("No any items is there")

n=int(input("Enter the number 1st number to begin with:"))
# nums=int(input("Enter the last number upto which you want to get prime :"))
# n=range(num,nums)
def is_prime(n):
    for x in range(2,n):
        if(n%x ==0):
            return 'It is  prime'
    return "It is not prime"
prime=is_prime(n)
print(prime)

# n=range(1,44)
# def prime(n):
#     for x in range(2,n):
#         if(n%x ==0):
#             return False
#     return True
# pr=list(filter(prime,n))
# print(pr)




    