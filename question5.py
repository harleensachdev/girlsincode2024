def calculate_fuel_consumption(altitude):
  if altitude > 1000:
      fuel_consumption_rate = 20 
  elif altitude > 500:
      fuel_consumption_rate = 13
  else:
      fuel_consumption_rate = 5 
  return fuel_consumption_rate

def simulate_descent(remaining_fuel, altitude):

  while altitude >= 0:
      fuelused = calculate_fuel_consumption(altitude)
      remaining_fuel -= fuelused
      if remaining_fuel < 0:
          print("Lunar lander ran out of fuel.")
          exit()
      else:

          print("Altitude:", altitude, "km - Remaining fuel:", remaining_fuel, "units")

          altitude -= 100

  print("Lunar lander landed with remaining fuel:", remaining_fuel, "units")

originalfuel = 249
originalaltitude = 1599
simulate_descent(originalfuel, originalaltitude)
