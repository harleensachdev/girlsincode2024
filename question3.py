sequence = [3, 7, 11, 15, 19]

for i in range(100):
    newterm = sequence[-1] + 4
    sequence.append(newterm)

print("The full sequence: {}".format(sequence))
