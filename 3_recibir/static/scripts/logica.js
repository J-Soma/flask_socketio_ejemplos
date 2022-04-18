socket = io()

document.querySelector("form").onsubmit = () =>
{
    nombre = document.querySelector("#nombre").value

    socket.emit("saludar", nombre, (respuesta) => {
        document.querySelector("#contenido").append(respuesta)
        document.querySelector("#contenido").innerHTML += ("<br>")
    })

    return false;
}