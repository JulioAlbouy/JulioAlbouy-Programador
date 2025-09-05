
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar, 
                             QAction, QFileDialog, QMessageBox, QStatusBar,
                             QVBoxLayout, QWidget, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence, QFont

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Texto")
        self.showMaximized()
        
        cuerpo = QWidget()
        self.setCentralWidget(cuerpo)
        
        layout = QVBoxLayout(cuerpo)
        self.setStyleSheet("background-color: #19B6D1;")

        self.editor = QTextEdit()
        self.editor.setFixedSize(800,600)
        fuente = QFont("Times New Roman", 20)
        self.editor.setFont(fuente)
        self.editor.setPlaceholderText("Escribe aqui: ")
        self.editor.setStyleSheet("background-color: #A0B6BA;color: black;")       
        layout.addWidget(self.editor, alignment=Qt.AlignCenter)

        self.barra_estado = QStatusBar()


    def crear_menu(self):
        menu_general = self.menuBar()
        menu_general.setStyleSheet("background-color: #81D6E3; color: black;")
        
        menu_archivo = menu_general.addMenu("&Archivo")
        menu_ayuda = menu_general.addMenu("&Ayuda")
        menu_editar = menu_general.addMenu("&Editar")

        accion_nuevo = QAction("&Nuevo", self)
        accion_nuevo.setShortcut(QKeySequence.New)
        accion_nuevo.triggered.connect(self.nuevo_archivo)
        menu_archivo.addAction(accion_nuevo)

        accion_abrir = QAction("&Abrir", self)
        accion_abrir.setShortcut(QKeySequence("Ctrl+a"))
        accion_abrir.triggered.connect(self.abrir_archivo)
        menu_archivo.addAction(accion_abrir)
        
        accion_guardar = QAction("&Guardar", self)
        accion_guardar.setShortcut(QKeySequence("Ctrl+s"))
        accion_guardar.triggered.connect(self.guardar_archivo)
        menu_archivo.addAction(accion_guardar)

        accion_salir = QAction("&Salir", self)
        accion_salir.setShortcut(QKeySequence("Ctrl+e"))
        accion_salir.triggered.connect(self.salir_archivo)
        menu_archivo.addAction(accion_salir)

       
        accion_acerca_de = QAction("&Acerca de", self)
        accion_acerca_de.setShortcut(QKeySequence("Ctrl+D"))
        accion_acerca_de.triggered.connect(self.acerca_de)
        menu_ayuda.addAction(accion_acerca_de)

        accion_copiar = QAction("&Copiar", self)
        accion_copiar.setShortcut(QKeySequence("Ctrl+c"))
        accion_copiar.triggered.connect(self.copiar)
        menu_editar.addAction(accion_copiar)

        accion_pegar = QAction("&Pegar", self)
        accion_pegar.setShortcut(QKeySequence("Ctrl+p"))
        accion_pegar.triggered.connect(self.pegar)
        menu_editar.addAction(accion_pegar)

        accion_cortar = QAction("&Cortar", self)
        accion_cortar.setShortcut(QKeySequence("Ctrl+x"))
        accion_cortar.triggered.connect(self.cortar)
        menu_editar.addAction(accion_cortar)

    def cortar(self):
        self.editor.cut()
        self.statusBar().showMessage("Texto cortado", 2000)

    def pegar(self):
        self.editor.paste()
        self.statusBar().showMessage("Texto pegado", 2000)

    def copiar(self):
        self.editor.copy()
        self.statusBar().showMessage("Texto copiado", 2000)

    def acerca_de(self):
        """Muestra información sobre el programa y la ventana actual."""
        info = (
            f"Editor de Texto v1.0\n"
            f"Creado con PyQt5\n"
            f"Autores: Mateo Woinarowski y Julio Albouy\n\n"
            f"Ventana actual:\n"
            f"  - Título: {self.windowTitle()}\n"
            f"  - Tamaño: {self.width()}x{self.height()} píxeles\n"
            f"  - Posición: ({self.x()}, {self.y()})\n"
        )

        QMessageBox.information(self, "Acerca de", info)
    
        
    def nuevo_archivo(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Desea guardar antes de crear un nuevo archivo?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            ruta, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
            if ruta:
                with open(ruta, "w", encoding="utf-8") as archivo:
                    archivo.write(self.editor.toPlainText())
        elif respuesta == QMessageBox.No:
            print("No se guardó el archivo, creando uno nuevo...")
            self.editor.clear()
        
    
    def abrir_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', 'Archivos de texto (*.txt)')
        if archivo:
            try:
                 with open(archivo, 'r', encoding='utf-8') as f:
                     contenido = f.read()
                     self.editor.setPlainText(contenido)
            except Exception as e:
                 QMessageBox.warning(self, 'Error', f'No se pudo abrir el archivo:\n{e}')
        
    
    def guardar_archivo(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
        if ruta:
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write(self.editor.toPlainText())
            self.statusBar().showMessage("Se ha guardado con exito!!", 3000)

    def salir_archivo(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Desea guardar antes de salir de la ventana?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            ruta, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
            if ruta:
                with open(ruta, "w", encoding="utf-8") as archivo:
                    archivo.write(self.editor.toPlainText())
                self.statusBar().showMessage("Se ha guardado con exito!!", 3000)
                sys.exit(app.exec_())
        elif respuesta == QMessageBox.No:
            sys.exit(app.exec_())

        

         
app = QApplication(sys.argv)
editor = EditorTexto()
editor.crear_menu()
editor.show()
sys.exit(app.exec_())