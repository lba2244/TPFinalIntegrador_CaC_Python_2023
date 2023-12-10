function validarFormulario() {
    // Validar el nombre
    if (document.fvalida.nombre.value.length == 0) {
        alert("Tiene que escribir su Nombre")
        document.fvalida.nombre.focus()
        return 0;
    }
 // Validar el apellido
 if (document.fvalida.apellido.value.length == 0) {
    alert("Tiene que escribir su Apellido")
    document.fvalida.apellido.focus()
    return 0;
}

    
         //validar teléfono
 if (document.fvalida.telefono.value.length != 10){
    alert("El número de teléfono NO es válido")
    document.fvalida.telefono.focus()
    return 0;
}

 //validar mail
 var expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
 var esValido = expReg.test(document.fvalida.mail.value)
 if (esValido==false){
     alert ("Revise su mail no debe haber símbolos ni ñ")
     document.fvalida.mail.focus()
     return 0;
 }

  //valido cantidad de comensales
  if (document.fvalida.cant_comensales.selectedIndex <= 0){
    alert("Debemos saber cuántos comensales son, por favor indíquelo.")
    document.fvalida.cant_comensales.focus()
// document.fvalida.motivo.focus()
return 0;
}

 //valido motivo de reserva
 if (document.fvalida.motivoR.selectedIndex <= 0){
    alert("Por favor indique el motivo de la reunión.")
    document.fvalida.motivoR.focus()
// document.fvalida.motivo.focus()
return 0;
}

    // Validar fecha
    var today = new Date()
    today.setHours(0,0,0,0)
    var fechaFormul = new Date (document.fvalida.fecha_reserva.value)
    fechaFormul.setMinutes(fechaFormul.getMinutes() + fechaFormul.getTimezoneOffset())
    
    if (fechaFormul < today){
        alert("Fecha ingresada es incorrecta");
        document.fvalida.fecha_reserva.focus()
        return 0;
    }


    
//el formulario se envia
alert("Muchas gracias el formulario de reserva fue enviado");
document.fvalida.submit();
            
        
        
}

