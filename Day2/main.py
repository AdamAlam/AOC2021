file = open("./input.txt", "r")
lines = file.readlines()
file.close()


direc = [line.strip().split() for line in lines]

def part1():
  hor = 0
  dep = 0

  for ins in direc:
    val = int(ins[1])
    if ins[0] == "forward":
      hor += val
    elif ins[0] == "down":
      dep += val
    else:
      dep -= val

  return hor*dep

def part2():
  hor = 0
  dep = 0
  aim = 0
  for ins in direc:
    w = ins[0]
    val = int(ins[1])
    if w == "down":
      aim += val
    elif w == "up":
      aim -= val
    else:
      hor += val
      dep += (aim*val)
  return hor*dep
