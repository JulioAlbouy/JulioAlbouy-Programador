import sys 
from PyQt6.QtWidgets import (QApplication,  QWidget, QPushButton, QGridLayout,QTextEdit)
from PyQt6.QtGui import QTextCursor
import funciones_calculadora1


class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_UI()
    
    def inicializar_UI(self):
        self.setGeometry(100,100,550,250)
        self.setWindowTitle('Calculadora')
        self.generar_interfaz()
        self.show()

    def generar_interfaz(self):
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)#Impide interactuar con la pantalla, solo con los botones
        
        #Botones numericos
        self.boton_1 = QPushButton('1')
        self.boton_1.clicked.connect(self.ingresar_numero)

        self.boton_2 = QPushButton('2')
        self.boton_2.clicked.connect(self.ingresar_numero)

        self.boton_3 = QPushButton('3')
        self.boton_3.clicked.connect(self.ingresar_numero)

        self.boton_4 = QPushButton('4')
        self.boton_4.clicked.connect(self.ingresar_numero)

        self.boton_5 = QPushButton('5')
        self.boton_5.clicked.connect(self.ingresar_numero)

        self.boton_6 = QPushButton('6')
        self.boton_6.clicked.connect(self.ingresar_numero)

        self.boton_7 = QPushButton('7')
        self.boton_7.clicked.connect(self.ingresar_numero)

        self.boton_8 = QPushButton('8')
        self.boton_8.clicked.connect(self.ingresar_numero)
        
        self.boton_9 = QPushButton('9')
        self.boton_9.clicked.connect(self.ingresar_numero)
        
        self.boton_0 = QPushButton('0')
        self.boton_0.clicked.connect(self.ingresar_numero)

        self.boton_00 = QPushButton('00')
        self.boton_00.clicked.connect(self.ingresar_numero)
        self.boton_punto = QPushButton('.')
        self.boton_punto.clicked.connect(self.ingresar_numero)
        #Botones de operaciones
        self.boton_suma = QPushButton('+')
        self.boton_suma.clicked.connect(self.ingresar_numero)
        self.boton_resta = QPushButton('-')
        self.boton_resta.clicked.connect(self.ingresar_numero)
        self.boton_multiplicacion = QPushButton('*')
        self.boton_multiplicacion.clicked.connect(self.ingresar_numero)
        self.boton_division = QPushButton('/')
        self.boton_division.clicked.connect(self.ingresar_numero)  
        
        #Botones de interaccion
        self.boton_ce = QPushButton('CE')
        self.boton_ce.clicked.connect(self.borrar)
        self.boton_borrar = QPushButton('<-')
        self.boton_borrar.clicked.connect(self.borrar_ultimo_caracter)
        self.boton_igual = QPushButton('=')
        self.boton_igual.clicked.connect(self.mostrar_resultado)

        self.layout_principal = QGridLayout()
        self.layout_principal.addWidget(self.pantalla,0,0,2,4) #Inicia en 0,0, y se expande 2 para abajo y 4 a la derecha
        self.layout_principal.addWidget(self.boton_ce,2,0,1,2)
        
        self.layout_principal.addWidget(self.boton_borrar,2,2)
        self.layout_principal.addWidget(self.boton_suma,2,3)
        
        self.layout_principal.addWidget(self.boton_7,3,0)
        
        self.layout_principal.addWidget(self.boton_8,3,1)
        
        self.layout_principal.addWidget(self.boton_9,3,2)
        self.layout_principal.addWidget(self.boton_division,3,3)
        
        self.layout_principal.addWidget(self.boton_4,4,0)
        self.layout_principal.addWidget(self.boton_5,4,1)
        self.layout_principal.addWidget(self.boton_6,4,2)
        self.layout_principal.addWidget(self.boton_multiplicacion,4,3)

        self.layout_principal.addWidget(self.boton_1,5,0)
        self.layout_principal.addWidget(self.boton_2,5,1)
        self.layout_principal.addWidget(self.boton_3,5,2)
        self.layout_principal.addWidget(self.boton_resta,5,3)

        self.layout_principal.addWidget(self.boton_0, 6,0)
        self.layout_principal.addWidget(self.boton_00, 6,1)
        self.layout_principal.addWidget(self.boton_punto, 6,2)
        self.layout_principal.addWidget(self.boton_igual, 6,3)

        self.setLayout(self.layout_principal)

    def ingresar_numero(self):
        boton = self.sender()  #Obtenemos la señal del boton que fue presionado
        caracter = boton.text() #Alojamos en la variable caracter, el texto del boton el cual fue presionado
        self.pantalla.insertPlainText(caracter) #Agregamos al QtextEdit el caracter obtenido del boton que fue presionado
    
    def borrar(self):
        self.pantalla.clear() #Limpiar la pantalla de la calculadora con el boton CE

    def borrar_ultimo_caracter(self):
        texto_actual = self.pantalla.toPlainText() #Obtenemos todo el texto en cadena de la pantalla
        if texto_actual: #si existe texto...
            nuevo_texto = texto_actual[:-1] #borra el ultimo caracter obtenido y lo guarda en una nueva variable
            self.pantalla.setPlainText(nuevo_texto) #Añanadimos esta nueva variable a la pantalla ("Refrescamos la pantalla")
            self.pantalla.moveCursor(QTextCursor.MoveOperation.End) #"Movemos el cursor de la pantalla al final de la lista de caracteres que se volvio a imprimir en la misma"
    
    def evaluar_operacion(self):
        texto_actual = self.pantalla.toPlainText() #Obtenemos el texto de la pantalla de la calculadora
        signos = ["+", "-", "*", "/"]
        for signo in signos: #Recorremos la lista de signos y evaluamos...
            if signo in texto_actual: #Si existe alguno de los signos de la lista, en el str extraido de la pantalla de la calculadora...
                partes = texto_actual.split(signo) #Dividimos el str en el signo encontrado con el metodo .split(). Esto nos devuelve una lista "partes" con la cadena de caracteres separada
                self.operador = signo #Asignamos el signo encontrado a una propiedad para luego utilizarlo
                if len(partes) == 2: #Si la longitud de la lista es de 2 partes. (Ya que la calculadora solo opera con 2 numeros)
                    self.num1 = partes[0].strip()
                    self.num2 = partes[1].strip() #Alojamos cada parte de la lista, es decir cada indice, en una variable independiente para ya obtener los dos nuemeros
        
    def aplicar_operacion(self):
        self.num1 = float(self.num1) #Convertimos los numero extraidos en floats para poder operar con ellos
        self.num2 = float(self.num2) 
        if self.operador == '+':
            return self.num1 + self.num2
        elif self.operador == '-':
            return self.num1 - self.num2
        elif self.operador == '*':
            return self.num1 * self.num2
        elif self.operador == '/':
            if self.num2 == 0:
                return "Error: división por cero"
            return self.num1 / self.num2
            #Retornamos el resultado de las operaciones

    def mostrar_resultado(self):
        self.evaluar_operacion() #Evaluamos el str ingresado llamando la funcion evaluar_operacion()
        resultado = self.aplicar_operacion() #Realizamos la operacion correspondiente
        resultado = str(resultado) #Convertimos el resultado a string para poder volver a mostrarlo en la pantalla de la calculadora, ya que esta no muestra otro tipo de dato
        self.pantalla.setText(resultado) #Agregamos el resultado a la pantalla



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculadora = Calculadora()
    sys.exit(app.exec())
