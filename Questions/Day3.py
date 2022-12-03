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

    self.itemPriorities = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13
                          ,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

  def solve1(self):
    sum = 0
    for row in self.data:
      leftCompartment = row[:int(len(row)/2)]
      rightCompartment = row[int(len(row)/2):]

      sharedItem = ""

      for item in leftCompartment:
        if item in rightCompartment:
          sharedItem = item
          break

      sum += 26 + self.itemPriorities.get(sharedItem.lower()) if sharedItem.isupper() else self.itemPriorities.get(sharedItem)
    print(sum)
      
  
  def solve2(self):
    
    sum = 0

    for tripletIndex in range(int(len(self.data)/3)):
      triplet = self.data[tripletIndex * 3: (tripletIndex + 1) * 3]
      
      sharedItem = ""

      for item in triplet[0]:
        if item in triplet[1] and item in triplet[2]:
          sharedItem = item

      sum += 26 + self.itemPriorities.get(sharedItem.lower()) if sharedItem.isupper() else self.itemPriorities.get(sharedItem)
    
    print(sum)

data = "Data/Day3.txt"
elf = Elf(data)
elf.solve2()