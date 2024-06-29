import random

def generate_password(length):
  
  lowercase = "abcdefghijklmnopqrstuvwxyz"
  uppercase = lowercase.upper()
  digits = "0123456789"
  symbols = "!@#$%^&*()"

  characters = lowercase + uppercase + digits + symbols

  password = random.choice(lowercase) + random.choice(uppercase) + random.choice(digits) + random.choice(symbols)

  password += ''.join(random.choices(characters, k=length - 4))

  password_list = list(password)
  random.shuffle(password_list)
  password = ''.join(password_list)

  return password

password_length = int(input("Enter desired password length : "))

generated_password = generate_password(password_length)
print("The Simple Generated password is :", generated_password)
