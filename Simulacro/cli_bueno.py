import socket

def recibirTodo(sock):
    datos = ""
    buff_size = 1024
    sock.setblocking(True)
    try:
        while True:
            datos += sock.recv(buff_size).decode("utf8")
            if datos == "servidor cerrado": #cerrar el servidor
                return datos

            sock.setblocking(False)

    except socket.error:
        pass
    return datos

def cli():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
    s.connect(("localhost",16051))
    
    #frase = input("Pedir la FECHA O HORA: ").strip()
    frase = input("Pedir la FECHA O HORA: ")
    if (frase):
        s.send(frase.encode("utf8")) #envia mensaje al cliente
        print (recibirTodo(s)) 
        s.close()
    else:
        s.close()
        print("Escribelo bien")

cli()
cli()
cli()

