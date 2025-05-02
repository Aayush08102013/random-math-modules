# Guess a number:
import math
import random # importing module
playing = True # intialise
number = str(random.randint(10,20))

print("i will genrate a random number between 10 and 20, you can guess it.")
print("The game ends when you get 1 hero!")

while playing:
    guess = input("Guess a number in between 10 and 20!: ")
    number = str(random.randint(10,20))                                                                           
    if guess == number:
        print("You have guessed the my number! ")
        print(f"The number you guessed was {number}")
        break
    
    else:
        print(f"Incorrect guess, please try again. My guess was: {number}")


# Rock Paper Scissors Game:

options = ["rock", "paper", "scissors"]
user_choice = input("Choose either: Rock, paper, scissors: ")
computer_choice = random.choice(options)

print("You choose", user_choice)
print("Computers choice", computer_choice)

if user_choice == computer_choice:
    print("Its a tie!")
# all computer winning conditons:
elif computer_choice == "rock" and user_choice == "scissors":
    print("Rock smashes scissors. computer wins!")
elif computer_choice == "scissors" and user_choice == "paper":
    print("scissors cut paper. computer wins!")
elif computer_choice == "paper" and user_choice == "rock":
    print("Paper covers rock. computer wins!")
# all user winning conditons:
elif computer_choice == "scissors" and user_choice == "rock":
    print("Rock smashes scissors. u win!")
elif computer_choice == "paper" and user_choice == "scissors":
    print("scissors cut paper. u win!")
elif computer_choice == "rock" and user_choice == "paper":
    print("Paper covers rock. u win!")
# if users chooses anything apart from Rock Paper Scissors
else:
    print("Invalid input")


# Math Module

print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

print(math.ceil(45.490))
print(math.floor(45.890))
print(math.factorial(5))
