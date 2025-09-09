import sys 
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, 
QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import (QFont, QPixmap)
from ventana_usuario_registrado import Ventana_de_Usuario

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_UI()

    def inicializar_UI(self):
        self.setGeometry(300,300,350,250)
        self.setWindowTitle("Mi Primer Login")
        self.generar_Formulario()
        self.show()

    #Creamos una nueva funcion en la cual integramos todos los elementos de nuestro QWidget, asi organizamos la estructura del codigo.
    def generar_Formulario(self):
        self.logearse = False

        #Creamos el QLabel (Usuario) con sus atributos.
        self.usuario = QLabel(self)
        self.usuario.setText("Usuario: ")
        self.usuario.setFont(QFont("Arial", 10))
        self.usuario.move(20, 54)

        #Creamos el QLineEdit (Para ingresar usuario) con sus atributos.
        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)

        #Creamos el QLabel (contraseña) con sus atributos.
        self.contraseña = QLabel(self)
        self.contraseña.setText("Contraseña: ")
        self.contraseña.setFont(QFont("Arial", 10))
        self.contraseña.move(20, 86)

        #Creamos el QLineEdit (Pra ingresar contraseña) con sus atributos.
        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(90, 82)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        #Creamos un campo para ver la contraseña ingresada.
        self.check_password = QCheckBox(self)
        self.check_password.setText("Ver contraseña")
        self.check_password.move(90,110)
        #self.check_password.clicked.connect(self.mostrar_contraseña) #<------------ si descomento esta linea no abre la ventana, es un error que corresponde a que ese clicked envia un valor booleano
                                                                                    #el cual debo pasar como parametro a la funcion que mostraria la contraseña, segun chatgp, es error de compatibilidad
                                                                                    #entre pyqt6 y la version de python, pero que el codigo deberia andar de perlas. :)

        #Creamos el boton de Loguearse con QPushButton.
        self.button_login = QPushButton(self)
        self.button_login.setText("Login")
        self.button_login.resize(320,30)
        self.button_login.move(20,140)
        self.button_login.clicked.connect(self.iniciar_sesion)
        
        #Creamos el boton de Registrarse con QPushButton.
        self.button_register = QPushButton(self)
        self.button_register.setText("Register")
        self.button_register.resize(320,30)
        self.button_register.move(20,180)
        self.button_register.clicked.connect(self.usuario_registrado)

    def mostrar_contraseña(self, checked):  # <- aceptar el parámetro
        if checked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
   
    def iniciar_sesion(self):
        self.mensaje_login = QMessageBox(self)
        self.mensaje_login.setText("Bienvenido")
        #Usamos exec() ya que este ejecuta la ventana del QMessageBox pero hasta no cerrarla, bloquea la ventana principal
        self.mensaje_login.exec()
       
    """
    def iniciar_registrarse(self):
        self.mensaje_register = QMessageBox()
        self.mensaje_register.setText("Gracias por Registrarte")
        #Usamos exec() ya que este ejecuta la ventana del QMessageBox pero hasta no cerrarla, bloquea la ventana principal
        self.mensaje_register.exec()
    """

    def usuario_registrado(self):
        print("Clic en botón Register")
        self.user_nuevo = Ventana_de_Usuario()
        self.user_nuevo.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())

