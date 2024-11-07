import random 

number = random.randint(1,500)

##prompt the user to pick a number
guessNum = 0

while (guessNum < 10):
    print("Pick a number between 1-500")
    curr_guess = int(input())

    if curr_guess > number:
        print ("Guess lower")
    
    elif curr_guess < number: 
        print ("Guess higher")

    else:
        print("You guessed correct!")
        break

    guessNum += 1

if (guessNum == 10 and curr_guess != number):
    print("haha you lost better luck next time")
    print("The correct number was", number)
