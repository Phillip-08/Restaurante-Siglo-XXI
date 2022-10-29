function validarEmail(email) {
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/.test(email)){
            mensajeError.push("La dirección de email " + valor + " es correcta.");
            return false
        } else {
            mensajeError.push("La dirección de email es incorrecta.");
            return false
        }
      }
      