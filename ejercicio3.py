import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QRadioButton, QButtonGroup, QPushButton
from PyQt5.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        self.label = QLabel()
        self.boton_m = QRadioButton("Masculino")
        self.boton_f = QRadioButton("Femenino")

        self.grupo = QButtonGroup()
        self.grupo.addButton(self.boton_m)
        self.grupo.addButton(self.boton_f)

        self.boton = QPushButton("Confirmar")

        self.boton.clicked.connect(self.mostrar_opcion)

        layout.addWidget(self.boton_m)
        layout.addWidget(self.boton_f)
        layout.addWidget(self.boton)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mostrar_opcion(self):
        if self.boton_m.isChecked():
            self.label.setText("Seleccionaste la opcion Masculino")
        elif self.boton_f.isChecked():
            self.label.setText("Seleccionante la opcion Femenino")
            

app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec_())