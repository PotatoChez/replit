import random

def loopy():
  while True:
    d = input("Do you want to continue? (Y/n)")
    print(d)
    d = d.strip().lower()
    if d != "y" and d != "n":
      print ("Invalid Input, Y or N")
    elif d == "y":
      print ("pew pew pew !!")
    else:
      break
      
def gam():
    print("INSTRUCTIONS:\nRock, Paper, Scissor! type r for Rock, p for Paper, s for Scissors, and q for Quit(case sensitive, must use lowercase)")
    print("_____________________________________")
    win = 0
    lose = 0
    tie = 0
    while True:
      n = random.randint(1, 3)
      e = input("Enter here:")
      b = {'r': 1, 's': 2, 'p': 3, 'q': 4}
      com = {1: 'Rock', 2: 'Scissors', 3: 'Paper', 4: 'Quit'}
      #print(randomlist)
      data = b.get(e, None)
      if data is None:
        print("Invalid, you may have done an uppercase letter or made a spelling error. Here are the instructions:")
        print("INSTRUCTIONS:\nRock, Paper, Scissor! type r for Rock, p for Paper, s for Scissors, and q for Quit(case sensitive, must use lowercase)")
        print("__________________________________________________")
        continue
      
      if data != 4:
        print(com[data])
        print(com[n])
        
      if n == data:
          print('tie')
          tie = tie + 1
      elif n == 1 and data == 2:
          print("You lost!")
          lose = lose + 1
      elif n == 1 and data == 3:
          print("You win!")
          win = win + 1
      elif n == 2 and data == 1:
          print('You win!')
          win = win + 1
      elif n == 2 and data == 3:
          print('You lost!')
          lose = lose + 1
      elif n == 3 and data == 1:
          print('You lost!')
          lose = lose + 1
      elif n == 3 and data == 2:
          print('You win!')
          win = win + 1
      elif data == 4:
        print('byeeeeeeeeeeeeeeeeeeeeee')
        break
      print("Results:")
      print(f"{win} Wins, {lose} Losses, {tie} Ties")
      p = input("do you want to keep playing?(y for yes, n for no)>")
      if p == 'n':
        print('why you no like my game :(')
        break
      while True:
        if p != 'n' and p != 'y':
          print("INVALID")
          p = input("do you want to keep playing?(y for yes, n for no)>")

        if p == 'y':
          break
if __name__ == '__main__':
    gam()
