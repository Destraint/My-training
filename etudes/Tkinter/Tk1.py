from tkinter import *

root = Tk()

root.title("Калькулятор площади параллелипипеда")
root.geometry("512x256")
root["bg"] = "#F0FFFF"
root.resizable(width=False, height=False)


frame = Frame(
    root,
    padx = 10,
    pady = 10
)
frame.pack(expand=True)
frame.pack(fill=Y)
frame["bg"] = "#F0FFFF"

method_lbl = Label(
    frame,
    text="Способ расчёта площади"
)
method_lbl["bg"] = "#F0FFFF"
method_lbl.grid(row=1, column=1)


root.mainloop()
