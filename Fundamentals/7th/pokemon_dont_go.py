numbers = [int(x) for x in input().split()]

list_removed = []
while True:
    if len(numbers) < 1:
        break
    element_num = int(input())

    if element_num < 0:
        list_removed.append(numbers.pop(0))
        numbers.insert(0, numbers[-1])
        removed_element = list_removed[-1]
        for num in range(len(numbers)):
            if numbers[num] <= removed_element:
                numbers[num] += removed_element
            else:
                numbers[num] -= removed_element
        # print(numbers)
        continue

    if element_num >= len(numbers):
        list_removed.append(numbers.pop(-1))
        numbers.append(numbers[0])
        removed_element = list_removed[-1]
        for num in range(len(numbers)):
            if numbers[num] <= removed_element:
                numbers[num] += removed_element
            else:
                numbers[num] -= removed_element
        # print(numbers)
        continue

    removed_element = numbers[element_num]

    for num in range(len(numbers)):
        if numbers[num] <= removed_element:
            numbers[num] += removed_element
        else:
            numbers[num] -= removed_element
    list_removed.append(removed_element)
    numbers.pop(element_num)
    # print(numbers)
    # print(list_removed)
print(sum(list_removed))

