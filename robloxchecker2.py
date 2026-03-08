import requests
import itertools
import string
import time
import threading

found = []
lock = threading.Lock()

def check_username(username):
    url = "https://auth.roblox.com/v1/usernames/validate"
    params = {"Username": username, "Birthday": "2000-01-01"}
    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        if data.get("code") == 0:
            with lock:
                print(f"  [AVAILABLE] {username}")
                found.append(username)
                with open("available_usernames.txt", "a") as f:
                    f.write(username + "\n")
    except:
        pass

def generate_usernames(length):
    chars = string.ascii_lowercase + string.digits + "_"
    for combo in itertools.product(chars, repeat=length):
        yield "".join(combo)

def main():
    print("=== Roblox Username Finder ===")
    threads = []
    checked = 0
    for length in range(3, 5):
        print(f"Checking {length}-letter usernames...")
        for username in generate_usernames(length):
            thread = threading.Thread(target=check_username, args=(username,))
            threads.append(thread)
            thread.start()
            checked += 1
            if len(threads) % 50 == 0:
                for t in threads:
                    t.join()
                threads = []
                print(f"  ...checked {checked} usernames, found {len(found)} available")
    print(f"Done! Found {len(found)} available usernames.")

if __name__ == "__main__":
    main()