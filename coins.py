print("Please enter the amount of money to convert:")

dollars = int(input("# of dollars: ")) * 100
cents = int(input("# of cents: "))
total = dollars + cents

quarters = total // 25
left_over = total - quarters * 25

dimes = left_over // 10
left_over = total - quarters * 25 - dimes * 10

nickels = left_over // 5
left_over = total - quarters * 25 - dimes * 10 - nickels * 5

pennies = left_over // 1

print(f'The coins are {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies')
