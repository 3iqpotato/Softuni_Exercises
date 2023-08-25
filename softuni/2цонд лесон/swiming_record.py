from math import floor

world_record = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

time_swimming1 = distance_meters * seconds_per_meter
time_delayed = floor(distance_meters / 15) * 12.5
full_time = time_delayed + time_swimming1

if world_record <= full_time:
    diff = full_time - world_record
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {full_time:.2f} seconds.")
