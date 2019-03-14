import socket
import random
PORT = 8071
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5
aleatorio = random.randrange(100)
print("El numero aleatorio", aleatorio)



def comprobar(numero, aleatorio):
    numero = int(numero)
    if 1<=(aleatorio -numero ) <= 10 or 1<= (numero -aleatorio) <= 10 and numero!= aleatorio:
        mns = ("Caliente, caliente")
    elif 10 < (aleatorio - numero )<99:
        mns = ("frío, frío por abajo  ")
    elif 10< (numero -aleatorio) <99:
        mns = ("frío, frío por arriba")
    elif numero == aleatorio:
        mns = ("Felicidades")
    return mns



def process_client(clientsocket):
    print(clientsocket)
    condition = True
    while condition:

        inbox = clientsocket.recv(2048).decode("utf-8")
        print("El cliente nos dice: ", inbox)
        print(comprobar(inbox,aleatorio))
        if (comprobar(inbox,aleatorio)) == "Felicidades":
            condition = False

        outbox = str.encode(comprobar(inbox,aleatorio))
        clientsocket.send(outbox)


    clientsocket.close()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = IP
try:
    serversocket.bind((hostname, PORT))

    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Esperando conexión con %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()

        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
