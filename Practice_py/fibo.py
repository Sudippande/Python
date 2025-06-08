# def fib(n):
#     a,b=0,1
#     while(a<n):
#         print(a,end=" ")
#         a,b=b,a+b
#     print()
# fib(50)


#even fun are object
# def fun():
#     print("sudip")
# mess=fun
# mess()
# mess()


a=153
b=str(a)
su=0
for i in b:
    su+=int(i)**3
if a ==su:
     print("it is anarmstrong number ")
else:
    print("it is not ")
