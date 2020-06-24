import random

price = input("Transaction price: ")
price = float(price)
tendered_amount = input("Amount tendered: ")
tendered_amount = float(tendered_amount)
change = tendered_amount - price
change = '%.2f'%change
change = float(change)
if price == tendered_amount:
	print("Exact Change")
else:
	print(change)

five_amount = change/5
if five_amount >= 1:
	five_amount = int(five_amount)
	print("Five Dollar Bill: " + str(five_amount))
else:
	five_amount = 0
change_less_five = change - (5 * five_amount)
change_less_five = '%.2f'%change_less_five
change_less_five = float(change_less_five)

one_amount = change_less_five / 1
if one_amount >= 1:
	one_amount = int(one_amount)
	print("One Dollar Bill: " + str(one_amount))
else:
	one_amount = 0
change_less_one = change_less_five - (1 * one_amount)
change_less_one = '%.2f'%change_less_one
change_less_one = float(change_less_one)

quarter_amount = change_less_one / 0.25
quarter_amount = '%.2f'%quarter_amount
quarter_amount = float(quarter_amount)
if quarter_amount >= 1:
    quarter_amount = int(quarter_amount)
    print("Quarter: " + str(quarter_amount))
else:
    quarter_amount = 0
change_less_q = change_less_one - (0.25 * quarter_amount)
change_less_q = '%.2f'%change_less_q
change_less_q = float(change_less_q)

dime_amount = change_less_q / 0.1
if dime_amount >= 1:
    dime_amount = int(dime_amount)
    print("Dime: " + str(dime_amount))
else:
    dime_amount = 0
change_less_d = change_less_q - (0.1 * dime_amount)
change_less_d = '%.2f'%change_less_d
change_less_d = float(change_less_d)

nickel_amount = change_less_d / 0.05
if nickel_amount >= 1:
    nickel_amount = int(nickel_amount)
    print("Nickel: " + str(nickel_amount))
else:
    nickel_amount = 0
change_less_n = change_less_d - (0.05 * nickel_amount)
change_less_n = '%.2f'%change_less_n
change_less_n = float(change_less_n)

penny_amount = change_less_n / 0.01
if penny_amount >= 1:
	penny_amount = int(penny_amount)
	print("Penny: " + str(penny_amount))
else:
	penny_amount = 0
change_less_p = change_less_n - (0.01 * penny_amount)
