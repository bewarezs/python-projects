import requests
import itertools
import string
import time

def check_username(username):
    url = "https://auth.roblox.com/v1/usernames/validate"
    params = {"Username": username, "Birthday": "2000-01-01"}
    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        return data.get("code") == 0
    except:
        return None

def generate_usernames(length):
    chars = string.ascii_lowercase + string.digits + "_"
    for combo in itertools.product(chars, repeat=length):
        yield "".join(combo)

def main():
    print("=== Roblox Username Finder ===")
    found = []
    checked = 0
    for length in range(3, 5):
        print(f"Checking {length}-letter usernames...")
        for username in generate_usernames(length):
            result = check_username(username)
            checked += 1
            if result is True:
                print(f"  [AVAILABLE] {username}")
                found.append(username)
                with open("available_usernames.txt", "a") as f:
                    f.write(username + "\n")
            if checked % 50 == 0:
                print(f"  ...checked {checked} usernames, found {len(found)} available")
            time.sleep(0.3)
    print(f"Done! Found {len(found)} available usernames.")
    print("Saved to available_usernames.txt")

if __name__ == "__main__":
    main()
