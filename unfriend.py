import requests
import time

cookie = input("Paste your .ROBLOSECURITY cookie:")
session = requests.Session()
session.cookies.set(".ROBLOSECURITY", cookie)

token_response = session.post("https://auth.roblox.com/v1/logout")
csrf_token = token_response.headers.get("x-csrf-token")
session.headers["X-Csrf-Token"] = csrf_token

response = session.get("https://users.roblox.com/v1/users/authenticated")
data = response.json()
user_id = data["id"]
print("Logged in as:", data["name"])

friends_response = session.get(f"https://friends.roblox.com/v1/users/{user_id}/friends")
friends_data = friends_response.json()
friends = friends_data["data"]
print("Total friends found:", len(friends))

for friend in friends:
    friend_id = friend["id"]
    session.post(f"https://friends.roblox.com/v1/users/{friend_id}/unfriend")
    print("Unfriended:", friend_id)
    time.sleep(0.5)