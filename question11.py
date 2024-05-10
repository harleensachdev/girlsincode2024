def caesarcipher(plaintext, shift):
  ciphertext = ''
  for letter in plaintext:
      if letter.isalpha():
          if letter.isupper():
              newletter = chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
          else:
              newletter = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
      else:
          newletter = letter
      ciphertext += newletter
  return ciphertext

plaintext = input("Enter the message to encrypt: ")
shift = int(input("Enter your chosen shift: "))
encryptedmessage = caesarcipher(plaintext, shift)
print("Encrypted message: {}".format(encryptedmessage))
