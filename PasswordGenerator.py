import random
import subprocess
import string

mylist = []
cnt = 0
while cnt < 19:
	x = random.choice(string.ascii_letters)
	y = random.randint(0,9)
	z = random.randint(0,1)
	if z == 0:
		a = x
		cnt += 1
	else:
		a = y
		cnt += 1
	mylist.append(a)

password = str("".join(str(e) for e in mylist[0:6])) + "-" + str("".join(str(e) for e in mylist[6:12])) + "-" + str("".join(str(e) for e in mylist[12:18]))
print(password)

# subprocess.run("pbcopy", universal_newlines = True, input = password)