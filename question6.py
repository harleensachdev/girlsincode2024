def move_rover(grid, starting, movements):
  x, y = starting

  for move in movements:
      if move == 'L':
          x -= 1
      elif move == 'R':
          x += 1
      elif move == 'F':
          y += 1
      elif move == 'B':
          y -= 1
      x = max(0, min(x, grid[0] - 1))
      y = max(0, min(y, grid[1] - 1))

  return x, y
usersgrid = tuple(map(int, input("Enter the dimensions of chosen lunar grid (format: rows columns, seperated by a space): ").split()))
startingplace = tuple(map(int, input("Enter the starting position of your rover (format: x y): ").split()))
sequence = []
while True:
  inputvalue = input("Enter the directions you want your rover to move in ('L' for left, 'R' for right, 'F' for forward, 'B' for backward) or type 'stop rover' to end: ")
  if inputvalue == 'stop rover':
      break
  sequence.append(inputvalue)
final_position = move_rover(usersgrid, startingplace, sequence)
print("Rover's final position:", final_position)
