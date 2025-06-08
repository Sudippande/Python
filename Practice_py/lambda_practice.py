# def fun(*args):
#     print(args[0:3])
# fun(1,2,3,"ram")

#**kwrgs

# def fun(**kwargs):
#     for key in kwargs.values():
#         print(key)
# fun(name="syasdbf",age=34,address="Dhansha")

#complex
#Write a function that takes a string and prints it in reverse.
# def fun(x):
#     print(x[::-1])
# fun("rammandir")

#factorial
# def fact(n):
#     pro=1
#     for i in range(1,n+1):
#         # !5= 5 * 4 * 3 *2 *1
#         pro=i*pro
#     print(pro)
# fact(5)


# if you want to return the largest string based on length, you can do:
# def find_largest_string(*args):
#     largest = ''
#     for word in args:
#         if len(word) > len(largest):
#             largest = word
#     return largest

# print(find_largest_string("ram", "hi", "haribahadur", "hello"))

#Write a fun that accept std info using **kwargs and prints it
# def fun(**kwargs):
#     for key,value in kwargs.items():
#         print(F"{key}:{value}")
# fun(name='sudip',clas=3,roll=1,address="Dhanusha")

#write a recursive function to caluculate a fibonacci series 
# def fibo(n):
#     if(n<=1):
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
# for i in range(10):
#     print(fibo(i),end=" ")



# def name():
#     a=['apple','ball','cat']
#     for i in enumerate(a):
#         print(i)
# name()
# x=lambda a:a**2
# print(x(5))

# e=lambda x: print("Even") if x%2==0 else print("odd")
# print(e(7))

#cube
# nbr=[1,2,3,4]
# cub=list(map(lambda x:x**3,nbr))
# print(cub)
 
# nbr=[1,2,3,4,5,6,7,8]
# evn=filter(lambda x: x%2==0,nbr)
# print(list(evn))

# name=['ramesh','ram','sudip','roamnnia']
# res=list(filter(lambda x:len(x)>=5,name))
# print(res)

# data=[(1,3),(3,2),(5,1)]
# re=sorted(data,key=lambda x:x[1])
# print(re)

# d=121
# b=str(d)
# re=lambda x:"Palindrome" if x[::-1]==b else "Not"
# print(re(b))

# a=[1,2,3,4,5,6,7,8]
# evn=list(filter(lambda x:x%2==0,a))
# sqr=list(map(lambda x:x**2,evn))
# sumO=sum(sqr)
# print(sumO)


# sort by  score
# students = [{'name': 'Ram', 'score': 80}, {'name': 'Sita', 'score': 95}]
# re=sorted(students,key=lambda x:x['score'])
# print(re)

#shorting of string based on last Character
# names = ['apple', 'banana', 'cherry']
#Expected sort: ['banana', 'apple', 'cherry'] → because of 'a', 'e', 'y'
# re=sorted(names,key=lambda x:x[::-1])
# print(re)

class Example:
    def __init__(self):
        self.__pr = "I am private"


    def ac(self):
        return self.__pr  # Can be accessed inside the class

obj = Example()
print(obj.ac())
# print(obj.__private_variable)  # Error: AttributeError: 'Example' object has no attribute '__private_variable'
# print(obj.access_private())  # Accessed through a public method
