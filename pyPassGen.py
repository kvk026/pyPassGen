import random
import string

length = int(input("Password Length: "))
password = ['a'] * length


def genPass(length):
    if length > 7:
        charList = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
        capSpace = random.choice(range(length))
        numSpace = random.choice(range(length))
        spSpace = random.choice(range(length))
    else:
        print("A secure password must be greater than 8 chars")
        quit()
    for i in range(length):
        if i == capSpace:
            password[capSpace - 1] = random.choice(string.ascii_uppercase)
        elif i == numSpace:
            password[numSpace - 1] = random.choice(string.digits)
        elif i == spSpace:
            password[spSpace - 1] = random.choice(string.punctuation)
        else:
            randomchar = random.choice(charList)
            password[i-1] = randomchar
    return password


def check(passw):
    chks = 0
    for i in passw:
        if i in string.ascii_uppercase:
            chks += 1
        if i in string.ascii_lowercase:
            chks += 1
        if i in string.digits:
            chks += 1
        if i in string.punctuation:
            chks += 1
    if chks > 3:
        return True
    else:
        return False

p = []
while True:
    if not check(p):
        p = genPass(length)
    else:
        print("Secure Password: " + "".join(password))
        # p = genPass(length)
        exit()
