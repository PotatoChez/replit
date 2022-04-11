import math
def tutorial():
  with open('tut02.txt') as f:
    for line in f:
      data = line.strip().split(',')
      print(data[0], '|', data[1])
      base = int(data[0])
      height = int(data[1])
      square_base = base * base
      square_height = height * height
      square_diagonal = square_base + square_height
      diagonal = round(math.sqrt(square_diagonal), 2)
      print("Diagonal:", diagonal)
      print("____________________________________")
if __name__ == '__main__':
  tutorial()
  