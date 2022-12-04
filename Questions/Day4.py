class Elf:
  def __init__(self, data):
    f = open(data, "r")
    self.data=[]
    string = ""
    for row in f.read():
      if row != "\n":
        string += row
      else:
        self.data.append(string)
        string = ""
    self.data.append(string)

  def solve1(self):
    count = 0

    for row in self.data:
      areas = row.split(",")
      area1 = areas[0]
      area2 = areas[1]

      area1Bounds = area1.split("-")
      area2Bounds = area2.split("-")

      if  int(area1Bounds[0]) <= int(area2Bounds[0]) and int(area1Bounds[1]) >= int(area2Bounds[1]) or \
          (int(area1Bounds[0]) >= int(area2Bounds[0]) and int(area1Bounds[1]) <= int(area2Bounds[1])):
          count += 1

    print(count)
  
  def solve2(self):
    count = 0
    
    for row in self.data:
      areas = row.split(",")
      area1 = areas[0]
      area2 = areas[1]

      area1Bounds = area1.split("-")
      area2Bounds = area2.split("-")

      if  (int(area1Bounds[0]) >= int(area2Bounds[0]) and int(area1Bounds[0]) <= int(area2Bounds[1])) or \
          (int(area1Bounds[1]) >= int(area2Bounds[0]) and int(area1Bounds[1]) <= int(area2Bounds[1])) or \
          (int(area2Bounds[0]) >= int(area1Bounds[0]) and int(area2Bounds[0]) <= int(area1Bounds[1])) :
          count +=1

    print(count)


data = "Data/Day4.txt"
elf = Elf(data)
elf.solve2()