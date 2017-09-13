from tkinter import *
from tkinter import ttk
import math

def getSum(event):
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    sum = num1 + num2

    answer_entry.delete(0, "end")
    answer_entry.insert(0, sum)

def getSub(event):
    num1 = float(num1_entry2.get())
    num2 = float(num2_entry2.get())
    sub = num1 - num2

    answer_entry2.delete(0, "end")
    answer_entry2.insert(0, sub)

def getMulti(event):
    num1 = float(num1_entry3.get())
    num2 = float(num2_entry3.get())
    multi = num1 * num2

    answer_entry3.delete(0, "end")
    answer_entry3.insert(0, multi)

def getDivide(event):
    num1 = float(num1_entry4.get())
    num2 = float(num2_entry4.get())

    try:
        div = num1 / num2
        answer_entry4.delete(0, "end")
        answer_entry4.insert(0, round(div, 2))

    except ZeroDivisionError:
        answer_entry4.delete(0, "end")
        answer_entry4.insert(0, "DivideByZeroError")

def getSin(event):
    num1 = float(sin_entry.get())
    sin = math.sin(math.radians(num1))
    answer_entry5.delete(0, "end")
    answer_entry5.insert(0, round(sin, 4))

def getCos(event):
    num1 = float(cos_entry.get())
    cos = math.cos(math.radians(num1))

    answer_entry6.delete(0, "end")
    answer_entry6.insert(0, round(cos, 4))

def getTan(event):
    num1 = float(tan_entry.get())
    tan = math.tan(math.radians(num1))

    answer_entry7.delete(0, "end")
    answer_entry7.insert(0, round(tan, 4))

def getArcSin(event):
    num1 = float(arc_sin_entry.get())

    try:
        asin = math.degrees(math.asin(num1))
        answer_entry8.delete(0, "end")
        answer_entry8.insert(0, round(asin))

    except ValueError:
        answer_entry8.delete(0, "end")
        answer_entry8.insert(0, "DOMAIN ERROR")

def getArcCos(event):
    num1 = float(arc_cos_entry.get())

    try:
        acos = math.degrees(math.acos(num1))
        answer_entry9.delete(0, "end")
        answer_entry9.insert(0, round(acos))

    except ValueError:
        answer_entry9.delete(0, "end")
        answer_entry9.insert(0, "DOMAIN ERROR")

def getTax(event):
    price = float(price_entry.get())
    tax = float(tax_entry.get())
    final_price = (tax / 100) * price + price

    answer_entry10.delete(0, "end")
    answer_entry10.insert(0, round(final_price, 2))


def getTip(event):
    price = float(price_entry2.get())
    tip = float(tip_entry.get())
    show_tip = (tip / 100) * price
    final_price = (tip / 100) * price + price

    answer_entry11.delete(0, "end")
    answer_entry11.insert(0, round(final_price, 2))

    display_tip_entry.delete(0, "end")
    display_tip_entry.insert(0, round(show_tip, 2))

def getDiscount(event):
    price = float(price_entry3.get())
    percent = float(percent_entry.get())
    you_save = price * (percent / 100)
    discount_price = price - price * (percent / 100)

    answer_entry12.delete(0, "end")
    answer_entry12.insert(0, round(discount_price, 2))

    you_save_entry.delete(0, "end")
    you_save_entry.insert(0, round(you_save, 2))

def getFah(event):
    cel_value = float(convert_entry.get())
    formula = (cel_value * 9 / 5) + 32

    answer_entry13.delete(0, "end")
    answer_entry13.insert(0, round(formula, 2))

def getCel(event):
    fah_value = float(convert_entry2.get())
    formula = (fah_value - 32) * 5 / 9

    answer_entry14.delete(0, "end")
    answer_entry14.insert(0, round(formula, 2))


root = Tk()
root.title("All-In-One Calculator")
root.geometry("790x380")
root.resizable(width=False, height=False)

style = ttk.Style()
style.configure("TButton", font="Serif 14", padding=1)
style.configure("TLabel", font="Serif 12", padding=1)

quit_button = ttk.Button(root, text="QUIT", command=exit, width=12).grid(row=15, columnspan=10)

# --- Addition Row ---

num1_entry = Entry(root)
num1_entry.grid(row=0, column=0)

addition_label = ttk.Label(root, text="+ ").grid(row=0, column=1)

num2_entry = Entry(root)
num2_entry.grid(row=0, column=2)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getSum)
equal_button.grid(row=0, column=3)

answer_entry = Entry(root)
answer_entry.grid(row=0, column=4)

# --- Subtraction Row ---

num1_entry2 = Entry(root)
num1_entry2.grid(row=1, column=0)

subtract_label = ttk.Label(root, text="- ").grid(row=1, column=1)

num2_entry2 = Entry(root)
num2_entry2.grid(row=1, column=2)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getSub)
equal_button.grid(row=1, column=3)

answer_entry2 = Entry(root)
answer_entry2.grid(row=1, column=4)

# --- Multiplication Row ---

num1_entry3 = Entry(root)
num1_entry3.grid(row=2, column=0)

multiply_label = ttk.Label(root, text="x ").grid(row=2, column=1)

num2_entry3 = Entry(root)
num2_entry3.grid(row=2, column=2)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getMulti)
equal_button.grid(row=2, column=3)

answer_entry3 = Entry(root)
answer_entry3.grid(row=2, column=4)

# --- Division Row ---

num1_entry4 = Entry(root)
num1_entry4.grid(row=3, column=0)

divide_label = ttk.Label(root, text="/ ").grid(row=3, column=1)

