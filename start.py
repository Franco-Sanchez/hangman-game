DATA = []

def read():
  pass


def start_game():
  print('Adivina la palabra')
  character = input("Ingresa una letra: ")  


def fill_data():
  with open("./files/data.txt", "r", encoding="utf-8") as f:

    for line in f:
      DATA.append(line.rstrip("\n")) # agrega el elemento a la lista y borra los saltos de línea


def run():
  fill_data()
  start_game()


if __name__ == "__main__":
  run()