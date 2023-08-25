from collections import deque

male_nums = deque(int(x) for x in input().split())
female_nums = deque(int(x) for x in input().split())
matches = 0

while male_nums and female_nums:
    male = male_nums.pop() if female_nums[0] > 0 or male_nums[-1] <= 0 else 0
    female = female_nums.popleft() if female_nums[0] <= 0 or male > 0 else 0

    if male and female:
        if male % 25 == 0 and female % 25 == 0:
            male_nums.pop()
            female_nums.popleft()
            continue

        if male % 25 == 0:
            if male_nums:
                male_nums.pop()
                female_nums.appendleft(female)
                continue

        if female % 25 == 0:
            if female_nums:
                female_nums.popleft()
                male_nums.append(male)
                continue

        else:
            if female == male:
                matches += 1
            else:
                male -= 2
                male_nums.append(male)


print(f'Matches: {matches}')
print(f'Males left: {", ".join(str(l) for l in reversed(male_nums)) if male_nums else "none"}')
print(f'Females left: {", ".join(str(l) for l in female_nums) if female_nums else "none"}')