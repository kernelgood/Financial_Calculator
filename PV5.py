#!/usr/bin/python3

from tkinter import *
import pylab
root = Tk()
#Кнопки
class Buttons:
	def __init__(self, display):
		but = Button(root,text="Выбрать")
		but.bind('<Button-1>', display) 
		but.grid()
	def __init__(self, display1):
		but = Button(root,text="Выбрать")
		but.bind('<Button-1>', display1) 
		but.grid()
	def __init__(self, display2):
		but = Button(root,text="Посчитать")
		but.bind('<Button-1>', display2) 
		but.grid()
	def __init__(self, display3):
		but = Button(root,text="Выбрать")
		but.bind('<Button-1>', display3) 
		but.grid()
#Текст для 1-го окна
tx = Text(font=('times',12),width=20,height=1,wrap=WORD)
tx.insert(1.0,"Что считать будем?")
tx.grid() 
#Выбор для 1-го окна
var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="PV",variable=var,value=0)
rad1 = Radiobutton(root,text="FV",variable=var,value=1)
rad2 = Radiobutton(root,text="PMT",variable=var,value=2)
rad0.grid()
rad1.grid()
rad2.grid()
#События при выборе 1	
def display(event):
	global var
	v0 = var.get()
#PV
	if v0 == 0:
		tx = Text(font=('times',12),width=25,height=1,wrap=WORD)
		tx.insert(1.0,"Через что искать будем?")
		tx.grid() 
		var=IntVar()
		var.set(1)
		rad3 = Radiobutton(root,text="FV",variable=var,value=0)
		rad4 = Radiobutton(root,text="PMT",variable=var,value=1)
		rad3.grid()
		rad4.grid()
#Событие для выбора 2
		def display1(event):
			global var
			v1 = var.get()
#PV через PMT
			if v1 == 1:
				tx = Text(font=('times',12),width=35,height=1,wrap=WORD)
				tx.insert(1.0,"PMT на начало/конец месяца или в год?")
				tx.grid() 
				var=IntVar()
				var.set(1)
				rad3 = Radiobutton(root,text="в год",variable=var,value=0)
				rad4 = Radiobutton(root,text="на начало месяца",variable=var,value=1)
				rad5 = Radiobutton(root,text="на конец месяца",variable=var,value=2)
				rad3.grid()
				rad4.grid()
				rad5.grid()
#Событие для выбора 3
				def display3(event):
					global var
					v2 = var.get()
#PV через PMT в год
					if v2 == 0:
#Подпись параметров ввода
						ent0_label = Label(text="PMT=")
						ent1_label = Label(text="n(лет)=")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 320)
						ent1_label.place(x = 20, y = 340)	
						ent2_label.place(x = 40, y = 360)			
#Расчет

						def display2(event):
							PMT = dent0.get()
							n = dent1.get()
							r = dent2.get()
							PV = PMT * (1 - ((1+r/100) ** -n)) / (r/100)

#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (2,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$PV = PMT * \frac{1-(1+r)^{-n}}{r}$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$PV = %s * \frac{1-(1+%s)^{-%s}}{%s}$" %(PMT, r/100, n, r/100)
							ax.text(0,0.3, text_formula,fontsize=14)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()
#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, PV)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)	

#PV через PMT в месяц (на начало месяца)

					elif v2 == 1:

#Подпись
						ent0_label = Label(text="PMT=")
						ent1_label = Label(text="n(мес)=")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)
						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 320)
						ent1_label.place(x = 20, y = 340)	
						ent2_label.place(x = 40, y = 360)			
#Расчет

						def display2(event):
							PMT = dent0.get()
							n = dent1.get()
							r = dent2.get()
							PV = PMT * (1 - ((1+(r/12)/100) ** (-n-1))) / ((r/12)/100) + PMT

							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (3,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$PV = PMT * \frac{1-(1+ \frac{r}{12})^{-n-1}}{\frac{r}{12}} +PMT$",fontsize=14)
#Подставляет данные в формулу на изображении
							text_formula = r"$PV = %s * \frac{1-(1+ \frac{%s}{12})^{-%s-1}}{\frac{%s}{12}} + %s$" %(PMT, r/100, n, r/100, PMT)
							ax.text(0,0.3, text_formula,fontsize=14)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()

#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, PV)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)

#PV через PMT в месяц (на конец месяца)

					elif v2 == 2:

#Подпись
						ent0_label = Label(text="PMT=")
						ent1_label = Label(text="n(мес)=")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 320)
						ent1_label.place(x = 20, y = 340)	
						ent2_label.place(x = 40, y = 360)			
