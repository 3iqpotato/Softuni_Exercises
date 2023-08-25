times = int(input())
my_dict = {}
for _ in range(times):
    word = input()
    meaning = input()
    if word in my_dict:
        my_dict[word].append(meaning)
    else:
        my_dict[word] = [meaning]

for word in my_dict:
    print(f"{word} - {', '.join(my_dict[word])}")
# 2
# task
# problem
# task
# assignment
# 3
# cute
# adorable
# cute
# charming
# smart
# clever