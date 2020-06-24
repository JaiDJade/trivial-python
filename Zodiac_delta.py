monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
zodiaclist = ['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn']

month = input("Month of birth: ")
mval = month[0:3]
mval = mval.lower()

cnt = 0
fcnt = 0
while fcnt < 12:
	status = 0
	# print(monthlist[cnt])
	cntval = monthlist[cnt]
	cntval = cntval.lower()
	if cntval[0:3] == mval:
		status = 1
		fcnt = 12
	else:
		fcnt += 1
		cnt = fcnt

if status == 0:
	print("/error")
	exit()
	
date = input("Date of birth: ")

if int(date) > 31 or int(date) == 0:
	print("//error")
	exit()
elif cnt == 1 and int(date) > 29:
	print("//error.f")
	exit()
elif cnt == 3 and int(date) > 30 or cnt == 5 and int(date) > 30 or cnt == 8 and int(date) > 30 or cnt == 10 and int(date) > 30:
	print("//error.30")
	exit()
	
if cnt == 0:
	m = 0
elif cnt == 1:
	m = 31
elif cnt == 2:
	m = 59
elif cnt == 3:
	m = 90
elif cnt == 4:
	m = 120
elif cnt == 5:
	m = 151
elif cnt == 6:
	m = 181
elif cnt == 7:
	m = 212
elif cnt == 8:
	m = 243
elif cnt == 9:
	m = 273
elif cnt == 10:
	m = 304
elif cnt == 11:
	m = 334
	
zodiac = m + int(date)
if zodiac < 1 or zodiac > 365:
	print("//error.z")

if 20 <= zodiac <= 49:
	print(zodiaclist[0])
elif 50 <= zodiac <= 79:
	print(zodiaclist[1])
elif 80 <= zodiac <= 109:
	print(zodiaclist[2])
elif 110 <= zodiac <= 140:
	print(zodiaclist[3])
elif 141 <= zodiac <= 171:
	print(zodiaclist[4])
elif 172 <= zodiac <= 203:
	print(zodiaclist[5])
elif 204 <= zodiac <= 234:
	print(zodiaclist[6])
elif 235 <= zodiac <= 265:
	print(zodiaclist[7])
elif 266 <= zodiac <= 295:
	print(zodiaclist[8])
elif 296 <= zodiac <= 325:
	print(zodiaclist[9])
elif 326 <= zodiac <= 355:
	print(zodiaclist[10])
elif 356 <= zodiac <= 365 or zodiac <= 19:
	print(zodiaclist[11])
								
# print(zodiac)
# print(monthlist[cnt])
# print(cnt + 1)

