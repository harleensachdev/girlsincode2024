def findmaximumconcentration(map):
  max_concentration = 0

  for row in map:
      for mineralconcentration in row:
          if mineralconcentration > max_concentration:
              max_concentration = mineralconcentration
  return max_concentration
map = [
  [100, 440, 3030, 31118],
  [28282, 277272, 343, 3333],
  [223, 33333, 4444, 44],
  [33838,3737373,838,88888888]
]

maxconcentration = findmaximumconcentration(map)
print("Maximum concentration of minerals: {}".format(maxconcentration))
