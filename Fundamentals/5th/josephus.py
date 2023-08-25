list_people = input().split()

num_k = int(input())
dead = []
times = 0
idx = 0
while len(list_people) > 0:
    times += 1

    if times % num_k == 0:
        dead.append(list_people.pop(idx))
    else:
        idx += 1

    if idx >= len(list_people):
        idx = 0

print(str(dead).replace(' ', '').replace('\'', ''))