#Расчет

						def display2(event):
							PMT = dent0.get()
							n = dent1.get()
							r = dent2.get()
							PV = PMT * (1 - ((1+(r/12)/100) ** -n)) / ((r/12)/100)
							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (3,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$PV = PMT * \frac{1-(1+ \frac{r}{12})^{-n}}{\frac{r}{12}}$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$PV = %s * \frac{1-(1+ \frac{%s}{12})^{-%s}}{\frac{%s}{12}}$" %(PMT, r/100, n, r/100)
							ax.text(0,0.3, text_formula,fontsize=15)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()
#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, PV)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)

#PV через FV
			if v1 == 0:
#Поля ввода
#Подпись
				ent0_label = Label(text="FV=")
				ent1_label = Label(text="n(лет)=")
				ent2_label = Label(text="r =")
#Тип вводимых данных
				dent0 = IntVar()
				dent1 = IntVar()
				dent2 = IntVar()
#Непосредственно ввод
				ent0 = Entry(textvariable=dent0, width=10)
				ent1 = Entry(textvariable=dent1,width=10)
				ent2 = Entry(textvariable=dent2,width=10)
				ent0.grid()
				ent1.grid()
				ent2.grid()
#Координаты подписи
				ent0_label.place(x = 40, y = 210)
				ent1_label.place(x = 20, y = 230)	
				ent2_label.place(x = 40, y = 250)			
#Расчет

				def display2(event):
					FV = dent0.get()
					n = dent1.get()
					r = dent2.get()
					PV = FV / (1 + (r/100)) ** n
					#Вывод изображения	
#Рисует формулу						
					fig = pylab.figure(figsize= (2,2))
					ax = pylab.axes([0,0,1,1])
					ax.text(0,0.5,r"$PV = \frac{FV}{(1+r)^{n}}$",fontsize=15)
#Подставляет данные в формулу на изображении
					text_formula = r"$PV = \frac{%s}{(1+%s)^{%s}}$" %(FV, r/100, n)
					ax.text(0,0.3, text_formula,fontsize=14)
					pylab.savefig("aa.png")
#Выводим на экран
					im = PhotoImage(file='aa.png')
					l = Label(root, image=im)
					l.grid()

#Событие для кнопки "Посчитать!"
					tex = Text(root,width=20,height=3,font="12",wrap=WORD)
					tex.insert(END, PV)
					tex.grid()
#Кнопка для расчета
				Buttons(display2)
	#Кнопка
			Buttons(display3)
		#Кнопка
		Buttons(display1)
#FV
	elif v0 == 1:
		tx = Text(font=('times',12),width=25,height=1,wrap=WORD)
		tx.insert(1.0,"Через что искать будем?")
		tx.grid() 
		var=IntVar()
		var.set(1)
		rad3 = Radiobutton(root,text="PV",variable=var,value=0)
		rad4 = Radiobutton(root,text="PMT",variable=var,value=1)
		rad3.grid()
		rad4.grid()
#Событие для выбора 2
		def display1(event):
			global var
			v1 = var.get()
#FV через PMT
			if v1 == 1:

				tx = Text(font=('times',12),width=35,height=1,wrap=WORD)
				tx.insert(1.0,"PMT на начало/конец месяца или в год?")
				tx.grid() 
				var=IntVar()
				var.set(1)
				rad3 = Radiobutton(root,text="в год",variable=var,value=0)
				rad4 = Radiobutton(root,text="на начало месяца",variable=var,value=1)
				rad5 = Radiobutton(root,text="на конец месяца",variable=var,value=2)
				rad3.grid()
				rad4.grid()
				rad5.grid()
#Событие для выбора 3
				def display3(event):
					global var
					v2 = var.get()
#FV через PMT в год
					if v2 == 0:
#Подпись
						ent0_label = Label(text="PMT=")
						ent1_label = Label(text="n(лет)=")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 320)
						ent1_label.place(x = 20, y = 340)	
						ent2_label.place(x = 40, y = 360)			
#Расчет

						def display2(event):
							PMT = dent0.get()
							n = dent1.get()
							r = dent2.get()
							FV = PMT * ( ((1+r/100) ** n) - 1) / (r/100)
							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (2,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$FV = PMT * \frac{(1+r)^{n}-1}{r}$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$FV = %s * \frac{(1+%s)^{%s}-1}{%s}$" %(PMT, r/100, n, r/100)
							ax.text(0,0.3, text_formula,fontsize=14)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()
#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, FV)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)
			
#FV через PMT в месяц (на начало месяца)

					elif v2 == 1:

#Подпись
						ent0_label = Label(text="PMT=")
						ent1_label = Label(text="n(мес)=")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 320)
						ent1_label.place(x = 20, y = 340)	
						ent2_label.place(x = 40, y = 360)			
