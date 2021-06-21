from random import choice
from os import system
from inflection import pluralize

def fill_data():
  convert = str.maketrans('áéíóú', 'aeiou')

  with open("./files/data.txt", "r", encoding="utf-8") as f:
    return [line.translate(convert).upper().rstrip("\n") for line in f]


def validate_input(message):
  while True:
    try:
      character = input(message).upper()

      if len(character) == 0:
        raise ValueError("You have to enter a letter")
      elif len(character) > 1:
        raise ValueError("You must enter only one letter")
      elif character.isnumeric(): 
        raise ValueError("It must be a letter, not a number")
      
      return character

    except ValueError as ve:
      print(ve)
      

def start_game(word_random, word_to_guess):
  attempts = 5

  print("Guess the word!")
  print(f"You have {attempts} attempts. For every hit you win one more attempt.")

  while '-' in word_to_guess:
    print(' '.join(word_to_guess))
    character = validate_input("Enter a letter: ")

    right_guess = False

    for index, letter in enumerate(word_random):
      if letter == character:
        word_to_guess[index] = character
        right_guess = True
    
    attempts = attempts + 1 if right_guess else attempts - 1
    
    if attempts == 0:
      system("cls || clear")
      return print(f"Sorry! The word right was {word_random}.")

    system("cls || clear")
    print("Guess the word!")
    print(f"You have {attempts} {pluralize('attempt') if attempts > 1 else 'attempt'} left.")

  system("cls || clear")
  print(f"Won! The word was {word_random}")


def run():
  data = fill_data()
  word_random = choice(data)
  word_to_guess = list(('-' * len(word_random)))
  start_game(word_random, word_to_guess)


if __name__ == "__main__":
  system("cls || clear")
  run()