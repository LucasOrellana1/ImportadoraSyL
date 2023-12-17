
const menuButton = document.querySelector(".menu-button");
const menu = document.querySelector(".menu");

// Agrega un manejador de eventos al botón
menuButton.addEventListener("click", function() {
    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "block";
       
        menu.style.opacity = '1';
       

        menu.style.transition = "opacity 1s ease"
    } else {
        menu.style.display = "none";
    }
});

document.addEventListener("DOMContentLoaded", function () {
    // Obtén una lista de todos los elementos h1 en la página
    if (window.innerWidth < 768) {
        var h1Elements = document.querySelectorAll("h1");

        // Define el nuevo tamaño de fuente que deseas aplicar (por ejemplo, 24px)
        var nuevoTamañoDeFuente = "3rem";

        // Itera a través de la lista de elementos h1 y cambia el tamaño de fuente
        for (var i = 0; i < h1Elements.length; i++) {
        h1Elements[i].style.fontSize = nuevoTamañoDeFuente;
        }
    
    }
    else{
        var h1Elements = document.querySelectorAll("h1");

        // Define el nuevo tamaño de fuente que deseas aplicar (por ejemplo, 24px)
        var nuevoTamañoDeFuente = "3.5rem";

        // Itera a través de la lista de elementos h1 y cambia el tamaño de fuente
        for (var i = 0; i < h1Elements.length; i++) {
        h1Elements[i].style.fontSize = nuevoTamañoDeFuente;
    }
}});

//Filtro de productos:
