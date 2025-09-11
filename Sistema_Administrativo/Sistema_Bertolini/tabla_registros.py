import sys
import os
from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QApplication,  QWidgetAction,  QTextEdit, QMenuBar, QFileDialog, QMessageBox, QStatusBar, QWidget, QLabel,QTableWidget, QHBoxLayout,
                             QPushButton)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QFont, QAction



class Tabla_de_Registros(QMainWindow):
    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.path = path
        self.setWindowTitle('Registro de Servicio Tecnico')
        self.setGeometry(400,100,1200,900)
        self.inicializar_ventana()
        

    def inicializar_ventana(self):
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        self.tabla = QTableWidget(10, 3)
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Descripción", "Importe"])

        self.tabla.setColumnWidth(0, 150)  
        self.tabla.setColumnWidth(1, 800)  
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setMaximumHeight(400)

        btn_guardar = QPushButton("Guardar TXT")
        btn_guardar.clicked.connect(self.guardar_registros_servicios)
        btn_guardar.setFixedHeight(40)  
        btn_guardar.setFixedWidth(120)

        layout_botones = QHBoxLayout()
        layout_botones.addWidget(btn_guardar)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.tabla)
        layout_principal.addLayout(layout_botones)
        
        widget_central.setLayout(layout_principal)

    def guardar_registros_servicios(self,path):
        path = getattr(self, 'path', None)
        if path is None:
            QMessageBox.critical(self, "Error", "No se ha definido la ruta del archivo.")
            return 
            
        try: 
            with open(path, 'w', encoding='utf-8') as archivo:
                    archivo.write("Fecha\tDescripción\tImporte\n")
                    for fila in range(self.tabla.rowCount()):
                        texto_fila = []
                        for columna in range(self.tabla.columnCount()):
                            item = self.tabla.item(fila, columna)
                            texto = item.text() if item else ""
                            texto_fila.append(texto)
                            archivo.write("\t".join(texto_fila) + "\n")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo:\n{e}")