#Расчет

						def display2(event):
							PMT = dent0.get()
							n = dent1.get()
							r = dent2.get()
							FV = PMT * (((1+(r/12)/100) ** (n+1)) - 1) / ((r/12)/100) - PMT
							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (3,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$FV = PMT * \frac{(1+ \frac{r}{12})^{n+1})-1}{\frac{r}{12}} - PMT$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$FV = %s * \frac{(1+ \frac{%s}{12})^{%s+1})-1}{\frac{%s}{12}} - %s$" %(PMT, r/100, n, r/100, PMT)
							ax.text(0,0.3, text_formula,fontsize=15)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()
#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, FV)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)
#PV через PMT в месяц (на конец месяца)
					elif v2 == 2:

#Подпись
						ent0_label = Label(text="PMT=")
						ent1_label = Label(text="n(мес)=")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 320)
						ent1_label.place(x = 20, y = 340)	
						ent2_label.place(x = 40, y = 360)			
#Расчет

						def display2(event):
							PMT = dent0.get()
							n = dent1.get()
							r = dent2.get()
							FV = PMT * ( ((1+(r/12)/100) ** n) - 1) / ((r/12)/100)
							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (3,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$FV = PMT * \frac{(1+ \frac{r}{12})^{n})-1}{\frac{r}{12}}$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$FV = %s * \frac{(1+ \frac{%s}{12})^{%s})-1}{\frac{%s}{12}}$" %(PMT, r/100, n, r/100)
							ax.text(0,0.3, text_formula,fontsize=15)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()
#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, FV)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)
#FV через PV
			if v1 == 0:
#Поля ввода

#Подпись
				ent0_label = Label(text="PV=")
				ent1_label = Label(text="n(лет)=")
				ent2_label = Label(text="r =")
#Тип вводимых данных
				dent0 = IntVar()
				dent1 = IntVar()
				dent2 = IntVar()
#Непосредственно ввод
				ent0 = Entry(textvariable=dent0, width=10)
				ent1 = Entry(textvariable=dent1,width=10)
				ent2 = Entry(textvariable=dent2,width=10)

				ent0.grid()
				ent1.grid()
				ent2.grid()
#Координаты подписи
				ent0_label.place(x = 40, y = 210)
				ent1_label.place(x = 20, y = 230)	
				ent2_label.place(x = 40, y = 250)			
#Расчет
				def display2(event):
					PV = dent0.get()
					n = dent1.get()
					r = dent2.get()
					FV = PV * (1 + (r/100)) ** n
					#Вывод изображения	
#Рисует формулу						
					fig = pylab.figure(figsize= (2,2))
					ax = pylab.axes([0,0,1,1])
					ax.text(0,0.5,r"$FV = PV *(1+r)^{n}$",fontsize=15)
#Подставляет данные в формулу на изображении
					text_formula = r"$FV = %s *(1+%s)^{%s}$" %(PV, r/100, n)
					ax.text(0,0.3, text_formula,fontsize=14)
					pylab.savefig("aa.png")
#Выводим на экран
					im = PhotoImage(file='aa.png')
					l = Label(root, image=im)
					l.grid()		
#Событие для кнопки "Посчитать!"
					tex = Text(root,width=20,height=3,font="12",wrap=WORD)
					tex.insert(END, FV)
					tex.grid()
#Кнопка для расчета
				Buttons(display2)
	#Кнопка
			Buttons(display3)
		#Кнопка
		Buttons(display1)

#PMT
	elif v0 == 2:
		tx = Text(font=('times',12),width=25,height=1,wrap=WORD)
		tx.insert(1.0,"Начисление % в месяц или в год?")
		tx.grid() 
		var=IntVar()
		var.set(1)
		rad3 = Radiobutton(root,text="в месяц",variable=var,value=0)
		rad4 = Radiobutton(root,text="в год",variable=var,value=1)
		rad3.grid()
		rad4.grid()
#Событие для выбора 2
		def display1(event):
			global var
			v1 = var.get()
#PMT % в год
			if v1 == 1:

				tx = Text(font=('times',12),width=35,height=1,wrap=WORD)
				tx.insert(1.0,"Через что искать будем?")
				tx.grid() 
				var=IntVar()
				var.set(1)
				rad4 = Radiobutton(root,text="PV",variable=var,value=0)
				rad5 = Radiobutton(root,text="FV",variable=var,value=1)
				rad3.grid()
				rad4.grid()
				rad5.grid()

#Событие для выбора 3
				def display3(event):
					global var
					v2 = var.get()
#PMT через PV в год
					if v2 == 0:

#Подпись
						ent0_label = Label(text="PV=")
						ent1_label = Label(text="n(лет)=")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 300)
						ent1_label.place(x = 20, y = 320)	
						ent2_label.place(x = 40, y = 340)			
