#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)

def select_dif():
  difficulty = input("[Hard - 5 attempts] [Easy - 10 attempts]\nSelect the difficulty: ")
  if difficulty == "easy":
    print("You have 10 attempts to guess the number.")
    return 10
  else:
    print("You have 5 attempts to guess the number.")
    return 5

def cpu_number():
  return random.randint(1,100)

def compare(guess,cpu_num):
  if guess == cpu_num:
    print(f"You got it! The answer was {cpu_num}")
    return True
  elif guess > cpu_num:
    print("Too high.")
    return False
  else:
    print("Too low.")
    return False

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
turns = select_dif()

cpu_num = cpu_number()
done = False
while not done:
  guess = int(input("Make a guess: "))
  done = compare(guess, cpu_num)
  turns -= 1
  if turns == 0:
    print("You've run out of guesses, you lose.")
    done = True
  else:
    print(f"You have {turns} attempts remaining to guess the number.")
