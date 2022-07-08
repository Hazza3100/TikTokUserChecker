import random
import string


name = input("Enter Start name: ")
amount = input("Enter amount of users: ")

user = name + "".join(random.choices(string.ascii_letters, k=3))

for i in range(int(amount)):
    with open('usernames.txt', 'a') as f:
        f.write(f'{user}\n')
