import pandas as pd
import socket, os, time, sys

class Servidor:
    def fecha(self,parametro):
        if parametro == "fecha":
            fecha = time.strftime("%A %B %d %Y")
            return fecha
        else:
            fallo = "Error en el formato"
            return fallo

    def hora(self,parametro):
        if parametro == "hora":
            hora = time.strftime("%H:%M:%S")
            return hora
        else:
            fallo = "Error en el formato"

    def minusculas(self,peticion):
        peticion_minusculas = peticion.lower()
        return peticion_minusculas

    def obtener_puerto(self):
        puerto =  16051
        return puerto

    def serv(self): #self para test
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        puerto = self.obtener_puerto()
        s.bind(("localhost",puerto))
        s.listen(1)

        while True:
            print("esperando que se conecte un cliente...")
            socket_hijo, direccion_cli = s.accept()

            try:
                hijo=os.fork()
                if hijo == 0:

                    print("conexión establecida con el cliente", direccion_cli)

                    while True:
                        datos = socket_hijo.recv(1024)#recibe el nombre fichero
                        
                        if not datos:# ctrl c
                            break
                        datos = self.minusculas(datos.decode("utf8"))

                        if datos == "fecha":
                            fecha = self.fecha(datos)
                            socket_hijo.send(fecha.encode("utf8"))

                        elif datos == "hora":
                            hora = self.hora(datos)
                            socket_hijo.send(hora.encode("utf8"))

                        else:
                            error1 = "Opcion incorrecta!!!"
                            socket_hijo.send(error1.encode("utf8"))
                        
            
            except KeyboardInterrupt: #se cierra el servidor
                salir = "servidor cerrado"
                socket_hijo.send(salir.encode("utf8"))
                print(salir)
                sys.exit(0) #cierre el programa bien 

            finally:
                socket_hijo.close() #CERRARLO SOLO UNA VEZ!!!!!!!!!!



if __name__=="__main__":
    servidor = Servidor()
    servidor.serv()