#Расчет
						def display2(event):
							PV = dent0.get()
							n = dent1.get()
							r = dent2.get()
							PMT = PV / (1 - ((1+r/100) ** -n)) * (r/100)
							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (3,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$PMT = \frac{PV}{1-(1+r)^{-n}}*r$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$PMT = \frac{%s}{1-(1+%s)^{-%s}}*%s$" %(PV, r/100, n, r/100)
							ax.text(0,0.3, text_formula,fontsize=14)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()

#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, PMT)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)
#PMT через FV в год
					elif v2 == 1:

#Подпись
						ent0_label = Label(text="FV=")
						ent1_label = Label(text="n(лет) =")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 300)
						ent1_label.place(x = 20, y = 320)	
						ent2_label.place(x = 40, y = 340)			
#Расчет

						def display2(event):
							FV = dent0.get()
							n = dent1.get()
							r = dent2.get()
							PMT = FV / ( ((1+r/100) ** n) - 1) * (r/100)
							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (3,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$PMT = \frac{FV}{(1+r)^{n}-1}*r$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$PMT = \frac{%s}{(1+%s)^{%s}-1}*%s$" %(FV, r/100, n, r/100)
							ax.text(0,0.3, text_formula,fontsize=14)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()

#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, PMT)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)
#PMT % в месяц
			elif v1 == 0:

				tx = Text(font=('times',12),width=35,height=1,wrap=WORD)
				tx.insert(1.0,"Через что искать будем?")
				tx.grid() 
				var=IntVar()
				var.set(1)
				rad4 = Radiobutton(root,text="PV",variable=var,value=0)
				rad5 = Radiobutton(root,text="FV",variable=var,value=1)
				rad3.grid()
				rad4.grid()
				rad5.grid()
#Событие для выбора 3
				def display3(event):
					global var
					v2 = var.get()

#PMT через PV в год
					if v2 == 0:

#Подпись
						ent0_label = Label(text="PV=")
						ent1_label = Label(text="n(лет)=")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 300)
						ent1_label.place(x = 20, y = 320)	
						ent2_label.place(x = 40, y = 340)			
#Расчет

						def display2(event):
							PV = dent0.get()
							n = dent1.get()
							r = dent2.get()
							PMT = PV / (1 - ((1+(r/12)/100) ** (-n*12))) * ((r/12)/100)
							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (3,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$PMT = \frac{PV}{1-(1+\frac{r}{12})^{-n*12}} *\frac{r}{12}}$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$PMT = \frac{%s}{1-(1+\frac{%s}{12})^{-%s*12}} *\frac{%s}{12}}$" %(PV, r/100, n, r/100)
							ax.text(0,0.3, text_formula,fontsize=14)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()
#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, PMT)
							tex.grid()

#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, PMT)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)
			
#PMT через FV в год

					elif v2 == 1:

#Подпись
						ent0_label = Label(text="FV=")
						ent1_label = Label(text="n(лет) =")
						ent2_label = Label(text="r =")
#Тип вводимых данных
						dent0 = IntVar()
						dent1 = IntVar()
						dent2 = IntVar()
#Непосредственно ввод
						ent0 = Entry(textvariable=dent0, width=10)
						ent1 = Entry(textvariable=dent1,width=10)
						ent2 = Entry(textvariable=dent2,width=10)

						ent0.grid()
						ent1.grid()
						ent2.grid()
#Координаты подписи
						ent0_label.place(x = 30, y = 300)
						ent1_label.place(x = 20, y = 320)	
						ent2_label.place(x = 40, y = 340)			
#Расчет

						def display2(event):
							FV = dent0.get()
							n = dent1.get()
							r = dent2.get()
							PMT = FV / ( ((1+(r/12)/100) ** (n*12)) - 1) * ((r/12)/100)
							#Вывод изображения	
#Рисует формулу						
							fig = pylab.figure(figsize= (3,2))
							ax = pylab.axes([0,0,1,1])
							ax.text(0,0.5,r"$PMT = \frac{FV}{(1+\frac{r}{12})^{n*12}-1} *\frac{r}{12}}$",fontsize=15)
#Подставляет данные в формулу на изображении
							text_formula = r"$PMT = \frac{%s}{(1+\frac{%s}{12})^{%s*12}-1} *\frac{%s}{12}}$" %(FV, r/100, n, r/100)
							ax.text(0,0.3, text_formula,fontsize=14)
							pylab.savefig("aa.png")
#Выводим на экран
							im = PhotoImage(file='aa.png')
							l = Label(root, image=im)
							l.grid()
#Событие для кнопки "Посчитать!"
							tex = Text(root,width=20,height=3,font="12",wrap=WORD)
							tex.insert(END, PMT)
							tex.grid()
#Кнопка для расчета
						Buttons(display2)
	#Кнопка
			Buttons(display3)
		#Кнопка
		Buttons(display1) 
#Кнопка
Buttons(display)
root.mainloop()