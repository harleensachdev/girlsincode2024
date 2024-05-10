def decrypt(text):
  answer = ''
  for letter in text:
      if letter.isalpha():
          if letter.isupper():
              answer += chr((ord(letter) - 70) % 26 + ord('A'))
          elif letter.islower():
              answer += chr((ord(letter) - 102) % 26 + ord('a'))
      else:
          answer += letter
  return answer

while True:
  encrypted_message = input("Enter message to decrypt: ")
  if encrypted_message == "stop program":
      exit()
  else:
      decrypted_message = decrypt(encrypted_message)
      print("Decrypted message: {}".format(decrypted_message))