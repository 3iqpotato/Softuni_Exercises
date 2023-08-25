import random

x = random.randint(0, 100)
guessed = False
while not guessed:
    num = int(input())
    if num == x:
        print("Congratulations you guessed the number")
        break
    else:
        if num < x:
            print("Too low")
        else:
            print("Too high")
