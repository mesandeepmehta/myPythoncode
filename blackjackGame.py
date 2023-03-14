import random
a = random.randint(2,12)
b = random.randint(2,12)
c = a + b
endGame = False
while endGame==False:
    if c==21:
        try:
            print("Your cards are ", a, " , ", b ," and ", d)
        except NameError:
            print("Your cards are ", a ," and ", b )
        print("you Got blackjack")
        endGame=True
    elif c>21:
        print("Your cards are ", a ," and ", b, " and sum is ", c)
        print("You lose")
        endGame=True
    else:
        try:
            print("Your cards are ", a, " , ", b ," and ", d)
        except NameError:
            print("Your cards are ", a ," and ", b )
        print("Do you want to draw another card\n" "1.yes  2.no")
        option =  int(input("Enter choice 1 or 2: "))
        if option == 1:
            d= random.randint(2,12)
            print("your card now is ", d)
            c=c+d
            continue
        elif option == 2:
            print ("Your sum is" , c)
        else: 
            print("Enter valid choice")

  
