from os import replace


file = open("./input.txt", "r")
nums = file.readline().strip().split(",")
nextLine = file.readline()
boards = []
board = []
while True:
  thisLine = file.readline()
  if len(thisLine) == 0:
    boards.append(board)
    break
  if len(thisLine) < 5:
    boards.append(board)
    board = []
    continue
  
  else:
    toAppend = thisLine.strip().replace("  ", " ").split(" ")
    toAppend = [int(num) for num in toAppend]
    board.append(toAppend)

file.close()
nums = [int(num) for num in nums]
# print(nums)

def checkArr(arr):
  return len(set(arr)) == 1

def checkBoard(board):
  # check rows
  for row in board:
    if checkArr(row):
      return board
  
  # check columns
  for i in range(len(board)):
    col = [board[j][i] for j in range(len(board[i]))]
    if checkArr(col):
      return board
  return False

def breplace(num):
  for board in boards:
    for line in board:
      for i, value in enumerate(line):
        if value == num:
          line[i] = "Y"
          
def replaceAndCheck():
  for number in nums:
    breplace(number)
    
    
    for i, board in enumerate(boards):
      result = checkBoard(board)
      if result:
        won[i] = True
        if won.count(False) == 0:
          sum = 0
          for row in result:
            for num in row:
              if type(num) == int:
                sum += num
          return sum * number
        

won = [False for i in range(len(boards))]

  
print(replaceAndCheck())