from .Carta import Carta

class ListaCircular:
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__size = 0
    
    def insertar(self, color, valor):
        if self.__size < 51:
            nuevo = Carta(color, valor)
            
            if self.__primero == None:
                self.__primero = nuevo
                self.__ultimo = nuevo
                self.__ultimo.set_siguiente(self.primero)
            else:
                self.__ultimo.set_siguiente(nuevo)
                nuevo.set_siguiente(self.primero)
                self.__ultimo = nuevo
            
            self.size += 1
        else:
            print('No se pueden insertar más cartas, ya que el límite son 51')
    
    # Toma funcionamiento de una cola FIFO
    def extraerPozo(self):
        actual = self.__primero
        self.__ultimo.set_siguiente(self.__primero.get_siguiente)
        self.__primero = self.__primero.get_siguiente
        return actual 