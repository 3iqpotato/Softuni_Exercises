# def remove_vowels(word):
#     pr = []
#     for idx in word:
#         if idx.lower() in ['a', 'o', 'u', 'e', 'i']:
#             continue
#         pr.append(idx)
#     return pr
#
#
# word = input()
# print(''.join(remove_vowels(word)))

word = input()
result = [idx for idx in word if idx.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(result))