from collections import deque

digit_list = []

input_line = input()
for ch in input_line:
    if ch.isdigit():
        digit_list.append(ch)
        input_line = input_line.replace(ch, '')


take_list = deque()
skip_list = deque()


for idx in range(len(digit_list)):
    if idx % 2 == 0:
        take_list.append(int(digit_list[idx]))
    else:
        skip_list.append(int(digit_list[idx]))

message = ''
while True:
    if take_list:
        take = take_list.popleft()
        skip = skip_list.popleft()
    else:
        break

    message += input_line[:take]
    input_line = input_line[take+skip:]


print(message)



# print(digit_list)
# print(input_line)
# T2exs15ti23ng1_3cT1h3e0_Roppe