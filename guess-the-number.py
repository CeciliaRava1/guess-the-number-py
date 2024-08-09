import random
numberToGuess = random.randint(1,100)

guessedNumber = False

def guessTheNumber(guessedNumber):
    amountOfAttempts = 0
    while (not guessedNumber):
        playerIntInput = int(input('- - - Type an int between 1 and 100 - - - '))
        if playerIntInput >= 1 and playerIntInput <= 100:
            amountOfAttempts += 1
        if playerIntInput == numberToGuess:
            print(f"You guessed the game! You have used {amountOfAttempts} attempts")
            guessedNumber = True
        elif playerIntInput < numberToGuess:
            print('The number is greater than yours')
            print('')
        else:
            print('The number is less than yours')
            print('')

result = guessTheNumber(guessedNumber)   


        