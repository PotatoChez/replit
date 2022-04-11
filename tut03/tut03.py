def triangle():
  print("triangle");
  with open("tut03.txt") as f:
    for line in f:
      data = line.strip().split(",")
      data.sort()
      print(data[0], data[1], data[2])
      a = int(data[0])
      b = int(data[1])
      c = int(data[2])
      print("A:", a)
      print("B:", b)
      print("C:", c)
      ab = a + b
      print("AB:", ab)
      if ab >= c:
        print("True")
      else:
        print("False")
      print("____________________")
if __name__ == "__main__":
  triangle()