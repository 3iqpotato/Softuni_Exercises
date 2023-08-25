num = int(input())
correct = 0
for x1 in range(num + 1):
    for x2 in range(num + 1):
        for x3 in range(num + 1):
            if x1 + x3 + x2 == num:
                correct += 1
print(correct)