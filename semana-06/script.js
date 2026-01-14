const formulario = document.getElementById('registroForm');
const btnSubmit = document.getElementById('btnSubmit');

const campos = {
    nombre: document.getElementById('nombre'),
    email: document.getElementById('email'),
    password: document.getElementById('password'),
    confirmPassword: document.getElementById('confirmPassword'),
    edad: document.getElementById('edad')
};

// Expresiones regulares
const patrones = {
    email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    // Al menos 8 caracteres, un número y un carácter especial
    password: /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/
};

const validarCampo = (input, condicion, errorId, mensaje) => {
    const errorSpan = document.getElementById(errorId);
    if (condicion) {
        input.classList.add('valid');
        input.classList.remove('invalid');
        errorSpan.textContent = "";
        return true;
    } else {
        input.classList.add('invalid');
        input.classList.remove('valid');
        errorSpan.textContent = mensaje;
        return false;
    }
};

const validarTodo = () => {
    const esNombreValido = validarCampo(campos.nombre, campos.nombre.value.trim().length >= 3, 'error-nombre', 'Mínimo 3 caracteres.');
    
    const esEmailValido = validarCampo(campos.email, patrones.email.test(campos.email.value), 'error-email', 'Correo no válido.');
    
    const esPassValido = validarCampo(campos.password, patrones.password.test(campos.password.value), 'error-password', '8+ caracteres, 1 número y 1 símbolo.');
    
    const esConfirmValido = validarCampo(campos.confirmPassword, (campos.confirmPassword.value === campos.password.value && campos.confirmPassword.value !== ""), 'error-confirm', 'Las contraseñas no coinciden.');
    
    const esEdadValida = validarCampo(campos.edad, parseInt(campos.edad.value) >= 18, 'error-edad', 'Debes ser mayor de 18 años.');

    // Habilitar botón solo si todo es true
    btnSubmit.disabled = !(esNombreValido && esEmailValido && esPassValido && esConfirmValido && esEdadValida);
};

// Listeners para validación en tiempo real
Object.values(campos).forEach(input => {
    input.addEventListener('input', validarTodo);
});

// Al enviar
formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('¡Registro validado y enviado con éxito!');
});

// Al reiniciar
formulario.addEventListener('reset', () => {
    setTimeout(() => {
        Object.values(campos).forEach(input => {
            input.classList.remove('valid', 'invalid');
        });
        document.querySelectorAll('.error-msg').forEach(msg => msg.textContent = "");
        btnSubmit.disabled = true;
    }, 10);
});