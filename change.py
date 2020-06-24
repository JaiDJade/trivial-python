import random

price = input("Transaction price: ")
if price.lower() == "random":
    price = random.uniform(0,99)
    price = '%.2f'%price
    price = float(price)
    tendered_amount = random.uniform(float(price), 99)
    tendered_amount = '%.2f'%tendered_amount
    tendered_amount = float(tendered_amount)
else:
    price = float(price)
    tendered_amount = input("Amount tendered: ")
    tendered_amount = float(tendered_amount)

change = tendered_amount - price
change = '%.2f'%change
change = float(change)

print("Price: " + str(price))
print("Amount tendered: " + str(tendered_amount))

if price == tendered_amount:
	print("Exact Change")
else:
	print("Change: " + str(change))

# Fifty Dollar Bills
fifty_amount = change/50
if fifty_amount >= 1:
	fifty_amount = int(fifty_amount)
	print("Fifty Dollar Bill: " + str(fifty_amount))
else:
	fifty_amount = 0
change_less_fifty = change - (50 * fifty_amount)
change_less_fifty = '%.2f'%change_less_fifty
change_less_fifty = float(change_less_fifty)

# Twenty Dollar Bills
twenty_amount = change_less_fifty/20
if twenty_amount >= 1:
	twenty_amount = int(twenty_amount)
	print("Twenty Dollar Bill: " + str(twenty_amount))
else:
	twenty_amount = 0
change_less_twenty = change_less_fifty - (20 * twenty_amount)
change_less_twenty = '%.2f'%change_less_twenty
change_less_twenty = float(change_less_twenty)

# Ten Dollar Bills
ten_amount = change_less_twenty/10
if ten_amount >= 1:
	ten_amount = int(ten_amount)
	print("Ten Dollar Bill: " + str(ten_amount))
else:
	ten_amount = 0
change_less_ten = change_less_twenty - (10 * ten_amount)
change_less_ten = '%.2f'%change_less_ten
change_less_ten = float(change_less_ten)
    
# Five Dollar Bills
five_amount = change_less_ten/5
if five_amount >= 1:
	five_amount = int(five_amount)
	print("Five Dollar Bill: " + str(five_amount))
else:
	five_amount = 0
change_less_five = change_less_ten - (5 * five_amount)
change_less_five = '%.2f'%change_less_five
change_less_five = float(change_less_five)

# One Dollar Bills
one_amount = change_less_five / 1
if one_amount >= 1:
	one_amount = int(one_amount)
	print("One Dollar Bill: " + str(one_amount))
else:
	one_amount = 0
change_less_one = change_less_five - (1 * one_amount)
change_less_one = '%.2f'%change_less_one
change_less_one = float(change_less_one)

# Quarters
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

# Dimes
dime_amount = change_less_q / 0.1
if dime_amount >= 1:
    dime_amount = int(dime_amount)
    print("Dime: " + str(dime_amount))
else:
    dime_amount = 0
change_less_d = change_less_q - (0.1 * dime_amount)
change_less_d = '%.2f'%change_less_d
change_less_d = float(change_less_d)

# Nickels
nickel_amount = change_less_d / 0.05
if nickel_amount >= 1:
    nickel_amount = int(nickel_amount)
    print("Nickel: " + str(nickel_amount))
else:
    nickel_amount = 0
change_less_n = change_less_d - (0.05 * nickel_amount)
change_less_n = '%.2f'%change_less_n
change_less_n = float(change_less_n)

# Pennies
penny_amount = change_less_n / 0.01
if penny_amount >= 1:
	penny_amount = int(penny_amount)
	print("Penny: " + str(penny_amount))
else:
	penny_amount = 0
change_less_p = change_less_n - (0.01 * penny_amount)

check = input("Run check? ")
value50 = fifty_amount * 50
value20 = twenty_amount * 20
value10 = ten_amount * 10
value5 = five_amount * 5
value1 = one_amount * 1
valueQ = quarter_amount * 0.25
valueD = dime_amount * 0.1
valueN = nickel_amount * 0.05
valueP = penny_amount * 0.01
values = [value50, value20, value10, value5, value1, valueQ, valueD, valueN, valueP]
if check == "yes":
    print(sum(values))
    if sum(values) == change:
        print("Congruent")
