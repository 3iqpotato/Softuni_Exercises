times = int(input())
dict_registered = {}
for _ in range(times):
    input_data = input().split()
    command = input_data[0]
    if command == 'register':
        name = input_data[1]
        code = input_data[2]
        if name in dict_registered:
            print(f"ERROR: already registered with plate number {dict_registered[name]}")
        else:
            dict_registered[name] = code
            print(f"{name} registered {code} successfully")
    elif command == 'unregister':
        name = input_data[1]
        if name not in dict_registered:
            print(f"ERROR: user {name} not found")
        else:
            dict_registered.pop(name)
            print(f"{name} unregistered successfully")

for name in dict_registered:
    print(f'{name} => {dict_registered[name]}')