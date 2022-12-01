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
    return
  
  def solve2(self):
    return


data = "INSERT URL PATH HERE"
elf = Elf(data)