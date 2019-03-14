import socket

IP = "127.0.0.1"
PORT = 8071
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))
    print("Conexión establecida con el servidor ")
except OSError:
    print("El Socket ya está usado")

    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

condition = True
while condition:

    out = input("Introduzca un número entre 0 y 99 : ")
    outbox = str.encode(out)
    s.send(outbox)
    a = s.recv(2048).decode("utf-8")
    print("El servidor nos dice: ", a)
    if  a.lower() == "felicidades":
        condition = False

s.close()
