import tkinter
from tkinter import ttk
from currency_converter import CurrencyConverter
from tkinter.messagebox import showinfo

root = tkinter.Tk()

root.geometry("400x400")
root.title("Конвертер валют")

c = CurrencyConverter()

def convert():
    showinfo("Ответ", str(round(c.convert(int(spinbox.get()), "RUB", languages_var.get()))))

spinbox = tkinter.Spinbox(from_=1, to=1000)
spinbox.pack()

languages = ["EUR", "USD", "BGN"]

languages_var = tkinter.StringVar(value=languages[0])
combobox = ttk.Combobox(textvariable=languages_var, values=languages)
combobox.pack()


button = tkinter.Button(text="Узнать(из рублей)", command=convert)
button.pack()


root.resizable(False, False)

root.mainloop()
