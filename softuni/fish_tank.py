widht = int(input())
lenght = int(input())
height= int(input())
percent_full = float(input())

volume = widht * lenght * height
volume_in_liters = volume / 1000
full_space_in_pertcent = percent_full / 100
needed_liters = volume_in_liters*(1-0.17)
print(needed_liters)