import string
import random
from typing import List
from abc import ABC, abstractmethod


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SoporteTicket:

    def __init__(self, cliente, asunto):
        self.identificacion = generate_id()
        self.cliente = cliente
        self.asunto = asunto


class EstrategiaPedidoTicket(ABC):
    @abstractmethod
    def creacion_pedido(self, lista: List[SoporteTicket]) -> List[SoporteTicket]:
        pass


class EstrategiaPedidoFIFO(EstrategiaPedidoTicket):
    def creacion_pedido(self, lista: List[SoporteTicket]) -> List[SoporteTicket]:
        return lista.copy()


class EstrategiaPedidoFILOO(EstrategiaPedidoTicket):
    def creacion_pedido(self, lista: List[SoporteTicket]) -> List[SoporteTicket]:
        lista_copia = lista.copy()
        lista_copia.reverse()
        return lista_copia


class EstrategiaPedidoAleatorio(EstrategiaPedidoTicket):
    def creacion_pedido(self, lista: List[SoporteTicket]) -> List[SoporteTicket]:
        lista_copia = lista.copy()
        random.shuffle(lista_copia)
        return lista_copia


class EstrategiaBlackHole(EstrategiaPedidoTicket):
    def creacion_pedido(self, lista: List[SoporteTicket]) -> List[SoporteTicket]:
        return []


class SoporteCliente:

    def __init__(self, procesamiento_estrategia: EstrategiaPedidoTicket):
        self.tickets = []
        self.procesamiento_estrategia = procesamiento_estrategia

    def creacion_ticket(self, cliente, asunto):
        self.tickets.append(SoporteTicket(cliente, asunto))

    def procesamiento_tickets(self):
        # create the ordered list
        ticket_lista = self.procesamiento_estrategia.creacion_pedido(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_lista) == 0:
            print("No hay tickets para procesar. ¡Bien hecho!")
            return

        # go through the tickets in the list
        for ticket in ticket_lista:
            self.procesamiento_ticket(ticket)

    def procesamiento_ticket(self, ticket: SoporteTicket):
        print("==================================")
        print(f"ticket: {ticket.identificacion}")
        print(f"cliente: {ticket.cliente}")
        print(f"asunto: {ticket.asunto}")
        print("==================================")


# create the application
aplicacion = SoporteCliente(EstrategiaPedidoAleatorio())

# register a few tickets
aplicacion.creacion_ticket("John Smith", "¡Mi computadora hace sonidos extraños!")
aplicacion.creacion_ticket("Linus Sebastian", "No puedo subir ningún video, por favor ayuda.")
aplicacion.creacion_ticket("Arjan Egges", "VSCode no resuelve automáticamente mis errores.")

# process the tickets
aplicacion.procesamiento_tickets()
