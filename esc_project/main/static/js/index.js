console.log("El archivo JavaScript se ha cargado correctamente.");

const menuButton = document.querySelector(".menu-button");
const menu = document.querySelector(".menu");

// Agrega un manejador de eventos al botón
menuButton.addEventListener("click", function() {
    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
});

