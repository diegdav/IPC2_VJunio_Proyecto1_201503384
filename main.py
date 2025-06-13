from ListaEnlazada import ListaEnlazada
from ListaCircular import ListaCircular
from utils import *
import customtkinter as ctk

rutaArchivo = "entrada_ejemplo.xml"

# leer_archivo_mazo(rutaArchivo)
# leer_archivo_jugador(rutaArchivo)
# leer_archivo_partida(rutaArchivo)


#Apariencia y tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurar una ventana:
        self.title("Card Clash - IPC2 Edition")
        self.geometry("1280x720")
    
        self.labelBienvenida = ctk.CTkLabel(self, text="Bienvenido a CARD CLASH - IPC2", font=("Arial", 24))
        self.labelBienvenida.pack(pady=20)
        
        self.label = ctk.CTkLabel(self, text="Esperando archivo de entrada", font=("Arial", 24))
        self.label.pack(pady=50)

        #Boton - Cargar configuraciones
        self.button1 = ctk.CTkButton(self, text="Cargar Partida", width=400, height=120, font=("Arial", 18), command=self.onButtonConfigurarClick)
        self.button1.place(relx=0.2, rely=0.5, anchor="center")

        self.button1 = ctk.CTkButton(self, text="Jugar", width=400, height=120, font=("Arial", 18), command=self.onButtonJugarClick)
        self.button1.place(relx=0.8, rely=0.5, anchor="center")

    def onButtonConfigurarClick(self):
        fileOpen = ctk.filedialog.askopenfilename(title="Selecciona un archivo de entrada: ", filetypes=[("Archivo de entrada", "*.xml")])

        if fileOpen:
            leer_archivo_mazo(archivo=fileOpen)
            leer_archivo_jugador(archivo=fileOpen)
            leer_archivo_partida(archivo=fileOpen)
            self.label.configure(text=f'Archivo cargado con éxito')
            print(f'label: {self.label.cget("text")}')

    def onButtonJugarClick(self):
        if self.label.cget("text") == "Archivo cargado con éxito":
            self.ventanaInicio = ctk.CTkToplevel(self)
            self.ventanaInicio.title("Card Clash - IPC2 Edition - Inicio")
            self.ventanaInicio.geometry("1280x720")
            
            partidas = obtenerPartida()
            self.comboBox = ctk.CTkComboBox(self.ventanaInicio, values=partidas, command=self.seleccion_Partida)
            self.comboBox.pack(pady=50)
            
            self.ButtonSeleccionar = ctk.CTkButton(self.ventanaInicio, text="Seleccionar", width=400, height=80, font=("Arial",18), command=self.onButtonSeleccionarPartida)
            self.ButtonSeleccionar.pack(pady=70)
        else:
            dialogo = ctk.CTkToplevel(self)
            dialogo.geometry("300x150")
            dialogo.title("Error")
            
            mensaje = ctk.CTkLabel(dialogo, text="debe de seleccionar un archivo primero", font=("Arial", 14))
            mensaje.pack(pady=20)
    
    seleccion_de_partida = None
    
    def seleccion_Partida(self, choice):
        seleccion_de_partida = choice
        print(seleccion_de_partida)
    
    def onButtonSeleccionarPartida(self):
        self.ventanaPartidaSeleccionada = ctk.CTkToplevel(self)
        self.ventanaPartidaSeleccionada.title("Card Clash - IPC2 Edition - Partida")
        self.ventanaPartidaSeleccionada.geometry("1280x720")
        
        self.label1 = ctk.CTkLabel(self.ventanaPartidaSeleccionada, text="Partida Seleccionada:", width=400, height=120, font=("Arial", 18))
        self.label1.pack(pady=10)
        
        self.label2 = ctk.CTkLabel(self.ventanaPartidaSeleccionada, text=f'{self.seleccion_de_partida}', width=40, height=80, font=("Arial", 18))
        self.label2.pack(pady=20)
    
if __name__ == '__main__':
    app = App()
    app.mainloop()
    print('hola')