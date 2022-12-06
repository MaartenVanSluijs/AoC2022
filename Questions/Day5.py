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

    self.stacks = [ ["V", "N", "F", "S", "M", "P", "H", "J"],
                    ["Q", "D", "J", "M", "L", "R", "S"],
                    ["B", "W", "S", "C", "H", "D", "Q", "N"],
                    ["L", "C", "S", "R"],
                    ["B", "F", "P", "T", "V", "M"],
                    ["C", "N", "Q", "R", "T"],
                    ["R", "V", "G"],
                    ["R", "L", "D", "P", "S", "Z", "C"],
                    ["F", "B", "P", "G", "V", "J", "S", "D"]]

  def move(self, begin, end, amount):
    item = self.stacks[begin-1][0:amount]
    self.stacks[begin-1] = self.stacks[begin-1][amount:]
    self.stacks[end-1] = item + self.stacks[end-1]

  def solve1(self):
    for row in self.data:
      amount = row.split(" from ")[0].split(" ")[1]
      begin = row.split(" from ")[1].split(" to ")[0]
      end = row.split(" from ")[1].split(" to ")[1]
      
      self.move(int(begin), int(end), int(amount))
    
    for row in self.stacks:
      print(row)

  
  def solve2(self):
    for row in self.data:
      amount = row.split(" from ")[0].split(" ")[1]
      begin = row.split(" from ")[1].split(" to ")[0]
      end = row.split(" from ")[1].split(" to ")[1]
      
      self.move(int(begin), int(end), int(amount))
  
    for row in self.stacks:
      print(row)


data = "Data/Day5.txt"
elf = Elf(data)
elf.solve2()