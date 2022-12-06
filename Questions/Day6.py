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
    data = self.data[0]
    for index in range(len(data)-3):
      # # print(data[index:index + 4])
      if len(set(data[index:index+4])) == len(data[index:index+4]):
        print(set(data[index:index+4]))
        return index+4        
  
  def solve2(self):
    data = self.data[0]
    for index in range(len(data)-13):
      if len(set(data[index:index+14])) == len(data[index:index+14]):
        print(set(data[index:index+14]))
        return index+14  


data = "Data/Day6.txt"
elf = Elf(data)
print(elf.solve2())