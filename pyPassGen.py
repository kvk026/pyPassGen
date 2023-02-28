import random
import string

length = int(input("Password Length: "))
password = []

if length:
    charList = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    for i in range(length):
        randomchar = random.choice(charList)
        password.append(randomchar)

print("Secure Password: " + "".join(password))
