secretFruit = "Mango"
userinput = ""
guessCount = 0
maxGuess = 3
outOfGuesses = False
while secretFruit!=userinput and not outOfGuesses:
    userinput=input("Enter a name of fruit: ")
    guessCount=guessCount+1
    if guessCount==3:
        outOfGuesses=True
if outOfGuesses:
    print ("You Lose")
else:
    print("You Win")
