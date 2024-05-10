import random
def generate_password(num_letters, num_symbols, num_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    passwordjoined = ''.join(random.sample(letters, num_letters) + random.sample(symbols, num_symbols) + random.sample(numbers, num_numbers))
    passwordlist = list(passwordjoined)
    random.shuffle(passwordlist)
    finalpassword = ''.join(passwordlist)
    return finalpassword
numberofletters = int(input("How many letters would you like in your password? "))
numberofsymbols = int(input("How many symbols would you like? "))
numberofnumbers = int(input("How many numbers would you like? "))
generatedpassword = generate_password(numberofletters, numberofsymbols, numberofnumbers)
print("Your password is: {}".format(generatedpassword))
