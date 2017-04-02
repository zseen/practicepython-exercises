
x = input("player A: ")
y = input("player B: ")

def game(x,y):
    if x==y:
        print ("It is a tie")
    elif x=="paper" and y=="rock":
        print ("A won")
    elif x=="paper" and y=="scissors":
        print("B won")
    elif x=="rock" and y=="paper":
        print ("B won")
    elif x=="rock" and y=="scissors":
        print ("A won")
    elif x=="scissors" and y=="rock":
        print ("B won")
    elif x=="scissors" and y=="paper":
        print ("A won")
    else:
        print ("Please type rock, paper or scissors")

game(x,y)
