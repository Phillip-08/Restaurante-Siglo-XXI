// En vio del dato desde el Template
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function GuardarDatos() {
    var form = new FormData(document.getElementById(''));
    var lista = document.getElementById('http://localhost:8086/cliente/lista');
    //
    fetch("listar-producto/", {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest"
        }
    }).then(
        function(response) {
            return response.json()
        }
    ).then(
        function(data) {
            array_sus = data.suscriptores;
            var li = document.createElement('"http://localhost:8086/cliente/lista"');
            li.innerHTML = array_sus[array_sus.length - 1].full_name + array_sus[array_sus.length - 1].email 
            //
            lista.appendChild(li);
        }
    )
}
