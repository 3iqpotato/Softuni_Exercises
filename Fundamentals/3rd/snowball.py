import sys

num_snowballs = int(input())
max = -sys.maxsize
for _ in range(num_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    ball = (weight / time) ** quality
    if ball > max:
        max = int(ball)
        time_out = time
        quality_out = quality
        weight_out = weight
print(f'{weight_out} : {time_out} = {max} ({quality_out}) ')
