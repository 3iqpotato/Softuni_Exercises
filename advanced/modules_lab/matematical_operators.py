from modules.mat_func import mat
import string

num1, sign, num2 = [float(x) if x not in string.punctuation else x for x in input().split()]

print(f'{mat(num1, num2, sign):.2f}')
