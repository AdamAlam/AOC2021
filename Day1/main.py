file = open("./input.txt", "r")
lines = file.readlines()
nums = [int(lines[j].strip()) for j in range(len(lines))]

file.close()

def part1():
  count = 0
  for j in range(1, len(nums)):
    if nums[j] > nums[j-1]:
      count += 1
      
  return count
      

def part2():
  
  count = 0
  for i in range(1, len(nums)):
    sum1 = sum(nums[i-1:i+2])
    sum2 = sum(nums[i:i+3])
    if sum2 > sum1:
      count += 1
      
  
  return count

print(part1())
print(part2())