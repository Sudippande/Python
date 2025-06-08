# def prime(n):

#         if(n<=1):

#          return False
#         for i in range(2,int(0.5**n)+1):

#                 if(n%i==0):

#                     return False
#                 return True
# n=77
# if prime(n):
#     print("It is a prime")
# else:
#     print("It is not a prime")
        


# def greet(n):
#     print(f"Hello world {n}")
# if __name__=="__main__":
#     greet()

# try:
#     assert 2 + 2 == 5, "Math is broken!"
# except AssertionError as e:
#     print("Assertion failed:", e)

for i in range(5):
    print(" "*(4-i)+'*'*(i+1))
