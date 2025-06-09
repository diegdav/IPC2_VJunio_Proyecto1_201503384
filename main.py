from ListaCircular import ListaCircular
import xml.etree.ElementTree as ET
from xml.dom import minidom

def LeerArchivoMD(rutaArchivo):
    doc = minidom.parse(rutaArchivo)
    root = doc.documentElement
    
    print(root.tag)

if __name__ == '__main__':
    print('hola')