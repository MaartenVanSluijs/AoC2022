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

  def solve1(self):
    self.elf_calories = []
    calories = 0
    
    for row in self.data:
      if row != "":
        calories += int(row)
      else:
        self.elf_calories.append(calories)
        calories = 0
    
    print(max(self.elf_calories))
    
  
  def solve2(self):
    self.elf_calories.sort()
    print(sum(self.elf_calories[-3:]))

data = "Data/Day1.txt"
elf = Elf(data)
elf.solve1()
elf.solve2()