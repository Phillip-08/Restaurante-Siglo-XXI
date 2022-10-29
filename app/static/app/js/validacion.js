$(document).ready(function(){
    $('#form-nuevousuario').validate({
        debug: true,
        lang:'es',
        rules: {
            idNombreCompleto: {
                required: true,
                minlength: 5,
                maxlength: 20
            },
            idContraseña: "required",
            idReContraseña: {
                equalTo: "#idContraseña"
            }
        }
    });
});