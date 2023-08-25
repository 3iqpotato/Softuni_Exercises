season = input()
group_type = input()
students = int(input())
sleeps = int(input())

sport = ''
night_cost = 0
vacantion_cost = 0

if season == 'Spring':
    if group_type == "boys":
        night_cost = 7.2
        sport = 'Tennis'
    elif group_type == "girls":
        night_cost = 7.2
        sport = 'Athletics'
    else:
        night_cost = 9.5
        sport = 'Cycling'
elif season == "Summer":
    if group_type == "boys":
        night_cost = 15
        sport = 'Football'
    elif group_type == "girls":
        night_cost = 15
        sport = 'Volleyball'
    else:
        night_cost = 20
        sport = 'Swimming'
elif season == "Winter":
    if group_type == "boys":
        night_cost = 9.6
        sport = 'Judo'
    elif group_type == "girls":
        night_cost = 9.6
        sport = 'Gymnastics'
    else:
        night_cost = 10
        sport = 'Ski'
vacantion_cost = night_cost * sleeps * students
if 10 <= students < 20:
    vacantion_cost = vacantion_cost * 0.95
elif 20 <= students < 50:
    vacantion_cost = vacantion_cost * 0.85
elif students >= 50:
    vacantion_cost = vacantion_cost * 0.5

print(f'{sport} {vacantion_cost:.2f} lv.')
