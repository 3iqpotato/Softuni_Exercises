longest_internation_space = set()

for _ in range(int(input())):
    data1, data2 = [list(map(int, el.split(',')))for el in input().split('-')]

    lenght_1 = set(range(data1[0], data1[1] + 1))
    lenght_2 = set(range(data2[0], data2[1] + 1))

    internation_space = lenght_1.intersection(lenght_2)

    if len(internation_space) > len(longest_internation_space):
        longest_internation_space = internation_space


print(
    f"Longest intersection is " 
    f"[{', '.join(str(el) for el in longest_internation_space)}] with length {len(longest_internation_space)}"
)
