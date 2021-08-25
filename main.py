from tkinter import *
import random
import os

w = Tk()
#w.geometry("800x600")
w.title("Mental Maths")
w.resizable(height=FALSE, width=FALSE)
w.configure(bg="#1e1e1e")

#--font
font = ("JetBrains Mono", 20, "bold")
#Logo
logo = PhotoImage(file = "logo.png")
w.iconphoto(False, logo)
#Questions

def ranum():
    a = random.randint(0, 100)
    b = random.randint(0, 50)
    ranum.sum1 = a+b
    ranum.sub = a-b
    ranum.product = a*b
    #quotient is a/b only if a%b = 0
    #quotient = a/b
    res_list = [ranum.sum1, ranum.sub, ranum.product]#, quotient]
    ranum.res = random.choice(res_list)
    ranum.sign = ""
    if ranum.res == ranum.sum1:
        ranum.sign = "+"
    if ranum.res == ranum.sub:
        ranum.sign = "-"
    if ranum.res == ranum.product:
        ranum.sign = "X"
    """
    if res == quotient:
        sign = "/"
    """
    ranum.x = (a, ranum.sign, b)
    #print(res)

ranum()

#Functions
def chext():
    i = user_input.get()
    i = int(i)

    
    if ranum.sign == "+" and i == ranum.sum1:
        w.destroy()
        os.system("python main.py")

    elif ranum.sign == "-" and i == ranum.sub:
        w.destroy()
        os.system("python main.py")

    elif ranum.sign == "X" and i == ranum.product:
        w.destroy()
        os.system("python main.py")
    else:
        print("Wrong Nub")
    #w.destroy()
    #os.system("python main.py")
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
