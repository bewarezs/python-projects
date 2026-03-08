import string
import random

letters = string.ascii_lowercase
numbers = string.digits
symbols = "!@#$%^&*"

all_chars = letters + numbers + symbols

length = int(input("How long do you want your password? "))
password = random.choices(all_chars, k=length)

print("".join(password))