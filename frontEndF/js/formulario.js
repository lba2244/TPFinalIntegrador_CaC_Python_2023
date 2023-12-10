
    function validarFormulario() {
        //valido el nombre
        if (document.fvalida.name.value.length == 0) {
            alert("El campo Nombre es Obligatorio")
            document.fvalida.name.focus()
            return 0;
        }

     
         //valido la apellido. 
            apellido = document.fvalida.surname.value
           
                if (apellido == "") {
                alert("El campo Apellido es Obligatorio")
                document.fvalida.surname.focus()
                return 0;
            
            }

            //valido el celular.
            celular = document.fvalida.telephone.value
                if (celular="") {
                alert("Tiene que introducir un número de telefono para poder contactarlo.")
                document.fvalida.telephone.focus()
                return 0;
            } 
            
            //valido el Mail.
            correo= document.fvalida.mail.value
                if (correo == "") {
                alert("Tiene que introducir un mail de contacto.")
                document.fvalida.correo.focus()
                return 0;
            } 
            
            //valido cantidad de comensales
            if (document.fvalida.cantidad.selectedIndex == 0) {
                alert("Debemos saber cuántos comensales son, por favor indíquelo.")
                document.fvalida.motivo.focus()
                return 0;
            }

 //Validar fecha

/*/ /REVISAR FALIDACIÓN FECHA
    var today = new Date()
    today.setHours(0,0,0,0)
    var fechaForm = new Date (document.fvalida.Fecha.value)
    fechaForm.setMinutes(fechaForm.getMinutes() + fechaForm.getTimezoneOffset())
    
    if (fechaForm < today){
        alert("Fecha ingresada es incorrecta");
        document.fvalida.Fecha.focus()
        return 0;
        }
*/

         //valido motivo de la reserva
            if (document.fvalida.motivo.selectedIndex == 0) {
                alert("Debemos conocer el motivo de la reserva para atenderlo mejor.")
                document.fvalida.motivo.focus()
                return 0;
            }


//el formulario se envia
alert("Muchas gracias por completar y enviar el formulario");
document.fvalida.submit();
            
        }
        

      