def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for i in range(0, len(myList)):
        result = result * myList[i]
    return result
import re
digits_pattern = '\d'
pattern = r'\:{2}[A-Z][a-z]{2,}\:{2}|\*{2}[A-Z][a-z]{2,}\*{2}'
input_line = input()
coll_treshold_list = [int(x) for x in re.findall(digits_pattern, input_line)]
coll_treshold = multiplyList(coll_treshold_list)
dict_emojis = re.findall(pattern, input_line)
print(f'Cool threshold: {coll_treshold}')
print(f"{len(dict_emojis)} emojis found in the text. The cool ones are:")
for emoji in dict_emojis:
    sum_digits = sum(ord(x) for x in emoji[2:-2])
    if sum_digits >= coll_treshold:
        print(emoji)
