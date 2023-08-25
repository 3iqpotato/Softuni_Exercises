import os

while True:
    command, *info = input().split('-')

    if command == 'End':
        break

    if command == 'Create':
        file = os.path.join(os.path.dirname(__file__), info[0])

        with open(file, 'w'):
            pass

    elif command == 'Add':
        file = os.path.join(os.path.dirname(__file__), info[0])
        content = info[1]

        with open(file, 'a') as f:
            f.write(content + '\n')

    elif command == 'Replace':
        try:
            file = os.path.join(os.path.dirname(__file__), info[0])
            old_str = info[1]
            new_str = info[2]

            with open(file, 'r+') as f:
                text = f.read()
                text = text.replace(old_str, new_str)
                f.seek(0)
                f.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif command == 'Delete':
        file = os.path.join(os.path.dirname(__file__), info[0])

        try:
            os.remove(file)
        except FileNotFoundError:
            print("An error occurred")
