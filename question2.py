def martianlanguagedetector(input):
  syllables = []
  lengthofinput = len(input)
  index = 0

  while index < lengthofinput:
      k = index + 1
      while k < lengthofinput and input[k] != input[index]:
          k += 1

      if k - index > 1 and input[index:k + 1] == input[index:k + 1][::-1]:
          syllables.append(input[index:k + 1])
      elif k - index > 1:
          return "This isnt martian language"

      index = k + 1

  return "This is martian language" if syllables else "This isnt martian language"
t = 'civickayak'
print(martianlanguagedetector(t))
