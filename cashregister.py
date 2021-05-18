first_item = float(input("Enter price of the first item: "))
second_item = float(input("Enter price of the second item: "))
card_input = input("Does customer have a club card? (Y/N): ")
card_bool = None
if card_input == "Y" or card_input == "y":
    card_bool = True
elif card_input == "N" or card_input == "n":
    card_bool = False
else:
    print("Card input error!")
tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: ")) * .01
base_price = first_item + second_item
print(f'Base price = {round(base_price, 2):.2f}')
disc_amt = None
total_price = None
if first_item >= second_item:
    second_item = second_item / 2
else:
    first_item = first_item / 2
if card_bool:
    disc_amt = (first_item + second_item) * .10
    after_disc = (first_item + second_item) - disc_amt
    total_price = (after_disc * tax_rate) + after_disc
    print(f'Price after discounts = {round(after_disc, 2):.2f}')
    print(f'Total price = {round(total_price, 2):.2f}')
else:
    print(f'Price after discounts = {round((first_item + second_item), 2):.2f}')
    total_price = first_item + second_item
    total_tax = total_price * tax_rate + total_price
    print(f'Total price = {round(total_tax, 2):.2f}')

