function registro(){
    let comprovacion = document.querySelector("#email").value
    if (comprovacion == "") return
    else {
    let boolean = confirm("seguro que quiere proceder")
    if (boolean) alert("su solicitud a sido enviada con exito, pronto recivira un mail con el resultado de su peticion")
    else alert("su peticion a sido cancelada")
}}