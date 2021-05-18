day_of_call = input("Enter the day the call started at: ")
time_of_call = int(input("Enter the time the call started at (hhmm): "))
dura_of_call = int(input("Enter the duration of the call (in minutes): "))

if day_of_call == 'Mon' or day_of_call == 'Tue' or day_of_call == 'Wed' or day_of_call == 'Thr' or day_of_call == 'Fri':
    if 800 <= time_of_call <= 1800:
        rate = .4
    else:
        rate = .25
else:
    rate = .15

total_charge = rate * dura_of_call

print(f'This call will cost ${round(total_charge, 2):.2f}')

