def xor_gate(input1, input2):
  if input1 not in (0, 1) or input2 not in (0, 1):
      print("Invalid input detected")
      exit()
  else:
      output = input1 ^ input2
      return output
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
print("Output is {}".format(xor_gate(input1, input2)))