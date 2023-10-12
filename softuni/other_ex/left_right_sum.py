numbers = int(input())
score1 = 0
score2 = 0
for num in range(numbers * 2):
    if num < numbers:
        first_numbers = int(input())
        score1 += first_numbers
    else:
        second_numbers = int(input())
        score2 += second_numbers

if score1 == score2:
    print(f'Yes, sum = {score2}')
else:
    diff = abs(score2 - score1)
    print(f'No, diff = {diff}')