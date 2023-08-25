def words_sorting(*args):
    values = 0
    dict_words = {}
    for word in args:
        value = sum([ord(x) for x in word])
        values += value
        dict_words[word] = value
    if values % 2 == 0:
        return '\n'.join([f'{key} - {value}' for key, value in sorted(dict_words.items(), key=lambda x: x[0])])
    else:
        return '\n'.join([f'{key} - {value}' for key, value in sorted(dict_words.items(), key=lambda x: -x[1])])











print(
 words_sorting(
 'escape',
 'charm',
 'mythology'
 ))
print(
 words_sorting(
 'escape',
 'charm',
 'eye'
 ))