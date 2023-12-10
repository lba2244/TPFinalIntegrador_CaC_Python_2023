#mi PRIMER BACKEND a partir de aca voy a crear un OBJRTO MSJ, adentro
# va a tener un método q me permita conectar con mi BD (usando PYTHON Ovbio!!4265)
import datetime
import random
mensajes = []

#Funciones 
def enviar_mensaje(nombre, apellido, telefono, email, comensales,motivoR,mensaje):
    mensaje = {}
    mensaje["id"] = random.randint(1000, 9999)
    mensaje["nombre"] = nombre
    mensaje["apellido"] = apellido
    mensaje["telefono"] = telefono
    mensaje["email"] = email
    mensaje["comensales"] = comensales
    mensaje["motivoR"] = motivoR
    mensaje["fecha_reserva"] = datetime.datetime.now()
    mensaje["mensaje"] = mensaje
    mensajes.append(mensaje)

def leer_mensajes():
    # Consultar a la base de datos todos los mensajes
    for mensaje in mensajes:
        print(mensaje)
        print("-" * 10)

def responder_mensaje(id, gestion):
    for mensaje in mensajes:
        if mensaje["id"] == int(id):
            mensaje["leido"] = 1
            mensaje["gestion"] = gestion
            mensaje["fecha_gestion"] = datetime.datetime.now()
            break

def eliminar_mensaje(id):
    for x in range(0, len(mensajes)):
        if mensajes[x]["id"] == int(id):
            mensajes.pop(x)
            break

#Invocaciones
enviar_mensaje("Juan", "Perez", "223545487", "juanperez@gmail.com","2 a 4","Laboral","Necesito mas informacion sobre las ofertas")
enviar_mensaje("luis", "recondo","1123543246","lucho@mail.com","0 a 2","Aniversario","por favor envíe precios")
               
leer_mensajes()

id = input("Ingrese el id: ")
gestion = input("Gestión: ")
responder_mensaje(id, gestion)
print("*" * 40)

id_borrar = input("Que mensaje desea eliminar?: ")
eliminar_mensaje(id_borrar)
print("*" * 40)
leer_mensajes()