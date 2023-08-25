def what_kind(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 'zero'
    else:
        if a > 0 and b > 0 and c > 0:
            return 'positive'
        else:
            count_negative = 0
            nums = [a, b, c]
            for x in range(3):
                if nums[x] < 0:
                    count_negative += 1
            if count_negative == 2:
                return 'positive'
            else:
                return 'negative'





num1 = int(input())
num2 = int(input())
num3 = int(input())
print(what_kind(num1, num2, num3))

