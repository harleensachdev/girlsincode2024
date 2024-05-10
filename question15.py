def calculate(number):
  number /= 3
  number += 200
  number *= 25
  number -= 1000
  number *= 10
  number -= 17
  number *= 18
  number += 1790
  number /= 5
  number -= 78
  number += 57
  number *= 2
  return round(number,1)

number = 7

print("Result for {} is {}".format(number, calculate(number)))
