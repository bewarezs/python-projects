
import requests
import itertools
import string
import threading
import random
import os
from colorama import Fore, Back, Style, init

init()

found = []
lock = threading.Lock()
checked_count = 0

def clear():
    os.system('cls')

def print_header():
    print(Fore.GREEN + """
██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗
██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝
██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝ 
██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗ 
██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
    USERNAME SCANNER v2.0 - MATRIX EDITION
""")

def check_username(username):
    global checked_count
    url = "https://auth.roblox.com/v1/usernames/validate"
    params = {"Username": username, "Birthday": "2000-01-01"}
    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        with lock:
            checked_count += 1
            print(Fore.CYAN + f"  >> Checking: {username}" + " " * 20)
            if data.get("code") == 0:
                print(Fore.YELLOW + "█" * 50)
                print(Fore.GREEN + f"  [AVAILABLE] >>>  {username}  <<<")
                print(Fore.YELLOW + "█" * 50)
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
    clear()
    print_header()
    print(Fore.GREEN + "  Initializing scanner...")
    print(Fore.GREEN + "  " + "=" * 48)

    threads = []
    for length in range(3, 5):
        print(Fore.GREEN + f"\n  [*] Scanning {length}-letter usernames...\n")
        for username in generate_usernames(length):
            thread = threading.Thread(target=check_username, args=(username,))
            threads.append(thread)
            thread.start()
            if len(threads) % 50 == 0:
                for t in threads:
                    t.join()
                threads = []
                print(Fore.GREEN + f"  [*] Checked: {checked_count} | Found: {len(found)}")

    print(Fore.GREEN + f"\n\n  [DONE] Checked {checked_count} usernames.")
    print(Fore.GREEN + f"  [DONE] Found {len(found)} available usernames.")
    print(Fore.GREEN + "  Results saved to available_usernames.txt")

if __name__ == "__main__":
    main()


