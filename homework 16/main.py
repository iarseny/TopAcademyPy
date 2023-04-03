import tkinter

root = tkinter.Tk()

root.geometry("400x400")
root.title("Конвертер валют")

var = tkinter.StringVar()

spinbox = tkinter.Spinbox(from_=1, to=1000)
spinbox.pack()

button = tkinter.Button(text="Узнать")
button.pack()

root.resizable(False, False)

root.mainloop()
