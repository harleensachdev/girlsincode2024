def validcell(grid, row, col): #check?
  if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
      return False
  else:
      return True

def iswatersource(grid, row, col):
  if grid[row][col] > -5:
      return False #notwatersource
  for i in range(-1, 2):
      for j in range(-1, 2):
          if validcell(grid, row + i, col + j) and (i != 0 and j != 0): #all neighbouring cells have high elevation
              if grid[row][col] >= grid[row + i][col + j]:
                  return False
  else:
      return True

def potentialwatersource(grid): #goes through to find watersources, add tolist
  potentialwatersource = []
  for i in range(len(grid)):
      for j in range(len(grid[0])):
          if iswatersource(grid, i, j):
              potentialwatersource.append((i, j))
  return potentialwatersource


grid = [[3, 4, 0],
      [5, 2, 3],
      [4, -9, -4]]


finalwatersource = potentialwatersource(grid)
for source in finalwatersource:
  print(source)
