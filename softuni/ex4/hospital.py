period_for_calculation = int(input())

doctors = 7
waiting_patients = 0
reviwed_patients = 0

for days in range(1, period_for_calculation + 1):
    patients = int(input())
    if days % 3 == 0:
        if waiting_patients > reviwed_patients:
            doctors += 1
    if patients > doctors:
        waiting_patients += patients - doctors
        reviwed_patients += doctors
    else:
        reviwed_patients += patients

print(f'Treated patients: {reviwed_patients}.')
print(f'Untreated patients: {waiting_patients}.')

