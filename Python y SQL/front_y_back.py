
import mysql.connector
from mysql.connector import Error
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QTextEdit, QPushButton,
                             QLineEdit, QHBoxLayout, QGridLayout, QVBoxLayout,
                             QLabel
                             )
from PyQt5.QtCore import Qt 

#Backend
#Frontend
class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_UI()
        self.set_objets()
        self.show()
        self.limite_de_registros = 10
        self.controlar_registros = 0
        self.mostrar_todo()

    def inicializar_UI(self):
        self.setWindowTitle('Ventana Principal')
        self.setGeometry(425,75,600,380)

    def set_objets(self):
        layout_principal = QHBoxLayout()

        #Mitad para la izquierda
        layout1 = QVBoxLayout()
        self.tabla = QTextEdit()
        self.tabla.resize(580, 580)
        layout1.addWidget(self.tabla)

        layout2 = QHBoxLayout()
        self.boton_siguiente = QPushButton('Siguiente')
        self.boton_siguiente.setFixedSize(120, 40)
        self.boton_siguiente.setStyleSheet(" border-radius: 8px; background-color: lightblue")
        boton_atras = QPushButton('Atras')
        boton_atras.setStyleSheet(" border-radius: 8px; background-color:lightblue")
        boton_atras.setFixedSize(120, 40)
        self.boton_siguiente.clicked.connect(self.adelantar_pagina)
        boton_atras.clicked.connect(self.retroceder_pag)

        layout2.addWidget(boton_atras)
        layout2.addWidget(self.boton_siguiente)
        
        layout1.addLayout(layout2)
        
        #Mitad para la derecha

        layout_formulario = QVBoxLayout()
        layout_formulario.setAlignment(Qt.AlignCenter)
        label_nombre = QLabel('Buscar por Nombre de Jugador')
        label_nombre.setStyleSheet("font-size: 20px; font-family: Helvetica, sans-serif;")
        input_nombre = QLineEdit()
        boton_buscar_nombre = QPushButton('Buscar')
        boton_buscar_nombre.setFixedSize(120, 25)
        boton_buscar_nombre.setStyleSheet(" border-radius: 8px; background-color:lightblue")

        label_apellido = QLabel('Buscar por Apellido de Jugador')
        label_apellido.setStyleSheet("font-size: 20px; font-family: Helvetica, sans-serif")
        input_apellido = QLineEdit()
        boton_buscar_apellido = QPushButton('Buscar')
        boton_buscar_apellido.setFixedSize(120, 25)
        boton_buscar_apellido.setStyleSheet(" border-radius: 8px; background-color:lightblue")

        layout_formulario.addWidget(label_nombre)
        layout_formulario.addWidget(input_nombre)
        layout_formulario.addWidget(boton_buscar_nombre)
        
        layout_formulario.addWidget(label_apellido)
        layout_formulario.addWidget(input_apellido)
        layout_formulario.addWidget(boton_buscar_apellido)

        layout_principal.addLayout(layout1)
        layout_principal.addLayout(layout_formulario)
        
        self.setLayout(layout_principal)


    def conectar_sql(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                database = "riverplate",
                user = "root",
                password = "river",
                port = 3306
)   
    
            if self.conexion.is_connected():
                    print("Conexion exitosa a MySql")
                    info_servidor = self.conexion.get_server_info()
                    print(f"Informacion del servidor: MySQL {info_servidor}")

                    cursor = self.conexion.cursor()
                    cursor.execute("SELECT DATABASE();")
                    bd_actual = cursor.fetchone()
                    print(f"Base de Datos actual : {bd_actual[0]}")
                    return self.conexion
            

        except Error as e:
            print(f'No se pudo conectar a la base de datos {e}')

    
    def mostrar_todo(self):
        
        conexion = self.conectar_sql()
        cursor = conexion.cursor()
       
        select_all = f"SELECT nombre, apellido FROM persona LIMIT {self.limite_de_registros} OFFSET {self.controlar_registros}"
        cursor.execute(select_all)
        jugadores = cursor.fetchall()
        return jugadores

    def adelantar_pagina(self):
        self.tabla.clear()
        lista_jugadores = self.mostrar_todo()
        for jugador in lista_jugadores:
            jugador = str(jugador)
            self.tabla.insertPlainText(jugador + "\n")                
        self.controlar_registros = self.controlar_registros + self.limite_de_registros        
        
        
    def retroceder_pag(self):
        self.tabla.clear()
        if self.controlar_registros != 0:
            self.controlar_registros = self.controlar_registros - self.limite_de_registros
        lista_jugadores = self.mostrar_todo()
        for jugador in lista_jugadores:
            jugador = str(jugador)
            self.tabla.insertPlainText(jugador + "\n")    
   
            

        
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = main_window()
    menu.show()
    sys.exit(app.exec_())

  

  