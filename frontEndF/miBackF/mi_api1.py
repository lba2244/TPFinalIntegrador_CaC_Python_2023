#--------------------------------------------------------------------
# Instalé con pip install Flask , okk logrado
from flask import Flask, request, jsonify
#from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS


# Instalar con pip install mysql-connector-python
import mysql.connector
# No es necesario instalar, es parte del sistema standard de Python
import os
import time, datetime
#---------------------------------------------------------------
# Codigo en Python de Peticiones HTTP probadas y andando
#----------------------------------------------------------------
app = Flask(__name__)

# Permitir acceso desde cualquier origen externo
CORS(app, resources={r"/*": {"origins": "*"}}) 

class Reserva:
#----------A partir de acá mi clase Reserva ----------------------

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
        self.cursor.execute ('''CREATE TABLE IF NOT EXISTS reservas(
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
    def enviar_reserva(self,nombre,apellido,telefono,email,cant_comensales,motivoR,primera_visita,fecha_reserva,mensaje):
        sql = "INSERT INTO reservas (nombre, apellido, telefono, email,cant_comensales,motivoR,primera_visita,fecha_reserva, mensaje,fecha_gestion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
        fecha_gestion = datetime.datetime.now()
       # INSERT INTO pruebass() VALUES ("Juan", "Perez", "1234567890", "juan@gmail.com", "4","cumpleanios","si", "2023-12-15 09:03","Este es un mensaje de prueba","dandolo todo para q ande", "2023-12-13 19:03")
        valores = (nombre, apellido, telefono, email,cant_comensales,motivoR,primera_visita,fecha_reserva, mensaje,fecha_gestion)
        self.cursor.execute(sql,valores)        
        self.conn.commit()
        self.cursor.close()
        return True
       
  #----------------------------------------------------------------
    def listar_reservas(self):
        self.cursor.execute("SELECT * FROM reservas")
        reserva = self.cursor.fetchall()
        return reserva
 #----------------------------------------------------------------
    def responder_reserva(self, id, gestion):
        fecha_gestion = datetime.datetime.now()
        sql = "UPDATE reservas SET gestion = %s, fecha_gestion = %s WHERE id = %s"
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
        self.cursor.execute(f"DELETE FROM reservas WHERE id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

#----------------------------------------------------------------
#  mi objeto llamado prueba
#----------------------------------------------------------------
prueba= Reserva(host="tpfCac2023.mysql.pythonanywhere-services.com",user= "tpfCac2023",password="comision23501",database="tpfCac2023$reservas") 
#----------------------------------------------------------------

@app.route("/reservas", methods=["GET"]) 
def listar_reservas():
    reserva= prueba.listar_reservas()
    return jsonify(reserva)
#---------------------------------------------------------------

@app.route("/reservas", methods=["POST"])
def agregar_reserva():
    #Recojo los datos del form
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    email = request.form['mail']
    cant_comensales = request.form['cant_comensales']
    motivoR = request.form['motivoR']
    primera_visita = request.form['primera_visita']
    fecha_reserva = request.form['fecha_reserva']
    mensaje = request.form['mensaje']
    
 
 
    if prueba.enviar_reserva(nombre, apellido, telefono, email,cant_comensales,motivoR,primera_visita,fecha_reserva,mensaje):
        return jsonify({"mensaje": "Reserva agregada"}), 201
    else:
        return jsonify({"mensaje": "No fue posible registrar la reserva"}), 400
  

#--------------------------------------------------------------------
@app.route("/reservas/<int:id>", methods=["PUT"])
def responder_reserva(id):
    #Recojo los datos del form
    gestion = request.form.get("gestion")
    
    if prueba.responder_reserva(id, gestion):
        return jsonify({"mensaje": "Mensaje modificado"}), 200
    else:
        return jsonify({"mensaje": "Mensaje no encontrado"}), 403


#---------------------------------------------------------------
# cerrando el codigo de  mi app
#---------------------------------------------------------------

if __name__ == "__main__":
     app.run(debug=True)
#----------------------------------------------------------------
