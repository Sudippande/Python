# 5
# 45
# 345
# 2345
# 12345

for i in range(5, 0, -1):         # i from 5 down to 1
    for j in range(i, 6):         # j from i up to 5
        print(j, end="")          # print numbers on the same line
    print()                       # move to next line after inner loop

    

#1
# x=int(input("1st:"))
# y=int(input("2nd:"))
# z=int(input("3rd:"))
# n=3
# rest=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n]
# print(rest)
    
