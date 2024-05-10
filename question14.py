def happiest_employee(employees, barlengths):
  maxhappy = 0
  for employee, barlengths in zip(employees, barlengths):
      if barlengths > maxhappy:
          maxhappy = barlengths
          happiestguy = employee
          happinessbar = "*" * barlengths

  return happiestguy, happinessbar

employees = ["John", "Bob", "William", "Aryan"]
employeeshappiness = [2, 2, 8, 10]
happiest, bar = happiest_employee(employees, employeeshappiness)
print("Happiest employee: {}".format(happiest))
print("Happiness bar: {}".format(bar))
