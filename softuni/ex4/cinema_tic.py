film_name = input()
students = 0
standart = 0
kids = 0
all_people = 0
percent_full = 0
while film_name != 'Finish':
    free_places = int(input())
    people_movie = 0
    for _ in range(free_places):

        ticket_tipe = input()
        if ticket_tipe == 'End':
            break
        else:
            all_people += 1
            people_movie += 1
            if ticket_tipe == 'student':
                students += 1
            elif ticket_tipe == 'standard':
                standart += 1
            elif ticket_tipe == 'kid':
                kids += 1
    percent_full = people_movie / free_places * 100
    print(f'{film_name} - {percent_full:.2f}% full.')
    film_name = input()
student_per = students / all_people * 100
standard_per = standart / all_people * 100
kids_per = kids / all_people * 100
print(f'Total tickets: {all_people}')
print(f'{student_per:.2f}% student tickets.')
print(f'{standard_per:.2f}% standard tickets.')
print(f'{kids_per:.2f}% kids tickets.')
