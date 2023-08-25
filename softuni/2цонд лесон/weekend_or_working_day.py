day = input()
if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    print("Working day")
elif day in ['Sunday', 'Saturday']:
    print("Weekend")
else:
    print('Error')