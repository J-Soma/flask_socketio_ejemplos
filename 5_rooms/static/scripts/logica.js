socket = io()

document.querySelector("#boton1").onclick = () => {
    socket.emit("entrar", "CS50x.ni", (respuesta) => {
        document.querySelector("#contenido").append(respuesta)
        document.querySelector("#contenido").innerHTML += "<br>"
    })
}

document.querySelector('#boton2').onclick = () => {
    socket.emit("entrar", "Web50x.ni", (respuesta) => {
        document.querySelector("#contenido").append(respuesta)
        document.querySelector("#contenido").innerHTML += "<br>"
    })
}

socket.on("mensaje", (dato) => {
    document.querySelector("#contenido").append(dato)
    document.querySelector("#contenido").innerHTML += "<br>"
})