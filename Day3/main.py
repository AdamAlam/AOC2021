file = open("./Day3/input.txt", "r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

n = len(lines)


def part1():
  gamma = ""
  eps = ""
  for i in range(len(lines[0])):
    check = [line[i] for line in lines]
    if check.count("0") < n/2:
      gamma += "1"
      eps += "0"
    else:
      gamma += "0"
      eps += "1"
  return int(gamma, 2) * int(eps, 2)


def part2():
  ox = ""
  co2 = ""
  keptBits = lines[::]
  for i in range(len(lines[0])):
    checkBit = [bit[i] for bit in keptBits]
    keep = "1"
    if checkBit.count("0") > checkBit.count("1"):
      keep = "0"
    keptBits = [bit for bit in keptBits if bit[i] == keep]
    if len(keptBits) == 1:
      ox = keptBits[0]
      break
    
    
  keptBits = lines[::]
  for i in range(len(lines[0])):
    checkBit = [bit[i] for bit in keptBits]
    keep = "0"
    if checkBit.count("0") > checkBit.count("1"):
      keep = "1"
    keptBits = [bit for bit in keptBits if bit[i] == keep]
    if len(keptBits) == 1:
      co2 = keptBits[0]
      return int(ox, 2) * int(co2, 2)
    
  
