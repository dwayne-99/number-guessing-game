import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
  attempts = 10
else:
  attempts = 5

computer_num = random.randint(1, 100)

for i in range(attempts):
    print(f"You have {attempts - i} attempts remaining to guess the number.")
    user_input = int(input("Make a guess: "))
    if user_input == computer_num:
        print("Your guess is correct, You win!")
        break
    elif user_input > computer_num:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
else:
    print(f"You ran out of attempts. The number was {computer_num}.")
 
# Prints the remaining attempts for the user (line 16)
# Takes the users guess into a variable: user_input (line 17)
# Compares the users guess to the computer number and prints the corresponding message (lines 18-24)
# If the user runs out of attempts, the print statement on (line 26) is executed