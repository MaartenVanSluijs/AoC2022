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
    myScore = 0
    for row in self.data:
      myScore += self.getScore1(row)
    print(myScore)
    
  
  def solve2(self):
    myScore = 0
    for row in self.data:
      myScore += self.getScore2(row)
    print(myScore)

  def getScore1(self, game):
    if game[2] == "X":
      if game[0] == "A":
        return 4
      elif game[0] == "B":
        return 1
      elif game[0] == "C":
        return 7
    elif game[2] == "Y":
      if game[0] == "A":
        return 8
      elif game[0] == "B":
        return 5
      elif game[0] == "C":
        return 2
    else:
      if game[0] == "A":
        return 3
      elif game[0] == "B":
        return 9
      elif game[0] == "C":
        return 6

  def getScore2(self, game):
    if game[2] == "X":
      if game[0] == "A":
        return 3
      elif game[0] == "B":
        return 1
      elif game[0] == "C":
        return 2
    elif game[2] == "Y":
      if game[0] == "A":
        return 4
      elif game[0] == "B":
        return 5
      elif game[0] == "C":
        return 6
    else:
      if game[0] == "A":
        return 8
      elif game[0] == "B":
        return 9
      elif game[0] == "C":
        return 7

data = "Data/Day2.txt"
elf = Elf(data)
elf.solve1()
elf.solve2()
# print(elf.data)