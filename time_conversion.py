print("Please enter 24-hour time format to convert to 12-hour format:")
hour24 = int(input("Hour: "))
min24 = int(input("Minutes: "))

min12 = min24

if 0 <= hour24 <= 11:
    period = "am"
    if hour24 == 0:
        hour12 = 12
    else:
        hour12 = hour24
else:
    period = "pm"
    if hour24 == 12:
        hour12 = 12
    else:
        hour12 = hour24 - 12
print(f'{hour24}:{min24} is {hour12}:{min12} {period}')
