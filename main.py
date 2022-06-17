import requests
import threading
import random

from colorama import Fore, init

init(convert=True)


def check():

    usersf = open("users.txt")
    user = random.choice(usersf.read().splitlines())
    usersf.close()

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    r = requests.get(f'https://www.tiktok.com/@{user}', headers=header)
    if r.status_code == 200:
        print(Fore.RED + f"Taken | {Fore.RESET}{user}\n")
    else:
        print(Fore.GREEN + f"Available {Fore.RESET}| {user}\n")
        t = open('valid.txt', 'a')
        t.write(f'{user}\n')



def start():
    r = input("Amount of users to check: ")
    for i in range(int(r)):
        x = threading.Thread(target=check)
        x.start()

start()
