import string
import random
from csv import writer

head = ["Platform", "Pass"]


def passwordGen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    platform = input("Enter name of the Platform> ")
    passLength = int(input("Enter length of the password > "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = ("".join(s[0:passLength]))
    print(password)
    passData = [platform, password]
    with open("pass.csv", "a") as f:
        writeData = writer(f)
        writeData.writerow(passData)


passwordGen()
