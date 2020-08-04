"""
Programmer : R.Lokesh

Project : Standard Calculator

Language : Python

Module : Tkinter 

"""
# -----------------------------------------------------Importing the necessary module -----------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

# Creating Main window
root = Tk()
# Adding Title to our Window
root.title("Calculator")
root.geometry("280x400")

# Setting up the icon of our window
root.iconbitmap("Calculator.ico")

#----------------------------------------------------------- Defining the functions or commands----------------------------------------------------------------------------------
def enter(number):
	current_number = Entry_box.get()
	Entry_box.delete(0,END)
	Entry_box.insert(0,str(current_number)+str(number))
def clear():
	Entry_box.delete(0,END)
def dot():
	Entry_box.insert(0,".")
def Add():
	first_number = Entry_box.get()
	global f_num
	f_num = first_number
	Entry_box.delete(0,END)
	global math
	math = "add"
def Subtract():
	first_number = Entry_box.get()
	global f_num
	f_num = first_number
	Entry_box.delete(0,END)
	global math
	math = "sub"
def Multiply():
	first_number = Entry_box.get()
	global f_num
	f_num = first_number
	Entry_box.delete(0,END)
	global math
	math = "mul"
def Divide():
	first_number = Entry_box.get()
	global f_num
	f_num = first_number
	Entry_box.delete(0,END)
	global math
	math = "div"
def square():
	first_number = Entry_box.get()
	global f_num
	f_num = first_number
	global math
	math = "square"
def percent():
	first_number = Entry_box.get()
	global f_num
	f_num = first_number
	global math
	math = "percent"

def equal():
	second_number = Entry_box.get()
	Entry_box.delete(0,END)
	if math == "add":
		sum =  float(f_num)+float(second_number)
		Entry_box.insert(0,sum)
	elif math == "sub":
		subt = float(f_num)-float(second_number)
		Entry_box.insert(0,subt)
	elif math == "mul":
		mul = float(f_num)*float(second_number)
		Entry_box.insert(0,mul)
	elif math == "div":
		divi = float(f_num)/float(second_number)
		Entry_box.insert(0,divi)
	elif math == "square":
		sqr = float(f_num)*float(f_num)
		Entry_box.insert(0,sqr)
	elif math == "percent":
		per = float(f_num)/100
		Entry_box.insert(0,per)
	else:
		Entry_box.insert(0,"Invalid")
# ---------------------------------------------------------------------------- Widgets ----------------------------------------------------------------------------------------------------
Entry_box = Entry(root,width=25,font=('arial',14,'bold'),bg="skyblue",fg="white",borderwidth=1)
Entry_box.grid(row=0,column=0,columnspan=4,ipady=4,pady=10)

button_7 = Button(root,width=6,height=3,text='7',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(7))
button_7.grid(row=1,column=0,padx=0)

button_8 = Button(root,width=6,height=3,text='8',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(8))
button_8.grid(row=1,column=1,padx=0)

button_9 = Button(root,width=6,height=3,text='9',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(9))
button_9.grid(row=1,column=2,padx=0)

button_multiply = Button(root,width=6,height=3,text='x',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=Multiply)
button_multiply.grid(row=1,column=3,padx=0)

button_4 = Button(root,width=6,height=3,text='4',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(4))
button_4.grid(row=2,column=0,padx=0)

button_5 = Button(root,width=6,height=3,text='5',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(5))
button_5.grid(row=2,column=1,padx=0)

button_6 = Button(root,width=6,height=3,text='6',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(6))
button_6.grid(row=2,column=2,padx=0)

button_subtract = Button(root,width=6,height=3,text='-',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=Subtract)
button_subtract.grid(row=2,column=3,padx=0)

button_1 = Button(root,width=6,height=3,text='1',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(1))
button_1.grid(row=3,column=0,padx=0)

button_2 = Button(root,width=6,height=3,text='2',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(2))
button_2.grid(row=3,column=1,padx=0)

button_3 = Button(root,width=6,height=3,text='3',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(3))
button_3.grid(row=3,column=2,padx=0)

button_add = Button(root,width=6,height=3,text='+',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=Add)
button_add.grid(row=3,column=3,padx=0)

button_C = Button(root,width=6,height=3,text='C',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=clear)
button_C.grid(row=4,column=0,padx=0)

button_0 = Button(root,width=6,height=3,text='0',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=lambda:enter(0))
button_0.grid(row=4,column=1,padx=0)

button_dot = Button(root,width=6,height=3,text='.',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=dot)
button_dot.grid(row=4,column=2,padx=0)

button_equal = Button(root,width=6,height=3,text='=',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=equal)
button_equal.grid(row=5,column=3,padx=0)

button_square = Button(root,width=6,height=3,text='x2',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=square)
button_square.grid(row=5,column=0,padx=0)

button_one_divide = Button(root,width=6,height=3,text='1/x',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white")
button_one_divide.grid(row=5,column=1,padx=0)

button_percent = Button(root,width=6,height=3,text='%',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=percent)
button_percent.grid(row=5,column=2,padx=0)

button_divide = Button(root,width=6,height=3,text='/',font=('arial',12,'bold'),bg="skyblue",fg="white",borderwidth=1,activebackground="skyblue",activeforeground="white",command=Divide)
button_divide.grid(row=4,column=3,padx=0)

# Creating our loop()

root.mainloop()

# -------------------------------------------------------------------------------------------------  END -----------------------------------------------------------------------------------