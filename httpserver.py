import socket
import platform
import jinja2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 5000))
s.listen()
HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\n"

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(""),
    trim_blocks=True,
    lstrip_blocks=True)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode("utf-8")
    if data.split("\n")[0].split("/")[1] == "c HTTP":
        conn.send(HDRS.encode("utf-8") + (platform.machine() + "\n\n\n\r\r" + platform.version() + "\n\n\n" + platform.platform() + "\n\n\n" + platform.processor()).encode("utf-8"))
    else:
        conn.send(HDRS.encode("utf-8") + env.get_template("html.html").render().encode("utf-8"))