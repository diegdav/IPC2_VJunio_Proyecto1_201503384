class Carta:
    def __init__(self, color, valor):
        self.__color = color
        self.__valor = valor

    # Getters y Setters
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def __str__(self):
        return f'{self.__color} | {self.__valor}'