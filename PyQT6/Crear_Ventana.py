
#Creamos nuestra primera ventana con PyQT6 usando QWidget



#----Importamos SYS e importamos de PyQt6, QApplication y QWidget para desarrolar nuestra ventana
#QApplication nos va a controlar todos los eventos que sucedan en la interfaz
#QWidget es la clase que utilizamos para desarrollar nuestra ventana.

import sys
from PyQt6.QtWidgets import QApplication, QWidget


#Definimos la calase ventana y realizamos la herencia de la clase QWidget
class Ventana(QWidget):
    def __init__(self):
        super().__init__() #Inicializamos el metodo constructor de la clase heredada
        self.inicializar_UI() #Creamos un metodo en el cual integraremos todos los elementos de la ventana
                              #esto se realiza para que la estructura este en un metodo dedicado y no todo dentro del constructor
                              #no hace falta hacerlo pero mejora la estructura del codigo.
        
    def inicializar_UI(self): 
        self.setGeometry(300,300,800,600)
        self.setWindowTitle("Mi Primera Ventana")
        self.show() #metodo que ejecuta la ventana 


if __name__ == "__main__":  #Evaluamos si existe el archivo 
    app = QApplication(sys.argv) #Instanaciamos el QApplication para manipular los eventos de la ventana
    interfaz = Ventana() #Instanciamos la ventana de la calse VENTANA
    sys.exit(app.exec()) #Se encarga de una vez cerrada la ventana, se liberen los recursos que esta consumia




        

    