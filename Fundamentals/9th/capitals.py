countries = input().split(", ")
capitals = input().split(", ")

for idx in range(len(countries)):
    print(f"{countries[idx]} -> {capitals[idx]}")
