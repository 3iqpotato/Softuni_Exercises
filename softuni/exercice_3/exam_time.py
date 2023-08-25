exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

exam_full_min = (exam_hour * 60) + exam_min
arrive_full_time = (arrive_hour * 60) + arrive_min

diff = abs(exam_full_min - arrive_full_time)
hour = diff // 60
min1 = diff % 60
if exam_full_min > arrive_full_time and 0 < diff <= 30:
    print(f'On time {diff} minutes before the start')
elif exam_full_min == arrive_full_time:
    print('On time')
elif exam_full_min < arrive_full_time and diff < 60:
    print(f'Late {min1} minutes after the start')
elif exam_full_min < arrive_full_time and diff >= 60:
    print(f'Late {hour}:{min1:02d} hours after the start')
elif exam_full_min > arrive_full_time and 60 > diff > 30:
    print(f'Early {min1} minutes before the start')
elif exam_full_min > arrive_full_time and diff >= 60:
    print(f'Early {hour}:{min1:02d} hours before the start')
