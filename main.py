import requests
import threading
import random
import json


from colorama import Fore, init

init(convert=True)


with open('config.json') as f:
    cfg = json.load(f)


useproxy = cfg['use_proxy']


readproxy = open('proxies.txt','r')
readproxy2 = readproxy.readlines()
workproxy = []
for proxy3 in readproxy2:
    proxystrip = proxy3.strip('\n')
    workproxy.append(proxystrip)



def check():

    proxy1 = random.choice(workproxy)
    proxies = {'http': f'http://{proxy1}','https':f'http://{proxy1}'}

    usersf = open("users.txt")
    user = random.choice(usersf.read().splitlines())
    usersf.close()

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    if useproxy == True:
        r = requests.get(f'https://www.tiktok.com/@{user}', headers=header, proxies=proxies)
    else:
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
