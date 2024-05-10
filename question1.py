def roverdrive(grid, commands):
  totalrows = len(grid)
  totalcols = len(grid[0])
  rovermovement = {'L': (0, -1), 'U': (-1, 0), 'D': (1, 0),'R': (0, 1)}
  for i in range(totalrows):
      for j in range(totalcols):
          if grid[i][j] == 1:
              roverrow = i
              rovercol = j
              break
  for command in commands:
      xmove = rovermovement[command][0]
      ymove = rovermovement[command][1]
      roverrow = (roverrow + xmove) % totalrows
      rovercol = (rovercol + ymove) % totalcols
  updatedgrid = [[0] * totalcols for line in range(totalrows)]
  updatedgrid[roverrow][rovercol] = 1

  return updatedgrid

grid = [[0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0]]
commands = 'LLRDDUUDLRLRUDLDULLRRURUDUDDRUDUDDLLRUDLRURRLLDLDU'
answergrid = roverdrive(grid, commands)

for row in answergrid:
  print(row)
