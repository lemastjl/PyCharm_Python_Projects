print("Please enter the number of coins:")
quarters = float(input("# of quarters: ")) * .25
dimes = float(input("# of dimes: ")) * .10
nickels = float(input("# of nickels: ")) * .05
pennies = float(input("# of pennies: ")) * .01
total = quarters + dimes + nickels + pennies

dollars = int(total)
cents = int((total - dollars) * 100)

print("The total is " + str(dollars) + " dollars and " + str(cents) + " cents")
