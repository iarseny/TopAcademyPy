import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8000
HOST = "127.0.0.1"

s.bind((HOST, PORT))
s.listen(5)

clients = []

def f1():
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        thread2 = Thread(target=f2, args=(conn, ))
        thread2.start()

def f2(i):
    while True:
        try:
            data = i.recv(1024)
            for client in clients:
                client.send(data)
        except:
            clients.remove(i)

thread1 = Thread(target=f1)
thread1.start()
