from molmass import Formula
from tkinter import *

root = Tk()
root.geometry("400x270")
root.title("Molar Mass Calculator")
root.configure(bg="medium sea green")
userIn = StringVar()
var = StringVar()

def calc():
    input = userIn.get()
    ans = Formula(input).mass
    var.set(ans)


f1 = ("poppins", 24, "bold underline")
f2 = ("poppins", 18, "bold")
f3 = ("poppins", 12, "bold")
f4 = ("poppins", 10, "bold")

Label(root, text = "Molar Mass Calculator", font = f1, fg = "white", bg="medium sea green").pack(pady = 10)
Label(root, text = "enter formula:", font = f3, fg = "white", bg="medium sea green").pack(pady = 9)
Entry(root, textvariable = userIn).pack(pady = 5)
Button(root, text = "enter", font = f4, fg = "black", bg="lemon chiffon", command = calc).pack(pady = 7)

Label(root, textvariable = var, font = f2, fg = "white", bg="medium sea green").pack(pady = 6)

root.mainloop()

