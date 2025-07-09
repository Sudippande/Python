# fibo=fib(n-1)+fib(n-2)

# def fibo(n):
#     if n<=0:
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# print(fibo(10))
    
# n=int(input("Enter Fibonacci term: ",))
# n1,n2=0,1
# fibo=0
# if n<=0:
#     print("Positive number enter")
# elif n==1:
#     print('fibo is 1')

# else:
#     print("fibonacci")
#     while fibo<n:
#         print(n1)
#         nth=n1+n2
#         n1=n2
#         n2=nth
#         fibo +=1


#this is a recursive approach but slow

# class Solution:
#     def fib(self,n:int)->int:
#         if n==1:
#             return 1
#         elif n==0:
#             return 0
#         return self.fib(n-1) + self.fib(n-2)
# so=Solution()
# print(so.fib(10))

#this is a more updated version

class Solution:
    def fib(self,n:int)->int:
        ans=[0,1]
        for i in range(2,n+1):
            ans.append(ans[i-1] + ans[i-2])
        return ans

sol=Solution()
print(sol.fib(10))

