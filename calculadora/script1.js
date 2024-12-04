/*function variables(){

    let nombre = "Leonardo" 
    const edad = 15 
    var esEstudiante = true


    var nuevaEdad = edad + 5
    let mensaje = "Hola " + nombre
    alert(mensaje)
    alert("Tu edad dentro de cinco años sera :")
    alert(nuevaEdad)
}*/

function realizarSuma() {
    const numero1 = parseFloat(document.getElementById('numero1').value);
    const numero2 = parseFloat(document.getElementById('numero2').value);

    if (isNaN(numero1) || isNaN(numero2)) {
        alert('Por favor, ingresa valores numéricos válidos.');
        return;
    }

    const suma = numero1 + numero2;

    document.getElementById('resultado').value = suma;
}

function realizarResta() {
    const numero1 = parseFloat(document.getElementById('numero1').value);
    const numero2 = parseFloat(document.getElementById('numero2').value);

    if (isNaN(numero1) || isNaN(numero2)) {
        alert('Por favor, ingresa valores numéricos válidos.');
        return;
    }

    const suma = numero1 - numero2;

    document.getElementById('resultado').value = suma;
}

function realizarMultilicacion() {
    const numero1 = parseFloat(document.getElementById('numero1').value);
    const numero2 = parseFloat(document.getElementById('numero2').value);

    if (isNaN(numero1) || isNaN(numero2)) {
        alert('Por favor, ingresa valores numéricos válidos.');
        return;
    }

    const suma = numero1 * numero2;

    document.getElementById('resultado').value = suma;
}

function realizarDivision() {
    const numero1 = parseFloat(document.getElementById('numero1').value);
    const numero2 = parseFloat(document.getElementById('numero2').value);

    if (isNaN(numero1) || isNaN(numero2)) {
        alert('Por favor, ingresa valores numéricos válidos.');
        return;
    }

    const suma = numero1 / numero2;

    document.getElementById('resultado').value = suma;
}

function limpiarCampos() {
    document.getElementById('numero1').value = '';
    document.getElementById('numero2').value = '';
    document.getElementById('resultado').value = '';
}

/*function calcIVA(){
    const valPr = parseInt(prompt("Ingrese el valor de su producto"))
    const iva = 0.19

    let totalIva = valPr * iva
    alert("Su iva es de:" +  totalIva)
}*/

