from .Nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.size = 0
    
    def insertar(self, dato):
        if self.size < 4:
            nuevo = Nodo(dato)
        
            if self.primero == None:
                self.primero = nuevo
            else:
                actual = self.primero
                while actual.get_siguiente() != None:
                    actual = actual.get_siguiente()
                actual.set_siguiente(nuevo)
            self.size += 1
    
    def insertarPartida(self, dato):
        nuevo = Nodo(dato)
        if self.primero == None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.get_siguiente() != None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo)
        self.size += 1
    
    def imprimirShuffle(self):
        actual = self.primero
        while actual != None:
            print(f'Shuffle: {actual.get_dato().get_nombre()} | posicion: {actual.get_dato().get_posicion()}, este?')
            actual = actual.get_siguiente()
    
    def obtenerPartida(self):
        listaPartida = []
        actual = self.primero
        
        while actual != None:
            listaPartida.append(actual.get_dato().get_nombre())
            actual = actual.get_siguiente()
            
        return listaPartida