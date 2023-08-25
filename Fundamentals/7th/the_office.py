employers_happiness = [int(x) for x in input().split()]
improvement_factor = int(input())
improved_happines = [x*improvement_factor for x in employers_happiness]
happier = [x for x in improved_happines if x >= sum(improved_happines) / len(employers_happiness)]
if len(happier) >= len(employers_happiness) / 2:
    print(f'Score: {len(happier)}/{len(improved_happines)}. Employees are happy!')
else:
    print(f'Score: {len(happier)}/{len(improved_happines)}. Employees are not happy!')