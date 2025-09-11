import sys
import os
from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QApplication,  QWidgetAction,  QTextEdit, QMenuBar, QFileDialog, QMessageBox, QStatusBar, QWidget, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QFont, QAction
from tabla_registros import Tabla_de_Registros

class Ventana_Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("  R. H. Bertoini  ")
        self.setGeometry(400,100,1200,900)
        self.inicializar_ui()
        self.show()

        self.crear_menu()

    def inicializar_ui(self):
        self.widget_central = QWidget(self)
        self.setCentralWidget(self.widget_central)
        self.widget_central.setStyleSheet("background-color: #1B263B")

        layout = QVBoxLayout(self.widget_central)
        layout.addStretch(1)

        #titulo
        titulo = QLabel("Raul H. Bertolini")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setFont(QFont("Arial", 40, QFont.Weight.Bold))
        titulo.setStyleSheet("color: white")

        #Subtitulo
        subtitulo = QLabel("Instalaciones Comerciales y Maquinas Gastronómicas")
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitulo.setFont(QFont("Arial", 20))
        subtitulo.setStyleSheet("color: white")

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        layout.addStretch(2)

    def crear_menu(self):
        menu_inicio = self.menuBar()
        menu_inicio.setStyleSheet("background-color: #4A6FA5")

        #Menu Caja
        menu_Caja = menu_inicio.addMenu('&Caja')
        menu_Caja.setStyleSheet("color: white")
        #Accion ingresar
        self.accion_ingresar_activo = QAction('&Ingresar Movimientos Activos', self)
        self.accion_ingresar_activo.setStatusTip('Registrar Ingresos')
        self.accion_ingresar_activo.triggered.connect(self.registrar)
        menu_Caja.addAction(self.accion_ingresar_activo)

        self.accion_ingresar_pasivo = QAction('&Ingresar Movimientos Pasivos', self)
        self.accion_ingresar_pasivo.setStatusTip('Registrar Egresos')
        self.accion_ingresar_pasivo.triggered.connect(self.registrar)
        menu_Caja.addAction(self.accion_ingresar_pasivo)

        self.accion_pago_proveedores = QAction('&Ingresar Pago Proveedores', self)
        self.accion_pago_proveedores.setStatusTip('Registrar Pago a Proveedores')
        self.accion_pago_proveedores.triggered.connect(self.registrar)
        menu_Caja.addAction(self.accion_pago_proveedores)


        #Menu Servicio post venta
        menu_Servicios = menu_inicio.addMenu('&Servicios')
        menu_Servicios.setStyleSheet("color: white")
        #Accion Registrar
        self.accion_registrar_post_venta = QAction('&Registrar Ingreso de Maquina', self)
        self.accion_registrar_post_venta.setStatusTip('Registrar servicio tecnico')
        self.accion_registrar_post_venta.triggered.connect(self.registrar)
        menu_Servicios.addAction(self.accion_registrar_post_venta)

        #Menu Tramites bancarios
        menu_tramites_bancarios = menu_inicio.addMenu('&Tramites Bancarios')
        menu_tramites_bancarios.setStyleSheet("color: white")
        #Accion Registrar
        self.accion_registro_cheques = QAction('&Cheques Propios Emitidos', self)
        self.accion_registro_cheques.setStatusTip('Registrar la emision de cheques propios')
        self.accion_registro_cheques.triggered.connect(self.registrar)
        menu_tramites_bancarios.addAction(self.accion_registro_cheques)

        #Menu proveedores
        menu_proveedores = menu_inicio.addMenu('&Proveedores')
        menu_proveedores.setStyleSheet("color: white")
        #accion pedido a proveedores
        self.pedido_proveedores = QAction('&Pedidos a Proveedores', self)
        self.pedido_proveedores.setStatusTip('Registrar los pedidos realizados a los proveedores')
        self.pedido_proveedores.triggered.connect(self.registrar)
        menu_proveedores.addAction(self.pedido_proveedores)
        
    
    def registrar(self):
        registro = self.sender()
        if registro == self.accion_ingresar_activo:
            path = 'caja_activos.txt'
        elif registro == self.accion_ingresar_pasivo:
            path = 'caja_pasivos.txt'
        elif registro == self.accion_pago_proveedores:
            path = 'pago_proveedores.txt'
        elif registro == self.accion_registrar_post_venta:
            path = 'registro_arreglos.txt'
        elif registro == self.accion_registro_cheques:
            path = 'registrar_cheques.txt'
        else:
            path = 'pedido_a_proveedores.txt'
        
        
        self.ventana_tabla = Tabla_de_Registros(path)
        self.ventana_tabla.path = path
        self.ventana_tabla.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana_Inicio()
    
    sys.exit(app.exec())