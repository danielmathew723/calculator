from tkinter import *

# creates a window
root = Tk()
# titles window
root.title("Calculator")
# allows for user input
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# retrieves info when a button is clicked and prints it in the entry box
def click(number):
    temp = e.get()
    e.delete(0, END)
    e.insert(0, temp + number)


# clears entry box
def clear():
    e.delete(0, END)


# deletes last digit
def delete():
    length = len(e.get())
    e.delete(length - 1)


# adds two numbers
def add():
    first = e.get()
    global f
    global math
    math = 'addition'
    f = int(first)
    e.delete(0, END)


# subtracts two numbers
def subtract():
    first = e.get()
    global f
    global math
    math = 'subtraction'
    f = int(first)
    e.delete(0, END)


# multiplies two numbers
def multiply():
    first = e.get()
    global f
    global math
    math = 'multiplication'
    f = int(first)
    e.delete(0, END)


# divides two numbers
def divide():
    first = e.get()
    global f
    global math
    math = 'division'
    f = int(first)
    e.delete(0, END)


# completes computation
def equal():
    second = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f + int(second))
    elif math == 'subtraction':
        e.insert(0, f - int(second))
    elif math == 'multiplication':
        e.insert(0, f * int(second))
    else:
        e.insert(0, f / int(second))


# creates all the buttons in the calculator
button1 = Button(root, text='1', padx=30, pady=10, command=lambda: click('1'))
button2 = Button(root, text='2', padx=30, pady=10, command=lambda: click('2'))
button3 = Button(root, text='3', padx=30, pady=10, command=lambda: click('3'))
button4 = Button(root, text='4', padx=30, pady=10, command=lambda: click('4'))
button5 = Button(root, text='5', padx=30, pady=10, command=lambda: click('5'))
button6 = Button(root, text='6', padx=30, pady=10, command=lambda: click('6'))
button7 = Button(root, text='7', padx=30, pady=10, command=lambda: click('7'))
button8 = Button(root, text='8', padx=30, pady=10, command=lambda: click('8'))
button9 = Button(root, text='9', padx=30, pady=10, command=lambda: click('9'))
button0 = Button(root, text='0', padx=30, pady=10, command=lambda: click('0'))

buttonadd = Button(root, text='+', padx=34, pady=10, command=add)
buttonsub = Button(root, text='-', padx=35, pady=10, command=subtract)
buttonmul = Button(root, text='x', padx=35, pady=10, command=multiply)
buttondiv = Button(root, text='/', padx=35, pady=10, command=divide)

buttonequal = Button(root, text='=', padx=70, pady=10, command=equal)
buttonclear = Button(root, text="Clear", padx=24, pady=10, command=clear)
buttondel = Button(root, text='Delete', padx=23, pady=10, command=delete)

# adds buttons to the window
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttondel.grid(row=1, column=4)
buttonadd.grid(row=3, column=3)
buttonsub.grid(row=3, column=4)
buttonmul.grid(row=2, column=3)
buttondiv.grid(row=2, column=4)
buttonclear.grid(row=1, column=3)
buttonequal.grid(row=4, column=1, columnspan=2)

# mainloop, runs infinitely
mainloop()
