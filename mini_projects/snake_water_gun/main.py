import random

def game():
    print("You are playing game !")
    score=random.randint(1,100)
    with open("sudip.txt",'a+') as f:
        highscore=f.read()
        if(highscore !=""):
            highscore=int(highscore)
        else:
            highscore=0

    print(f"Your score:{score}")
    if(score>highscore):
          with open("sudip.txt",'w') as f:
            f.write(str(score))
    
    return score
game()