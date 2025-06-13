class Shuffle:
    def __init__(self, nombre, posicion):
        self.__nombre = nombre
        self.__posicion = posicion
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_posicion(self):
        return self.__posicion
    
    def set_posicion(self, posicion):
        self.__posicion = posicion
    
    def __str__(self):
        return f'Shuffle: {self.__nombre} | posicion: {self.__posicion}'