// 1. Equipos que aparecen al inicio
const equipos = [
    { nombre: "Manchester City", titulos: 8, estadio: "Etihad Stadium" },
    { nombre: "Liverpool FC", titulos: 19, estadio: "Anfield" },
    { nombre: "Arsenal FC", titulos: 13, estadio: "Emirates Stadium" }
];

// 2. Banco de datos de la Premier para "fichar"
const mercadoFichajes = [
    { nombre: "Manchester United", titulos: 20, estadio: "Old Trafford" },
    { nombre: "Chelsea FC", titulos: 6, estadio: "Stamford Bridge" },
    { nombre: "Tottenham Hotspur", titulos: 2, estadio: "Tottenham Hotspur Stadium" },
    { nombre: "Aston Villa", titulos: 7, estadio: "Villa Park" },
    { nombre: "Newcastle United", titulos: 4, estadio: "St. James' Park" }
];

const listaUl = document.getElementById('lista-equipos');
const boton = document.getElementById('btn-agregar');

// 3. Función para renderizar
function mostrarEquipos() {
    listaUl.innerHTML = "";

    equipos.forEach(equipo => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>${equipo.nombre}</strong> 
            <br>🏆 Títulos de Liga: ${equipo.titulos} 
            <br>🏟️ Sede: ${equipo.estadio}
        `;
        listaUl.appendChild(li);
    });
}

// 4. Lógica para "Fichar" un equipo de la Premier
boton.addEventListener('click', () => {
    if (mercadoFichajes.length > 0) {
        // Sacamos un equipo al azar del mercado
        const indiceAleatorio = Math.floor(Math.random() * mercadoFichajes.length);
        const equipoFichado = mercadoFichajes.splice(indiceAleatorio, 1)[0];

        // Lo añadimos a nuestra lista principal
        equipos.push(equipoFichado);
        mostrarEquipos();
    } else {
        boton.innerText = "❌ Mercado Cerrado";
        boton.style.background = "#333";
        boton.disabled = true;
    }
});

// Render inicial
mostrarEquipos();