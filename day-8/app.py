
import random

secret_number = random.randint(1, 100)

print("------Welcome to the Number Guessing Game------")
print("Guess a number between 1 and 100")

while True:
    try:
        guess = int(input("\nEnter your guess:"))

        if guess < 1 or guess >100 :
            print("Please enter a between 1 and 100!")
        elif guess < secret_number:
            print("Too low! try again") 
        elif guess > secret_number:
            print("Too high! Try again")
        else:
            print("Congratulation1 You guessed it right!")   
            break        
    except ValueError:
        print("Please enter a valid number!")    
    
