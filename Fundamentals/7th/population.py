population = [int(x) for x in input().split(", ")]
min_number = int(input())
if sum(population) / len(population) < min_number:
    print('No equal distribution possible')
else:
    for num in range(len(population)):
        max_value = max(population)
        index = population.index(max_value)
        while population[num] < min_number:
            population[num] += 1
            population[index] -= 1
    print(population)



