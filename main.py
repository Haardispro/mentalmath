from tkinter import *
import random

w = Tk()
#w.geometry("800x600")
w.title("Mental Maths")
w.resizable(height=FALSE, width=FALSE)
w.configure(bg="#1e1e1e")

#--font
font = ("JetBrains Mono", 20, "bold")
#Questions

def ranum():
    a = random.randint(0, 100)
    b = random.randint(0, 50)
    sum1 = a+b
    sub = a-b
    product = a*b
    #quotient is a/b only if a%b = 0
    #quotient = a/b
    res_list = [sum1, sub, product]#, quotient]
    res = random.choice(res_list)
    sign = ""
    if res == sum1:
        sign = "+"
    if res == sub:
        sign = "-"
    if res == product:
        sign = "X"
    """
    if res == quotient:
        sign = "/"
    """
    ranum.x = (a, sign, b)
    #print(res)

ranum()

#Functions
def chext():
    ranum()     

#Questions
heading = Label(w, text="Mental Maths", font=font, fg="white", bg="#1e1e1e")
question = Label(w, text=ranum.x, font=font, fg="white", bg="#1e1e1e")
#Input
user_input = Entry(w, width=20, font=font)

#Buttons
#--Next Button
chn = Button(w, text="Check and Next", command=chext, font=font)

#Positions
heading.grid(row=0, column=0, padx=10, pady=10)
question.grid(row=1, column=0, padx=10, pady=10)
user_input.grid(row=2, column=0, padx=10, pady=10)
chn.grid(row=3, column=0, padx=10, pady=10)


w.mainloop()
