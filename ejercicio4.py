import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QRadioButton, QButtonGroup, QPushButton, QComboBox
from PyQt5.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        self.pais = QLabel("Seleccione un pais:")
        self.paises = QComboBox()

        self.paises.addItems(["Jamaica", "Uruguay", "Bolivia", "Senegal", "Surinam"])
        

        self.boton = QPushButton("Confirmar")
        self.boton.clicked.connect(self.mostrar_seleccion)

        self.paises.currentIndexChanged.connect(self.cambio_automatico)

        layout.addWidget(self.paises)
        layout.addWidget(self.boton)
        layout.addWidget(self.pais)

        self.setLayout(layout)
    
    def mostrar_seleccion(self):
        seleccion = self.paises.currentText()
        self.pais.setText(f"Elegiste: {seleccion}")

    def cambio_automatico(self):
        self.pais.setText(f"Ahora elegiste: {self.paises.currentText()}")

    

app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec_())