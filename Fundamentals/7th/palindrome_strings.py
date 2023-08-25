def all_palindromes(words):
    palindromes = []
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes

def times_in(word, words):
    count = 0
    for x in words:
        if word == x:
            count += 1
    return count


strings = input().split()
palindrome = input()
found_palindrones = all_palindromes(strings)
print(found_palindrones)
print(f'Found palindrome {times_in(palindrome, found_palindrones)} times')
