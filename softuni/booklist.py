lists = int(input())
lists_pre_hour = int(input())
days = int(input())

time_for_read = lists // lists_pre_hour
hours_per_day = time_for_read // days

print(hours_per_day)