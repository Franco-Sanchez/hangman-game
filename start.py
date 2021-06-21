from random import choice

DATA = []

def start_game(word_random, word_spaces):
  bad_attempts = 0

  while '-' in word_spaces:
    print('¡Adivina la palabra!')
    word_spaces = list(read_data())
    print(' '.join(word_spaces))
    word_input = input("Ingresa una letra: ").upper()

    for index, letter in enumerate(word_random):
      if letter == word_input:
        word_spaces[index] = word_input
      else:
        bad_attempts += 1

    write_data(''.join(word_spaces))


def fill_data():
  with open("./files/data.txt", "r", encoding="utf-8") as f:

    for line in f:
      DATA.append(line.upper().rstrip("\n")) # agrega el elemento a la lista y borra los saltos de línea


def write_data(word):
  with open('./files/word.txt', 'w', encoding="utf-8") as f:
    f.write(word)


def read_data():
  with open('./files/word.txt', "r", encoding="utf-8") as f:
    for line in f:
      return line


def validate_input():
  pass


def run():
  fill_data()
  convert = str.maketrans('ÁÉÍÓÚ', 'AEIOU')
  word_random = (choice(DATA)).translate(convert)
  word_spaces = ('-' * len(word_random))
  write_data(word_spaces)
  start_game(word_random, word_spaces)


if __name__ == "__main__":
  run()