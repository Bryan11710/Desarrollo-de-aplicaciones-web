const inputUrl = document.getElementById('imgUrl');
const btnAgregar = document.getElementById('btnAgregar');
const btnEliminar = document.getElementById('btnEliminar');
const gallery = document.getElementById('gallery');

// Esta variable es CLAVE: guardará la imagen que toquemos
let seleccionado = null;

// FUNCIÓN PARA AGREGAR
btnAgregar.addEventListener('click', () => {
    if (inputUrl.value === "") {
        alert("Pega una URL primero");
        return;
    }

    const img = document.createElement('img');
    img.src = inputUrl.value;
    
    // Al hacer clic en la imagen, la marcamos como seleccionada
    img.addEventListener('click', () => {
        // Si ya había una seleccionada, le quitamos el borde
        if (seleccionado) {
            seleccionado.classList.remove('seleccionada');
        }
        
        // La nueva imagen seleccionada es esta
        seleccionado = img;
        seleccionado.classList.add('seleccionada');
    });

    gallery.appendChild(img);
    inputUrl.value = ""; // Limpiar el cuadro de texto
});

// FUNCIÓN PARA ELIMINAR (Aquí estaba el fallo)
btnEliminar.addEventListener('click', () => {
    if (seleccionado) {
        // Eliminamos el elemento del DOM
        seleccionado.remove(); 
        // Limpiamos la variable para que no quede rastro
        seleccionado = null; 
    } else {
        alert("Por favor, haz clic en una imagen para seleccionarla antes de borrar.");
    }
});

// ATAJO DE TECLADO: Tecla Delete o Suprimir
document.addEventListener('keydown', (e) => {
    if (e.key === "Delete" || e.key === "Backspace") {
        if (seleccionado) {
            btnEliminar.click(); // Simula el clic en el botón de borrar
        }
    }
});