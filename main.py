from math import *
from tkinter import *
'''SETTING UP THE WINDOWS OF THR CALCULATOR
'''
root = Tk()
root.title("JASB CALC")
root.geometry("310x510")
my_frame = Frame(root, width = 100, height = 50)
my_frame.pack(side = TOP)
'''SETTING UP THE SCREEN
'''
my_screen = Entry(my_frame, width = 30, borderwidth = 10)
my_screen.grid(row = 0, column = 1, columnspan = 6, padx = 5, pady = 30)


def entry_value(val):
	'''This function allows the user to enter values on the Calculator screen
	'''
    num = my_screen.get()
    my_screen.delete(0, END)
    my_screen.insert(0, num + val )

def delete_value():
	'''This function allows the button 'del' to delete values on the screen backward
	'''
    num = str(my_screen.get())
    my_screen.delete(0, END)
    single_value = num[: -1]
    my_screen.insert(0, single_value)
    
def calc():
	'''This function allows for the calculation of values set on the screen
	'''
	num = str(my_screen.get())
	my_screen.delete(0, END)
	if ("*") in num:
		result = eval(num)
		my_screen.insert(0, result )
	elif ("/") in num:
		result = eval(num)
		my_screen.insert(0, result )
	elif ("**") in num:
		result = eval(num)
		my_screen.insert(0, result )
	elif ("sin(") in num:
		result = sin(float(num[4:]) * pi/180)
		my_screen.insert(0, result)
	elif ("cos(") in num:
		result = cos(float(num[4:]) * pi/180)
		my_screen.insert(0, result)
	elif("tan(") in num:
		result = tan(float(num[4:]) * pi/180)
		my_screen.insert(0, result)
	elif ("log(") in num:
		result = log10(float(num[4:]))
		my_screen.insert(0, result)

def cancel():
	'''This function allowd the button 'cancel' when clicked to delete all values on the screen
	'''
    my_screen.delete(0, END)

'''BUTTON CONFIGURATION, ASSIGNMENT AND POSITIONING
'''

#This assigns values of Buttons on the button widget
button1 = Button(my_frame, text = "1", padx = 20, pady = 10, command = lambda: entry_value("1"))
button2 = Button(my_frame, text = "2", padx = 20, pady = 10, command = lambda: entry_value("2"))
button3 = Button(my_frame, text = "3", padx = 20, pady = 10, command = lambda: entry_value("3"))
button4 = Button(my_frame, text = "4", padx = 20, pady = 10, command = lambda: entry_value("4"))
button5 = Button(my_frame, text = "5", padx = 20, pady = 10, command = lambda: entry_value("5"))
button6 = Button(my_frame, text = "6", padx = 20, pady = 10, command = lambda: entry_value("6"))
button7 = Button(my_frame, text = "7", padx = 20, pady = 10, command = lambda: entry_value("7"))
button8 = Button(my_frame, text = "8", padx = 20, pady = 10, command = lambda: entry_value("8"))
button9 = Button(my_frame, text = "9", padx = 20, pady = 10, command = lambda: entry_value("9"))
button0 = Button(my_frame, text = "0", padx = 20, pady = 10, command = lambda: entry_value("0"))
button_add = Button(my_frame, text = "+", padx = 20, pady = 10, command = lambda: entry_value("+"))
button_sub = Button(my_frame, text = "-", padx = 20, pady = 10, command = lambda: entry_value("-"))
button_div = Button(my_frame, text = "/", padx = 20, pady = 10, command = lambda: entry_value("/"))
button_mul = Button(my_frame, text = "*", padx = 20, pady = 10, command = lambda: entry_value("*"))
button_squal = Button(my_frame, text = "**", padx = 20, pady = 10, command = lambda: entry_value("**"))
button_open = Button(my_frame, text = "(", padx = 20, pady = 10, command = lambda: entry_value("("))
button_close = Button(my_frame, text = ")", padx = 20, pady = 10, command = lambda: entry_value(")"))

button_root = Button(my_frame, text = "√", padx = 20, pady = 10, command = lambda: entry_value("sqrt("))
button_equal = Button(my_frame, text = "=", padx = 20, pady = 10, command = calc)
button_del = Button(my_frame, text = "del", padx = 20, pady = 10, command = delete_value)
button_cancel = Button(my_frame, text = "cancel", width = 30, command = cancel)
button_dot = Button(my_frame, text = ".", padx = 20, pady = 10, command = lambda: entry_value("."))
button_sin = Button(my_frame, text = "sin", padx = 20, pady = 10, command = lambda: entry_value("sin("))
button_cos = Button(my_frame, text = "cos", padx = 20, pady = 10, command = lambda: entry_value("cos("))
button_tan = Button(my_frame, text = "tan", padx = 20, pady = 10, command = lambda: entry_value("tan("))
button_log = Button(my_frame, text = "log", padx = 20, pady = 10, command = lambda: entry_value("log("))

#defining button position on the widget
button0.grid(row = 5, column = 1)
button_dot.grid(row = 5, column = 2)
button_equal.grid(row = 5, column = 3 )
button_squal.grid(row = 5, column = 4)
button_close.grid(row = 5, column = 5)
button_tan.grid(row = 5, column = 6)
button1.grid(row = 4, column = 1)
button2.grid(row = 4, column = 2)
button3.grid(row = 4, column = 3)
button_mul.grid(row = 4, column = 4)
button_open.grid(row = 4, column = 5)
button_cos.grid(row = 4, column = 6)
button4.grid(row = 3, column = 1)
button5.grid(row = 3, column = 2)
button6.grid(row = 3, column = 3)
button_div.grid(row = 3, column = 4)
button_del.grid(row = 3, column = 5)
button_log.grid(row = 3, column = 6)
button7.grid(row = 2, column = 1)
button8.grid(row = 2, column = 2)
button9.grid(row = 2, column = 3)
button_sub.grid(row = 2, column = 4)
button_root.grid(row = 2, column = 5)
button_sin.grid(row = 2, column = 6)
button_cancel.grid(row = 1, columnspan = 7)

my_frame.mainloop()