import socket
from threading import Thread
import tkinter


HOST = "127.0.0.1"
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def send():
    s.send((inp.get() + " : " + inp2.get()).encode("utf-8"))

def client():
    while True:
        data = s.recv(1024).decode("utf-8")
        l.insert(tkinter.END, data)



thread1 = Thread(target=client)

root = tkinter.Tk()
root.geometry("650x350")
root.title("Чат")
root.resizable(False, False)
l = tkinter.Listbox(width=60, height=17)
l.pack()
inp = tkinter.Entry()
inp.insert(0, "Аноним")
inp.pack()

inp2 = tkinter.Entry()
inp2.insert(0, "Сообщение")
inp2.pack()

B = tkinter.Button(text="Отправить", command=send)
B.pack()

scrollbar = tkinter.Scrollbar(orient="vertical", command=l.yview)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

thread1.start()
root.mainloop()