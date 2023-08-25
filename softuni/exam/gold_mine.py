num_locations = int(input())

for i in range(1, num_locations + 1):
    medium_gold_per_day = float(input())
    days = int(input())
    all_gold = 0
    for m in range(days):
        gold = float(input())
        all_gold += gold
    med_gold = all_gold / days
    if med_gold >= medium_gold_per_day:
        print(f"Good job! Average gold per day: {med_gold:.2f}.")
    else:
        diff = medium_gold_per_day - med_gold
        print(f"You need {diff:.2f} gold.")


