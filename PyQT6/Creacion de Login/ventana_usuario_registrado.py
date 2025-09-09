import sys 
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, 
QPushButton, QMessageBox, QCheckBox, QDialog)
from PyQt6.QtGui import (QFont, QPixmap)


class Ventana_de_Usuario(QDialog):
    def __init__(self):
        super().__init__()
        self.generar_formulario()
       
        

    def generar_formulario(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Usuario Registrado")

        self.usuario_label = QLabel(self)
        self.usuario_label.setText("Usuario: ")
        self.usuario_label.setFont(QFont('Arial', 10))
        self.usuario_label.move(20,44)

        self.input_usuario = QLineEdit(self)
        self.input_usuario.resize(250,28)
        self.input_usuario.move(90,40)

        self.contraseña_label = QLabel(self)
        self.contraseña_label.setText("Contraseña: ")
        self.contraseña_label.setFont(QFont("Arial", 10))
        self.contraseña_label.move(20, 74)

        self.input_contraseña = QLineEdit(self)
        self.input_contraseña.resize(250,28)
        self.input_contraseña.move(90,70)
        self.input_contraseña.setEchoMode(QLineEdit.EchoMode.Password)

        self.contraseña_label2 = QLabel(self)
        self.contraseña_label2.setText("Contraseña: ")
        self.contraseña_label2.setFont(QFont("Arial", 10))
        self.contraseña_label2.move(20, 104)

        self.input_contraseña2 = QLineEdit(self)
        self.input_contraseña2.resize(250,28)
        self.input_contraseña2.move(90,100)
        self.input_contraseña2.setEchoMode(QLineEdit.EchoMode.Password)

        self.create_button = QPushButton(self)
        self.create_button.setText("Create")
        self.create_button.resize(150, 32)
        self.create_button.move(20,170)
        self.create_button.clicked.connect(self.crear_usuario)

        self.cancel_button = QPushButton(self)
        self.cancel_button.setText("Cancel")
        self.cancel_button.resize(150, 32)
        self.cancel_button.move(170,170)
        self.create_button.clicked.connect(self.cancelar_creacion)

        """
        self.accept_button = QPushButton(self)
        self.accept_button.resize(250,30)
        self.accept_button.setText("Confirm")
        self.accept_button.move(90,200)
        #self.accept_button.clicked.connect(self.validar_contraseñas)
        """

    """
    def validar_contraseñas(self):
        if (self.input_contraseña.text() == self.input_contraseña2.text()):
            self.inicio_confirmado = QMessageBox()
            self.inicio_confirmado.setText("Registro completado")
            self.inicio_confirmado.setGeometry(130,130,250,200)
            self.inicio_confirmado.exec()
        else:
            self.inicio_confirmado = QMessageBox()
            self.inicio_confirmado.setText("Las contraseñas no coinciden")
            self.inicio_confirmado.setGeometry(130,130,250,200)
            self.inicio_confirmado.exec()
      """  
    
    def cancelar_creacion(self):
        self.close()

    def crear_usuario(self):
        usuario_path = 'usuarios.txt'
        usuario = self.input_usuario.text()
        password1 = self.input_contraseña.text()
        password2 = self.input_contraseña2.text()

        if(usuario == "" or password1 == "" or password2 == ""):
            QMessageBox.warning(self, "Campos incompletos", "Por favor, complete todos los campos",
            QMessageBox.StandardButton.Close)
            
        elif(password1 != password2):
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden",
            QMessageBox.StandardButton.Close)
        else:
            try:
                print("Entrando al bloque de escritura")
                with open(usuario_path, "a+") as f:
                    f.write(f"{usuario}, {password1}, {password2}")
                QMessageBox.information(self, "Creacion Exitosa", "Usuario creado correctamente", QMessageBox.StandardButton.Ok)
                
                self.close()
            except FileNotFoundError as e:
                QMessageBox.warning(self, "Error", f"La base de datos del usuario no existe: {e}", QMessageBox.StandardButton.Close)
                
                
        