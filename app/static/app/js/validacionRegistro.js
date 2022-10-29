var nombre =document.getElementById('name');
var apellido =document.getElementById('apellido');
var comuna =document.getElementById('comuna');
var telefono =document.getElementById('telefono');
var email =document.getElementById('email');
var contraseña =document.getElementById('contraseña');
var error = document.getElementById('error');
error.style.color='red';


function btnregistro(){
    
    console.log("Registrado");

    var mensajeError =[];
    

    if(nombre.value === null || nombre.value ===""){
        mensajeError.push("Ingresa tu nombre");
    }
    if(apellido.value === null || apellido.value ===""){
        mensajeError.push("Ingresa tu apellido");
    }
    if(comuna.value === null || comuna.value ===""){
        mensajeError.push("Ingresa tu comuna");
    }
    if(telefono.value === null || telefono.value ===""){
        mensajeError.push("Ingrese su telefono");
    }
    if(contraseña.value === null || contraseña.value === ""){
        mensajeError.push("Ingrese su contraseña");
    }
    if(email.value === null || email.value === ""){
        mensajeError.push("Ingrese correctamente su correo");}
            
    error.innerHTML = mensajeError.join(" , ");

    return false
}





$(document).ready(function(){
    $('#form-nuevousuario').validate({
        debug: true,
        lang:'es',
        rules: {
            idNombreCompleto: {
                required: true,
                minlength: 5,
                maxlength: 10
            },
            idContraseña: "required",
            idReContraseña: {
                equalTo: "#idContraseña"
            }
        }
    });
});