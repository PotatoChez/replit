import math
def areas():
  print("Areas")
  with open ("tut4.txt") as f:
    for line in f:
      data = line.strip().split(",")
      print(data)
      data1 = int(data[0])
      if len(data) == 1:
        circle_area = round(data1 * data1 * math.pi, 3)
        print(f"Area = {circle_area}")
      elif len(data) == 2:
        triangle_area = round(int(data[1]) * data1 * 0.5, 2)
        print(f"Area = {triangle_area}")
      elif len(data) == 3:
        trapezoid = 0.5 * int(data[0]) * (int(data[1]) + int(data[2]))
        print("Area = ", trapezoid)
      print("---------------------------")
if __name__ == "__main__":
  areas()