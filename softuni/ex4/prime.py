num = input()

prime = 0
non_prime = 0
while num != "stop":
    num = int(num)
    if num < 0:
        print("Number is negative.")
        num = input()
        continue
    times = 0
    for n in range(1, num + 1):
        core = num % n
        if core == 0:
            times += 1
    if times > 2:
        prime += num
    else:
        non_prime += num
    num = input()
print(f"Sum of all prime numbers is: {non_prime}")
print(f"Sum of all non prime numbers is: {prime}")

