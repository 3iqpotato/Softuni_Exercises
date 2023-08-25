first_char = input()
last_char = input()
start_num = ord(first_char)
end_num = ord(last_char)
input_string = input()
sum_ch = 0
for ch in input_string:
    if start_num < ord(ch) < end_num:
        sum_ch += ord(ch)
print(sum_ch)

