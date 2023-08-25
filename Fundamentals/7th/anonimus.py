def merging(start, end):
    merged = ''
    start = max(0, start)
    end = min(len(threat) - 1, end)
    for _ in range(start, end + 1):
        merged += threat[start]
        threat.remove(threat[start])
    return threat.insert(start, merged)


threat = input().split()

command = input().split()
while '3:1' not in command:
    function = command[0]
    first_idx = int(command[1])
    second_idx = int(command[2])

    if function == 'merge':
        merging(first_idx, second_idx)

    elif function == 'divide':
        if first_idx < 0 or first_idx >= len(threat):
            command = input().split()
            continue
        # word = threat[first_idx]
        # letters = []
        # particles_size = len(word) // second_idx
        # current_partition = ''
        # for idx in range((second_idx - 1) * particles_size):
        #     current_partition += word[idx]
        #     if len(current_partition) == particles_size:
        #         letters.append(current_partition)
        #         current_partition = ''
        # current_partition = ''
        # for idx in range((second_idx - 1) * particles_size, len(word)):
        #     current_partition += word[idx]
        # letters.append(current_partition)
        # threat.pop(first_idx)
        # for partition in range(len(letters)):
        #     threat.insert(first_idx + partition, letters[partition])
        # #
        letters = []
        word = threat[first_idx]
        particles_size = len(word) // second_idx
        for time in range(second_idx):
            letters.append(word[:particles_size])
            word = word[particles_size:]
        letters[-1] += word
        threat.remove(threat[first_idx])
        threat.insert(first_idx, ' '.join(letters))
    command = input().split()
print(" ".join(threat))
