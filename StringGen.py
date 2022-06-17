import random, string, sys


def save(code):
    file = open("strings.txt", 'a')
    write_code = code + "\n"
    file.write(write_code)
    file.close()


amount = int(input("Amount Of Strings > "))

for x in range(int(amount)):
    userStart = ''.join(random.choices(string.ascii_letters, k=4))
    save(userStart)
    print(f"Generated | {userStart} ")
