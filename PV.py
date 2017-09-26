#!/usr/bin/python3
q = input ("Что считать будем? PV, FV, PMT:")
#PV
if q=="PV":
	z = input ("Через что ищем? PMT, FV:")
	if z=="PMT":
		d = input ("PMT месяц/год? :")
#PV через PMT в год
		if d=="год":
			PMT = int(input ("PMT в год:"))
			r = int(input ("r:"))
			n = int(input ("n(лет):"))
			PV = PMT * (1 - ((1+r/100) ** -n)) / (r/100)
			print("Дано:", "\n" "PMT =", PMT, "\n" "r =", r, "\n" "n =", n, "\n" "PV = PMT * (1 - ((1+r/100) ^ -n)) / (r/100) =", PV)
#PV через PMT в месяц на конец месяца
		if d=="месяц":
			p = input ("начало/конец месяца :")
			if p=="конец":
				PMT = int(input ("PMT в месяц:"))
				r = int(input ("r:"))
				n = int(input ("n(мес):"))
				PV = PMT * (1 - ((1+(r/12)/100) ** -n)) / ((r/12)/100)
				print("Дано:", "\n" "PMT =", PMT, "\n" "r =", r, "\n" "n =", n, "\n" "PV = PMT * (1 - ((1+(r/12)/100) ^ -n)) / ((r/12)/100) = ", PV)
#PV через PMT в месяц на начало месяца
			if p=="начало":
				PMT = int(input ("PMT в месяц:"))
				r = int(input ("r:"))
				n = int(input ("n(мес):"))
				PV = PMT * (1 - ((1+(r/12)/100) ** (-n-1))) / ((r/12)/100) + PMT
				print("Дано:", "\n" "PMT =", PMT, "\n" "r =", r, "\n" "n =", n, "\n" "PV = PMT * (1 - ((1+(r/12)/100) ^ (-n-1))) / ((r/12)/100) + PMT= ", PV)
#PV через FV
	if z=="FV":
		FV = int(input ("FV:"))
		r = int(input ("r:"))
		n = int(input ("n(лет):"))
		PV = FV / (1 + (r/100)) ** n
		print("Дано:", "\n" "FV =", FV, "\n" "r =", r, "\n" "n =", n, "\n" "PV = FV / (1 + (r/100)) ^ n =", PV)

#FV
elif q=="FV":
	z = input ("Через что ищем? PV, PMT:")
	if z=="PMT":
		d = input ("PMT месяц/год? :")
#FV через PMT в год
		if d=="год":
			PMT = int(input ("PMT в год:"))
			r = int(input ("r:"))
			n = int(input ("n(лет):"))
			FV = PMT * ( ((1+r/100) ** n) - 1) / (r/100)
			print("Дано:", "\n" "PMT =", PMT, "\n" "r =", r, "\n" "n =", n, "\n" "FV = PMT * ( ((1+r/100) ^ n) - 1) / (r/100) = ", FV)
#FV через PMT в месяц на конец месяца
		if d=="месяц":
			p = input ("начало/конец месяца :")
			if p=="конец":
				PMT = int(input ("PMT в месяц:"))
				r = int(input ("r:"))
				n = int(input ("n(мес):"))
				FV = PMT * ( ((1+(r/12)/100) ** n) - 1) / ((r/12)/100)
				print("Дано:", "\n" "PMT =", PMT, "\n" "r =", r, "\n" "n =", n, "\n" "FV = PMT * ( ((1+(r/12)/100) ^ n) - 1) / ((r/12)/100) = ", FV)
#FV через PMT в месяц на начало месяца
			if p=="начало":
				PMT = int(input ("PMT в месяц:"))
				r = int(input ("r:"))
				n = int(input ("n(мес):"))
				FV = PMT * (((1+(r/12)/100) ** (n+1)) - 1) / ((r/12)/100) - PMT
				print("Дано:", "\n" "PMT =", PMT, "\n" "r =", r, "\n" "n =", n, "\n" "FV = PMT * (((1+(r/12)/100) ^ (n+1)) - 1) / ((r/12)/100) - PMT =  ", FV)
#FV через PV
	if z=="PV":
		p = input("начисление % мес/год?")
		if p=="год":
			PV = int(input ("PV:"))
			r = int(input ("r:"))
			n = int(input ("n(лет):"))
			FV = PV * (1 + (r/100)) ** n
			print("Дано:", "\n" "PV =", PV, "\n" "r =", r, "\n" "n =", n, "\n" "FV = PV * (1 + (r/100)) ^ n =", FV)
		if p=="мес":
			PV = int(input ("PV:"))
			r = int(input ("r:"))
			n = int(input ("n(мес):"))
			FV = PV * (1 + (r/12/100)) ** n
			print("Дано:", "\n" "PV =", PV, "\n" "r =", r, "\n" "n =", n, "\n" "FV = PV * (1 + (r/12/100)) ^ n =", FV)

#PMT % в год
elif q=="PMT":
	d = input ("PMT % месяц/год? :")
	if d=="год":
		z = input ("Через что ищем? PV, FV:")
		if z=="FV":
			FV = int(input ("FV:"))
			r = int(input ("r:"))
			n = int(input ("n(лет):"))
			PMT = FV / ( ((1+r/100) ** n) - 1) * (r/100)
			print("Дано:", "\n" "FV =", FV, "\n" "r =", r, "\n" "n =", n, "\n" "PMT = FV / ( ((1+r/100) ^ n) - 1) * (r/100)=", PMT)
		if z=="PV":
			PV = int(input ("PV:"))
			r = int(input ("r:"))
			n = int(input ("n(лет):"))
			PMT = PV / (1 - ((1+r/100) ** -n)) * (r/100)
			print("Дано:", "\n" "PV =", PV, "\n" "r =", r, "\n" "n =", n, "\n" "PMT = PV / (1 - ((1+r/100) ^ -n)) * (r/100) = ", PMT)

#PMT % в месяц
	if d=="месяц":
		z = input ("Через что ищем? PV, FV:")
		if z=="FV":
			FV = int(input ("FV:"))
			r = int(input ("r:"))
			n = int(input ("n(лет):"))
			PMT = FV / ( ((1+(r/12)/100) ** (n*12)) - 1) * ((r/12)/100)
			print("Дано:", "\n" "FV =", FV, "\n" "r =", r, "\n" "n =", n, "\n" "PMT = FV / ( ((1+(r/12)/100) ^ (n*12)) - 1) * ((r/12)/100) = ", PMT)
		if z=="PV":
			PV = int(input ("PV:"))
			r = int(input ("r:"))
			n = int(input ("n(лет):"))
			PMT = PV / (1 - ((1+(r/12)/100) ** (-n*12))) * ((r/12)/100)
			print("Дано:", "\n" "PV =", PV, "\n" "r =", r, "\n" "n =", n, "\n" "PMT = PV / (1 - ((1+(r/12)/100) ^ (-n*12))) * ((r/12)/100) =", PMT)
else:
	print ("Я ограничен в ответах. Задавайте правильные вопросы")
