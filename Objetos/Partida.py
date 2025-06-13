from ListaEnlazada.ListaEnlazada import ListaEnlazada

class Partida:
    def __init__(self, nombre):
        self.__nombre = nombre
        #self.__lista_shuffle = lista_shuffle
        self.lista_shuffle = ListaEnlazada()

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    # def get_lista_shuffle(self):
    #     return self.__lista_shuffle
    
    # def set_lista_shuffle(self, lista_shuffle):
    #     self.__lista_shuffle = lista_shuffle
    
    def __str__(self):
        return f'{self.__nombre}'