from tkinter import *

w = Tk()
w.title("Wrong nub")
w.resizable(width=FALSE, height=FALSE)
w.config(bg="red")

font = ("JetBrains Mono", 20, "bold")
wrong = Label(w, text="Wrong nub", font=font, fg="white", bg="red") 
wrong.grid(row=1, column=1, padx=30, pady=30)

w.mainloop()
