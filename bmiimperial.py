pounds = float(input("Please enter weight in pounds: "))
inches = float(input("Please enter height in inches: "))

kilos = pounds * 0.453592
meters = inches * 0.0254

bmi = kilos/meters**2

print(f'BMI is: {bmi}')
