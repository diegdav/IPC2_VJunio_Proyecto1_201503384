import xml.etree.ElementTree as ET
from os import system
from Objetos.Carta import Carta
from Objetos.Jugador import Jugador
from Objetos.Partida import Partida
from Objetos.Shuffle import Shuffle
from ListaCircular.ListaCircular import ListaCircular
from ListaEnlazada.ListaEnlazada import ListaEnlazada

mazo = ListaCircular()
jugador = ListaEnlazada()
partida = ListaEnlazada()

def leer_archivo_mazo(archivo):
    try:
        print('ando leyendo el archivo')
        tree = ET.parse(archivo)
        root = tree.getroot()
        
        contador = 0
        cartas = root.find('mazo_disponible/cartas')
        
        for carta in cartas.findall('carta'):
            if contador < 51:
                color = carta.attrib.get('color')
                valor = carta.text.strip()
                carta_obj = Carta(color, valor)
                
                contador += 1
                mazo.insertar(carta_obj)
                print(f'carta insertada: {carta_obj}')
            else:
                print('Ha alcanzado el máximo de cartas para el mazo (51 cartas)')
                break
        return True
    except FileNotFoundError:
        print(f'Archivo no encontrado: {archivo}')
        return None
    except ET.ParseError as e:
        print(f'Error al procesar el archivo XML: {e}')
        return None

def leer_archivo_jugador(archivo):
    try:
        print('ando leyendo el archivo')
        tree = ET.parse(archivo)
        root = tree.getroot()
        
        contador = 0
        jugadores = root.find('jugadores')
        
        for ju in jugadores.findall('jugador'):
            if contador < 4:
                nombre = ju.text.strip()
                jugador_obj = Jugador(nombre)
                
                contador += 1
                jugador.insertar(jugador_obj)
                print(f'jugador insertado: {jugador_obj}')
            else:
                print('Ha alcanzado el máximo de jugadores (4 jugadores)')
                break
        return True
    except FileNotFoundError:
        print(f'Archivo no encontrado: {archivo}')
        return None
    except ET.ParseError as e:
        print(f'Error al procesar el archivo XML: {e}')
        return None

def leer_archivo_partida(archivo):
    try:
        print('ando leyendo el archivo, partida')
        tree = ET.parse(archivo)
        root = tree.getroot()
        
        posicion_shuffle = 0
        partidas = root.find('partidas')
        
        for partida_elem in partidas.findall('partida'):
            nombre_partida = partida_elem.attrib.get('nombre')
            partida_obj = Partida(nombre_partida)
            print(f'Nombre partida: {partida_obj.get_nombre()}')
            
            for shuffle_elem in partida_elem.find('shuffles').findall('shuffle'):
                nombre_shuffle = shuffle_elem.text.strip()
                if nombre_shuffle == "RIGHT":
                    posicion_shuffle = shuffle_elem.attrib.get('x')
                    shuffle_obj = Shuffle(nombre_shuffle, posicion_shuffle)
                else:
                    shuffle_obj = Shuffle(nombre_shuffle, 0)
                partida_obj.lista_shuffle.insertarPartida(shuffle_obj)
            partida.insertarPartida(partida_obj)
            print(f'Partida insertada: {partida_obj} | {partida_obj.lista_shuffle.imprimirShuffle()}')
            print(' -------------------------------- ')
        return True
    except FileNotFoundError:
        print(f'Archivo no encontrado: {archivo}')
        return None
    except ET.ParseError as e:
        print(f'Error al procesar el archivo XML: {e}')
        return None
    
def obtenerPartida():
    listaPartida = partida.obtenerPartida()
    print(listaPartida)
    return listaPartida