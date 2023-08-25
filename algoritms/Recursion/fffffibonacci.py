

f = [0, 1, 1]
num = int(input())
if num < 2:
    print(f[num+1])
else:
    for n in range(2, num+1):
        f.append(f[n-1]+ f[n])
    print(f[num+1])