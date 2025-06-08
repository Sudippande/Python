#simple Number guessing game 

import random
count=0
a=random.randint(1,100)
print("Guess the number from 1 to 100")
 
while(True):

    b=int(input("Enter your number: "))
    count+=1
    if b>a:
        print(f"Lower Number than {b} please !")

    elif b<a:
        print(f"Higher number than {b} please !")

    elif b==a:
        print("Correct You guessed it write")
        break
print(f"You guessed the number in {count} counts")