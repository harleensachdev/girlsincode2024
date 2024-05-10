sequence = [3, 7, 11, 15, 19]

for i in range(100):
    newterm = sequence[-1] + 4
    sequence.append(newterm)

print("The full sequence with next 100 terms: {}".format(sequence))
print("Sum of all numbers is {}".format(sum(sequence)))
