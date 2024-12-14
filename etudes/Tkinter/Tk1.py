from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox 

#ГЛАВНОЕ ОКНО


root = Tk()

root.title("Калькулятор площади параллелипипеда")
root.geometry("512x256")
root["bg"] = "#F0FFFF"
root.resizable(width=False, height=False)


#ВИДЖЕТ FRAME


frame = Frame(
    root,
    padx = 10,
    pady = 10
)
frame.pack(expand=True)
frame.pack(fill=Y)
frame["bg"] = "#F0FFFF"


#ТЕКСТ


method_lbl = Label(
    frame,
    text="Способ расчёта площади"
)
method_lbl["bg"] = "#F0FFFF"
method_lbl.grid(row=1, column=1)
#method_lbl.configure(text="Не выбирайте")


#ВЫПАДАЮЩИЙ СПИСОК


methods = ["Через основание и высоту",
           "Через две стороны и угол"]

def selected(event):
    selection = combobox.get()
    if selection == "Через основание и высоту":
        method_with_base_and_height()
    elif selection == "Через две стороны и угол":
        method_with_sides_and_angle()

combobox = Combobox(frame, values=methods, width=30, state="readonly")
combobox.grid(row=2, column=1)
combobox.set("Через основание и высоту")
combobox.bind("<<ComboboxSelected>>", selected)


#ПОЛЯ ВВОДА


base_lbl = Label(
    frame,
    text="Основание треугольника"
)
base_lbl["bg"] = "#F0FFFF"
base_lbl.grid(row=3, column=1, pady=10)
base_ent = Entry(
    frame
)
base_ent.grid(row=3, column=2)

base_ent.focus()


#base_ent = Entry(
#    frame,
#    state="disabled"
#)
#base_ent.grid(row=3, column=2)


height_lbl = Label(
    frame,
    text="Высота треугольника"
)
height_lbl["bg"] = "#F0FFFF"
height_lbl.grid(row=4, column=1, pady=10)
height_ent = Entry(
    frame
)
height_ent.grid(row=4, column=2)


#КНОПКА


calc_btn = Button(
    frame,
    text="Рассчитать площадь",
    command=lambda: calculate_area_with_base_and_height(base_ent.get(), height_ent.get())
)
calc_btn.grid(row=5, column=2)


#ИНФОРМАЦИОННОЕ ОКНО


def calculate_area_with_base_and_height(base, height):
    base = float(base)
    height = float(height)
    area = float(base * height / 2)
    show_result(area)

def show_result(area): 
    area = round(area, 2)   
    messagebox.showinfo('Результат', f'Площадь треугольника равна {area}')



root.mainloop()
