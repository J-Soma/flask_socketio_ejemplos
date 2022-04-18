socket = io()

document.querySelector("form").onsubmit = () =>
{
    nombre = document.querySelector("#nombre").value
    socket.emit("saludar", nombre)

    return false;
}