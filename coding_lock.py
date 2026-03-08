import subprocess
import random

challenges = [
    "Write a program that prints the numbers 1 to 10",
    "Write a program that asks your name and prints hello back",
    "Write a program that adds two numbers together"
]

challenge = random.choice(challenges)
print("Complete your coding challenge to unlock Roblox!")

print(challenge)

answer = input("Type DONE when you completed the callenge  ")

if answer == "DONE":
    subprocess.Popen(r"C:\Users\tykei\AppData\Local\Roblox\Versions\version-d599f7fc52a8404c\RobloxPlayerBeta.exe")
else:
    print("You haven't completed the challenge yet!")
