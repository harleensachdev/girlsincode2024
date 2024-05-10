def getsmallestnumber(array):
  array.sort()
  smallest_number = array[0]
  return smallest_number

array = []
print("Smallest number in array: {}".format(getsmallestnumber(array)))