num2_entry4 = Entry(root)
num2_entry4.grid(row=3, column=2)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getDivide)
equal_button.grid(row=3, column=3)

answer_entry4 = Entry(root)
answer_entry4.grid(row=3, column=4)

# --- sin() Row ---

sin_label = ttk.Label(root, text="sin").grid(row=0, column=5)
sin_entry = Entry(root)
sin_entry.grid(row=0, column=6)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getSin)
equal_button.grid(row=0, column=7)

answer_entry5 = Entry(root)
answer_entry5.grid(row=0, column=8)

# -- cos() Row ---

cos_label = ttk.Label(root, text="cos").grid(row=1, column=5)
cos_entry = Entry(root)
cos_entry.grid(row=1, column=6)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getCos)
equal_button.grid(row=1, column=7)

answer_entry6 = Entry(root)
answer_entry6.grid(row=1, column=8)

# --- Tan() Row ---

tan_label = ttk.Label(root, text="tan").grid(row=2, column=5)
tan_entry = Entry(root)
tan_entry.grid(row=2, column=6)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getTan)
equal_button.grid(row=2, column=7)

answer_entry7 = Entry(root)
answer_entry7.grid(row=2, column=8)

# --- arcsin() Row ---

arc_sin_label = ttk.Label(root, text="arcsin").grid(row=3, column=5)
arc_sin_entry = Entry(root)
arc_sin_entry.grid(row=3, column=6)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getArcSin)
equal_button.grid(row=3, column=7)

answer_entry8 = Entry(root)
answer_entry8.grid(row=3, column=8)

# --- arccos() Row ---

arc_cos_label = ttk.Label(root, text="arccos").grid(row=4, column=5)
arc_cos_entry = Entry(root)
arc_cos_entry.grid(row=4, column=6)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getArcCos)
equal_button.grid(row=4, column=7)

answer_entry9 = Entry(root)
answer_entry9.grid(row=4, column=8)

# --- Tax calculator ---

tax_cal_label = ttk.Label(root, text="Calculate Tax").grid(row=4, column=0)
price_label = ttk.Label(root, text="Price:").grid(row=5, column=0)
price_entry = Entry(root)
price_entry.grid(row=5, columnspan=4)

tax_label = ttk.Label(root, text="Tax: ").grid(row=6, column=0)
tax_entry = Entry(root)
tax_entry.grid(row=6, columnspan=4)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getTax)
equal_button.grid(row=7, column=0)

answer_entry10 = Entry(root)
answer_entry10.grid(row=7, columnspan=4)

# --- Tip calculator ---

tip_cal_label = ttk.Label(root, text="Calculate Tip", ).grid(row=4, columnspan=6)
price_label2 = ttk.Label(root, text="Price:").grid(row=5, columnspan=5)
price_entry2 = Entry(root)
price_entry2.grid(row=5, columnspan=7)

tip_label = ttk.Label(root, text="Tip:").grid(row=6, columnspan=5)
tip_entry = Entry(root)
tip_entry.grid(row=6, columnspan=7)

display_tip_label = ttk.Label(root, text="Tip is:").grid(row=5, columnspan=9)
display_tip_entry = Entry(root, width=8, fg="BLUE")
display_tip_entry.grid(row=6, columnspan=10)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getTip)
equal_button.grid(row=7, column=2)

answer_entry11 = Entry(root)
answer_entry11.grid(row=7, columnspan=7)

# --- Discount calculator ---

discount_label = ttk.Label(root, text="Discount Calculator").grid(row=9, column=0)
price_label3 = ttk.Label(root, text="Price:").grid(row=10, column=0)
price_entry3 = Entry(root)
price_entry3.grid(row=10, columnspan=4)

you_save_label = ttk.Label(root, text="You Save:").grid(row=10, columnspan=6)
you_save_entry = Entry(root, width=8, fg="BLUE")
you_save_entry.grid(row=11, columnspan=6)

percent_label = ttk.Label(root, text="%:").grid(row=11, column=0)
percent_entry = Entry(root)
percent_entry.grid(row=11, columnspan=4)

equal_button = Button(root, text=" = ")
equal_button.bind("<Button-1>", getDiscount)
equal_button.grid(row=12, column=0)

answer_entry12 = Entry(root)
answer_entry12.grid(row=12, columnspan=4)

# --- Celsius to Fahrenheit ---

cel_to_fah_label = ttk.Label(root, text="Celsius to Fahrenheit").grid(row=5, column=6)

convert_entry = Entry(root)
convert_entry.grid(row=6, column=6)

cel_label = ttk.Label(root, text="°C").grid(row=6, column=7)

convert_button = Button(root, text="Convert")
convert_button.bind("<Button-1>", getFah)
convert_button.grid(row=7, column=6)

answer_entry13 = Entry(root)
answer_entry13.grid(row=8, column=6)

fah_label = ttk.Label(root, text="°F").grid(row=8, column=7)

# --- Fahrenheit to Celsius ---

fah_to_cel_label = ttk.Label(root, text="Fahrenheit to Celsius").grid(row=10, column=6)

convert_entry2 = Entry(root)
convert_entry2.grid(row=11, column=6)

fah_label2 = ttk.Label(root, text="°F").grid(row=11, column=7)

convert_button = Button(root, text="Convert")
convert_button.bind("<Button-1>", getCel)
convert_button.grid(row=12, column=6)

answer_entry14 = Entry(root)
answer_entry14.grid(row=13, column=6)

cel_label2 = ttk.Label(root, text="°C").grid(row=13, column=7)

root.mainloop()
