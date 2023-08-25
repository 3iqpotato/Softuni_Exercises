def vowel_filter(function):
    vowels = ['a', 'e', 'i', 'u', 'y', 'o']

    def wrapper():
        letters = function()
        return [l for l in letters if l in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
