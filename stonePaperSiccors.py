import random
import time
computerChoices=[1,2,3]
choice=["Stone","paper","Siccors"]
play=1
while play==1:
    print("Enter your choice number: \n"
          " 1. Stone\n"
          " 2. Paper\n"
          " 3. Siccors\n"
          "0. Exit")
    try:
        inp = int(input("Enter your choice: "))
    except ValueError:
        print("Enter valid integer")
        continue
    i = random.randint(0,2)
    computerGuesses = computerChoices[i]
    if computerGuesses==1 and inp==2:
        print ("you win computer has chosen Stone and you chose", choice[inp-1])
    elif computerGuesses==2 and inp==3:
        print ("you win computer has chosen Paper and you chose", choice[inp-1])
    elif computerGuesses==3 and inp==1:
        print ("you win computer has chosen Siccors and you chose", choice[inp-1] )
    elif computerGuesses==1 and inp==3:
        print("You lose as computer has chosen stone and you chose", choice[inp-1])
    elif computerGuesses==2 and inp==1:
        print("You lose as computer has chosen Paper and you chose", choice[inp-1])
    elif computerGuesses==3 and inp==2:
        print("You lose as computer has chosen Siccors and you chose", choice[inp-1])
    elif computerGuesses == 3 and inp == 3:
        print("You lose as computer has chosen Siccors and you chose", choice[inp-1])
    elif computerGuesses == inp:
        print("play again its a draw")
    elif inp==0:
        break
    else:
        print("Invalid choice!")
    time.sleep(3)

