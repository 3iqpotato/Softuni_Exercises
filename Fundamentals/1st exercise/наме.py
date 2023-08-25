name = input()
num = 0
while True:
    if name == 'Welcome!':
        print("Welcome to Hogwarts.")
        break

    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    else:
        for i in range(len(name)):
            num = i + 1

        if num < 5:
            print(f"{name} goes to Gryffindor.")
        elif num == 5:
            print(f"{name} goes to Slytherin.")
        elif num == 6:
            print(f"{name} goes to Ravenclaw.")
        elif num > 6:
            print(f"{name} goes to Hufflepuff.")
    name = str(input())
