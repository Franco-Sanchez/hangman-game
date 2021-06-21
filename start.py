from random import choice

def start_game(word_random, word_to_guess):
  bad_attempts = 0

  while '-' in word_to_guess:
    print(word_random)
    print('¡Adivina la palabra!')
    print(' '.join(word_to_guess))
    character = validate_input("Ingresa una letra: ")

    for index, letter in enumerate(word_random):
      if letter == character:
        word_to_guess[index] = character
      else:
        bad_attempts += 1

  print(f"¡Ganaste! La palabra correcta era {word_random}")


def fill_data():
  convert = str.maketrans('áéíóú', 'aeiou')

  with open("./files/data.txt", "r", encoding="utf-8") as f:
    return [line.translate(convert).upper().rstrip("\n") for line in f]


def validate_input(message):
  while True:
    try:
      character = input(message).upper()

      if len(character) == 0:
        raise ValueError("Tiene que ingresar una letra")
      elif len(character) > 1:
        raise ValueError("Debe ingresar solo una letra")
      elif character.isnumeric(): 
        raise ValueError("Debe ser una letra, no un número")
      
      return character

    except ValueError as ve:
      print(ve)


def run():
  data = fill_data()
  word_random = choice(data)
  word_to_guess = list(('-' * len(word_random)))
  start_game(word_random, word_to_guess)


if __name__ == "__main__":
  run()