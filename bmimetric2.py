kilos = float(input("Please enter weight in kilograms: "))
meters = float(input("Please enter height in meters: "))
bmi = kilos/meters**2
status = None
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi <= 24.9:
    status = "Normal"
elif 25 <= bmi <= 29.9:
    status = "Overweight"
elif bmi >= 30:
    status = "Obese"
else:
    status = "Invalid input!"

print(f'BMI is: {round(bmi, 2)}, Status is {status}')
