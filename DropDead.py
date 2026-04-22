import os
os.system('cls')

class Nodo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.conexion = []
        
    def add(self, nodo):
        self.conexion.append(nodo)
        print(f"The {self.nombre} device is ready to be connected with {nodo.nombre}")
    
    def sending(self, mensaje):
        print(f"{self.nombre}'s sending BOUNCE BOUNCE BOUNCE: {mensaje}")
        for nodo in self.conexion:
            nodo.getback(mensaje, self)
        
    def getback (self, mensaje, person1):
        print(f"{self.nombre} recibió mensaje de {person1.nombre}: {mensaje}") 
        
server = Nodo("Server")
customer1 = Nodo("Customer 1")
customer2 = Nodo("Customer 2")
customer3 = Nodo("Customer 3")

server.add(customer1)
server.add(customer2)
server.add(customer3)

server.sending(f"Hello pipolll It's a server's world and you're lucky to be livin' in it.")

"""
The Server device is ready to be connected with Customer 1
The Server device is ready to be connected with Customer 2
The Server device is ready to be connected with Customer 3
Server's sending BOUNCE BOUNCE BOUNCE: Hello pipolll It's a server's world and you're lucky to be livin' in it.
Customer 1 recibió mensaje de Server: Hello pipolll It's a server's world and you're lucky to be livin' in it.
Customer 2 recibió mensaje de Server: Hello pipolll It's a server's world and you're lucky to be livin' in it.
Customer 3 recibió mensaje de Server: Hello pipolll It's a server's world and you're lucky to be livin' in it.
"""
