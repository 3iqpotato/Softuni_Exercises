people = int(input())
prezent_name = input()
final = 0
prezentations = 0
final_score = 0
while prezent_name != 'Finish':

    full_score = 0
    mid_score = 0
    for i in range(1, people + 1):
        prezentations += 1

        score = float(input())
        full_score += score
        mid_score = full_score / people
        final += score
        final_score = final / prezentations
    print(f'{prezent_name} - {mid_score:.2f}.')
    prezent_name = input()


print(f"Student's final assessment is {final_score:.2f}.")
