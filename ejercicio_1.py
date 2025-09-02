import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)
    
        
        self.nombre = QLabel("Nombre:")
        self.label1 = QLabel("Formulario de registro")
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("")
        
        layout.addWidget(self.label1, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.nombre, 1, 0)
        layout.addWidget(self.nombre_input,2, 0)

app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec_())