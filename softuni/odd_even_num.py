numbers = int(input())
score_even = 0
score_odd = 0
for num in range(numbers):
    if num % 2 == 0:
        num_even = int(input())
        score_even += num_even
    else:
        num_odd = int(input())
        score_odd += num_odd

if score_even == score_odd:
    print(f'Yes\nSum = {score_even}')
else:
    diff = abs(score_even - score_odd)
    print(f'No\nDiff = {diff}')


