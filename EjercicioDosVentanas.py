import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setStyleSheet("Background-color: #ABCFD4")
        
        self.nombre_input = QLineEdit()
        self.apellido_input = QLineEdit()
        self.email_input = QLineEdit()

        self.formulario = QLabel("Formulario de afiliacion")
        self.formulario.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial;")
        self.nombre = QLabel("Nombre:")
        self.apellido = QLabel("Apellido:")
        self.email = QLabel("Email:")
        
        self.nombre_input.setStyleSheet("Border-radius: 5px; Background-color: #B570AB")
        self.apellido_input.setStyleSheet("Border-radius: 5px; Background-color: #B570AB")
        self.email_input.setStyleSheet("Border-radius: 5px; Background-color: #B570AB")
      


        self.formulario.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.formulario,0, 0, 1, 2, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.nombre, 2, 0)
        layout.addWidget(self.nombre_input, 2, 1)
        layout.addWidget(self.apellido, 3, 0)
        layout.addWidget(self.apellido_input, 3, 1)
        layout.addWidget(self.email, 4, 0)
        layout.addWidget(self.email_input, 4, 1)
    
    def getNombre(self):
        return self.nombre_input.text().capitalize()
    
    def getApellido(self):
        return self.apellido_input.text().capitalize()
    
    def getEmail(self):
        return self.email_input.text()


    

class VentanaHerramientas(QWidget):
    def __init__(self, VentanaFormulario):
        super().__init__()
        self.ventanaFormulario = VentanaFormulario
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button_guardar = QPushButton("GUARDAR")
        self.button_abrir = QPushButton("ABRIR")
        self.button_salir = QPushButton("SALIR")
        self.button_buscar = QPushButton("BUSCAR")

        self.button_guardar.setStyleSheet("Border-radius: 5px; Background-color: #729094")
        self.button_abrir.setStyleSheet("Border-radius: 5px; Background-color: #85C9A4")
        self.button_salir.setStyleSheet("Border-radius: 5px; Background-color: #CDE36D")
        self.button_buscar.setStyleSheet("Border-radius: 5px; Background-color: #E8B684")


        self.button_guardar.clicked.connect(self.clickear_button_guardar)
        self.button_abrir.clicked.connect(self.clickear_button_abrir)
        self.button_salir.clicked.connect(self.clickear_button_salir)
        self.button_buscar.clicked.connect(self.clickear_button_buscar)

        layout.addWidget(self.button_guardar)
        layout.addWidget(self.button_abrir)
        layout.addWidget(self.button_salir)
        layout.addWidget(self.button_buscar)

    def clickear_button_guardar(self):
        print(f"""
            El nombre es: {self.ventanaFormulario.getNombre()},
            El apellido es: {self.ventanaFormulario.getApellido()},
            El email es: {self.ventanaFormulario.getEmail()}""")
    
    def clickear_button_abrir(self):
        print("¡ABRISTE EL ARCHIVO!")

    def clickear_button_salir(self):
        sys.exit(app.exec_())

    
    def clickear_button_buscar(self):
        print("¡BUSCASTE EL ARCHIVO!")

        
app = QApplication(sys.argv)
ventana_form = VentanaFormulario()
ventana_herr = VentanaHerramientas(ventana_form)
ventana_form.show()
ventana_herr.show()
sys.exit(app.exec_())

