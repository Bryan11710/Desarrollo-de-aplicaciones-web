// Alerta del botón
document.getElementById("miBoton").onclick = function() {
    alert("¡Hola! Esta es una alerta de prueba.");
};

// Validación del formulario
const formulario = document.getElementById("miFormulario");

formulario.onsubmit = function(event) {
    const nombre = document.getElementById("nombre").value;
    const correo = document.getElementById("correo").value;
    const mensaje = document.getElementById("mensaje").value;

    if (nombre === "" || correo === "" || mensaje === "") {
        event.preventDefault(); // Detiene el envío
        alert("Por favor, llena todos los campos.");
    } else {
        alert("¡Gracias por escribirnos!");
    }
};