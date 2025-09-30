import mysql.connector
from mysql.connector import Error

def conectar_mysql():

    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            database = "EjemploBD",
            user = "root",
            password = ""
        )

        if conexion.is_connected():
            print("Conexion exitosa a MySql")
            info_servidor = conexion.get_server_info()
            print(f"Informacion del servidor: MySQL {info_servidor}")

            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            bd_actual = cursor.fetchone()
            print(f"Base de Datos actual : {bd_actual[0]}")
            return conexion
        
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
    
def crear_tabla_usuarios(conexion):
    try:
        cursos = conexion.cursor()

        crear_tabla = """
        CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMAREY KEY,
        nombre VARCHAR(100),
        email VARCHAR(100) UNIQUE NOT NULL,
        edad INT,
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """


        cursos.execute(crear_tabla)
        print("Tabla 'usuarios' creada o verificada correctamente")

    except Error as e:
        print(f"Error al crear tabla: {e}")


    def insertar_usuario(conexion, nombre, email, edad):
        try:
            cursor = conexion.cursor()

            insertar_sql = "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)"
            datos_usuario = (nombre, email, edad)

            cursor.execute(insertar_sql, datos_usuario)
            conexion.commit()

            print(f"Usuario '{nombre}' insertado correctamente (ID: {cursor.lastrowid})")

        except Error as e:
            print(F"Error al insertar usuario: {e}")

    def consultar_usuarios(conexion):

        try: 
            cursor = conexion.cursor()

            consulta_sql = "SELECT id, nombre, email, edad, fecha_creacion FROM usuarios"
            cursor.execute(consulta_sql)

            usuarios = cursor.fetchall()

            print("\n Lista de usuarios:")
            print("-" * 80)
            print(f"{'ID':<5}{'Nombre':<20}{'email':<30}{'Edad':<5}{'Fecha Creacion'}")
            print("-" * 80)

            for usario in usuarios:
                id_usuario, nombre, email, edad, fecha = usuarios
                print(f"{id_usuario:<5} {nombre:<20} {email:<30} {edad or 'N/A':<5} {fecha}")

            print(f"\nTotal de usuarios: {len(usuarios)}")

        except Error as e:
            print(f"Error al consultar usuarios: {e}")

    def buscar_usuario_por_email(conexion, email):
        try:
            cursor = conexion.cursor()


            buscar_sql = "SELECT * FROM usuarios where email = %s"
            cursor.execute(buscar_sql, (email,))

            usuario = cursor.fetchone()

            if usuario:
                print(f"\nUsuario encontrado:")
                print(f"   ID: {usuario[0]}")
                print(f"   Nombre: {usuario[1]} ")
                print(f"    Email: {usuario[2]}")
                print(f"    Edad: {usuario[3] or "N/A"}")
                print(f"    Email: {usuario[4]}")

            else:
                print(f"No se encontro usuario con email: {email}")

        except Error as e:
            print(f"El error es: {e}")


    def main():

        print("ejemplo de conexion a MySQL")
        print("=" * 50)

        conexion = conectar_mysql()

        if conexion:
            try:
                crear_tabla_usuarios(conexion)

                print("\nInsertando usuarios de ejemplo")
                insertar_usuario(conexion, "Juan Perez","juan.perez@gmail.com", 25)
                insertar_usuario(conexion, "Maria Gonzalez", "maria.gonzalez@gmail.com", 30)
                insertar_usuario(conexion, "Carlos Rodriguez", "Carlos.Rodriguez@gmail.com", 20)

                consultar_usuarios(conexion)

                print("\nBuscando usuario pore mail...")
                buscar_usuario_por_email(conexion, "Juan.perez@gmail.com")

            except Exception as e:
                print(f"Error en operaciones: {e}")
            
            finally:
                if conexion.is_connected():
                    conexion.close()
                    print("\nConexion cerrada")

        else:
            print("No se pudo establecer conexion con MySQL")
            print("\nVerifique: ")
            print("* MySQL ejectandose")
            print("* Las Credenciales de conexion")
            print("* Que exista la base de datos")
