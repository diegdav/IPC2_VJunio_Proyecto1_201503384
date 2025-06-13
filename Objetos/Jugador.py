from ListaEnlazada.ListaEnlazada import ListaEnlazada

class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.listaCartas = ListaEnlazada()
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return f'{self.__nombre}'