list_clothes = [int(x) for x in input().split()]
capacity = int(input())
racks = 1
rack_capacity = capacity

for _ in range(len(list_clothes)):
    cloth = list_clothes.pop()
    if rack_capacity >= cloth:
        rack_capacity -= cloth
    else:
        racks += 1
        rack_capacity = capacity - cloth

print(racks)