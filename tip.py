price = input("Bill: ")
tipA = float(price) * 0.3
totalA = float(price) + float(tipA)
totalB = int(totalA)

cnt = 0
while cnt < 1:
    tipB = totalB - float(price)
    tipB1 = '%.2f'%tipB
    percentage = float(tipB1) / float(price)
    status = 1
    if percentage > 0.25:
        status = 0
        cnt = 1
    else:
        totalB = totalB + 1

if status == 1:
    print("//error | in while loop")
    exit()

percentage0 = (totalA - float(price)) / float(price)
if percentage0 < 0.25:
    print("Initial: Fail | " + ('%.2f'%percentage0))

print("	Tip: " + str('%.2f'%tipB))
print("		Percent: " + str('%.2f'%percentage))
print("Total: " + str(totalB))
