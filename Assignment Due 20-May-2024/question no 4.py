# Number Guessing Game: Create a number guessing game where the computer
#  generates a random number between 1 and 100, and the user tries to
# guess it. Use a while loop to repeatedly prompt the user for guesses
#  until they correctly guess the number.


# import= random{1,100}


# random_num= (1,100)
# guess=None
# guess=int(input("enter a guess="))
# while(guess!=random_num):
#     guess=int(input("enter a guess="))
#     if(guess==random_num):
#         print("you guess the number",random_num)
#     else:
#         print("enter a vaild number bewteen 1 and 100")
        


import random
target_number = random.randint(1,100)
guess = None

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess what it is?")

    # Use a while loop to prompt the user for guesses until they guess correctly
while guess != target_number:
        # Take input from the user
    guess = input("Enter your guess: ")

        # Check if the input is a valid number
    if guess.isdigit():
        guess = int(guess)

            # Provide feedback to the user
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(" You guessed the number" ,target_number)
    else:
        print("Please enter a valid number between 1 and 100.")

    
return