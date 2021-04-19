period = int(input())
doctors = 7

untreated_patients = 0
treated_patients = 0


for day in range(1, period + 1):
    patients_for_day = int(input())
    if day % 3 == 0:
        if untreated_patients >= treated_patients:
            doctors += 1
    if patients_for_day >= doctors:
        untreated_patients += patients_for_day - doctors
        treated_patients += doctors
    else:
        treated_patients += patients_for_day

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")


