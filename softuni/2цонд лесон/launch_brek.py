from math import ceil

name_of_soap = input()
soap_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4

free_time = break_time - (lunch_time + rest_time)
diff = ceil(abs(soap_time - free_time))
if free_time >= soap_time:
    print(f"You have enough time to watch {name_of_soap} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_soap}, you need {diff} more minutes.")
