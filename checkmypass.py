import requests
import hashlib
import sys
import os
import getpass
import colorama
from colorama import Fore, Style

colorama.init()

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    # timeout prevents the script from hanging indefinitely if the API is
    # slow or unreachable
    res = requests.get(url, timeout=10)
    if res.status_code != 200:
       raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again. ')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':', 1) for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main():
    # Passwords are read via getpass (hidden input) instead of command-line
    # arguments, so they never land in shell history or show up to other
    # users on the machine via `ps`/process listings.
    print("Enter a password to check (input hidden). Press Enter on a blank line to finish.\n")
    checked_any = False
    while True:
        password = getpass.getpass("Password: ")
        if not password:
            break
        checked_any = True
        count = pwned_api_check(password)
        if count:
            clear_screen()
            print(f'{Fore.RED}Found in {count} breach(es)... You should change it!{Style.RESET_ALL}')
        else:
            print(f'{Fore.GREEN}Not found in any known breach -- good to go!{Style.RESET_ALL}')
    if not checked_any:
        print(f'{Fore.YELLOW}No input detected. Nothing checked.{Style.RESET_ALL}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
