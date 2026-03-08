
import requests

username = input("Enter the Roblox username to look up: ")
response = requests.get(f"https://users.roblox.com/v1/users/search?keyword={username}&limit=10")

data = response.json()


if data["data"]:
    print(f"Username: {data['data'][0]['name']}")
    print(f"User ID: {data['data'][0]['id']}")
else:
    print("User not found.")

