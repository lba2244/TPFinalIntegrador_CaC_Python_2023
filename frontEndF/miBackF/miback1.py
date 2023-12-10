#hago paso a paso mi OBJETO MSJ_CLIENTE
# Instalar con pip install mysql-connector-python
# Instalar con pip install mysql-connector-python
import mysql.connector

# No es necesario instalar, es parte del sistema standard de Python
import datetime

#--------------------------------------------------------------------

class Mensaje:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
        self.cursor.execute ('''CREATE TABLE IF NOT EXISTS pruebas(
            id int (15) NOT NULL AUTO_INCREMENT,
            nombre varchar(100) NOT NULL,
            apellido varchar(45) NOT NULL,
            telefono varchar(15) NOT NULL,
            email varchar(60) NOT NULL,
            cant_comensales decimal(9,0) NOT NULL,
            motivoR varchar(45) NOT NULL,
            primera_visita varchar(5),
            fecha_reserva datetime NOT NULL,
            mensaje varchar(500) NOT NULL,                           
            gestion varchar(200) DEFAULT NULL,
            fecha_gestion datetime DEFAULT NULL,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
            ''')
        self.conn.commit()
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
#confirmo la creacion siempre  commit() en Phyton es necesario
    #----------------------------------------------------------------
    def enviar_reserva(self,nombre,apellido,telefono,email,cant_comensales,motivoR,primera_visita,fecha_reserva,mensaje,gestion):
        sql = "INSERT INTO pruebas (nombre, apellido, telefono, email,cant_comensales,motivoR,primera_visita,fecha_reserva, mensaje,gestion, fecha_gestion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
        fecha_gestion = datetime.datetime.now()
       # INSERT INTO pruebass() VALUES ("Juan", "Perez", "1234567890", "juan@gmail.com", "4","cumpleanios","si", "2023-12-15 09:03","Este es un mensaje de prueba","dandolo todo para q ande", "2023-12-13 19:03")
        valores = (nombre, apellido, telefono, email,cant_comensales,motivoR,primera_visita,fecha_reserva, mensaje,gestion, fecha_gestion)
        self.cursor.execute(sql,valores)        
        self.conn.commit()
        self.cursor.close()
        return True
       
  #----------------------------------------------------------------
    def listar_reservas(self):
        self.cursor.execute("SELECT * FROM pruebas")
        reserva = self.cursor.fetchall()
        return reserva
 #----------------------------------------------------------------
    def responder_reserva(self, id, gestion):
        fecha_gestion = datetime.datetime.now()
        sql = "UPDATE pruebas SET gestion = %s, fecha_gestion = %s WHERE id = %s"
        valores = (gestion, fecha_gestion, id)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

#----------------------------------------------------------------
    def mostrar_reserva(self, id):
         sql = f"SELECT id, nombre, apellido, telefono, email,cant_comensales,motivoR,primera_visita,fecha_reserva, mensaje,gestion, fecha_gestion FROM pruebas WHERE id = {id}"
         self.cursor.execute(sql)
         return self.cursor.fetchone()

#----------------------------------------------------------------
    def eliminar_reserva(self, id):
        self.cursor.execute(f"DELETE FROM pruebas WHERE id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

#----------------------------------------------------------------
#----------------------------------------------------------------
prueba= Mensaje("localhost", "root","root","pruebas")  #mensaje puede ser reserva
#----------------------------------------------------------------
#     Prueba de c/u de las funciones de mi calse andan todas ok
#----------------------------------------------------------------
#prueba.enviar_reserva("ana","analitics","0982222321", "anao@mail.com","2","laboral","no", "2023-12-11","mensaje del 6 dic","siue andando??")
#prueba.enviar_reserva("juan","perez","1234567890", "juan@mail.com","4","aniversario","si", "2023-12-09","Mensaje de prueba","Anduvo!!")
#prueba.enviar_reserva("sara","lepes","15555524321", "sara@email.com","3","cumpleaños","no", "2023-12-02","menu vegetariano","sigue funcionando !!")

#prueba=prueba.eliminar_reserva(7)
#reserva= prueba.listar_reservas()

#if prueba.responder_reserva(10, "responde si anda "):
# print("Se modificó el mensaje indicado")
#else:
#print("No se modificó ningún registro")

#id = int(input("Ingrese id de la reserva que quiere ver: "))
#respuesta = prueba.mostrar_reserva(id)
#print(respuesta)     

#---------------------------------------------------------------
#prueba.enviar_reserva("Matias", "Seminara", "123456789", "matiasseminara@gmail.com", "6","cumpleaños","si", "2023-12-02","Esta consulta es para ver la conexion a la base de datos","sigue funcionando !!")
#prueba = prueba.listar_reservas()
#print(prueba.responder_reserva(1, "Ya le contesté nuevamente el regreso"))
#print(prueba.eliminar_reserva(1))
#print(prueba.mostrar_reserva(2))

