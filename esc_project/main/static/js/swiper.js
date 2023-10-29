var swiper;

function initSwiper() {
  if (window.innerWidth < 768) {
    // Configuración para dispositivos móviles
    if (swiper) {
      swiper.destroy(); // Destruye la instancia anterior de Swiper
    }

    swiper = new Swiper(".mySwiper", {
      loop: true,
      slidesPerView: 1, // Número de diapositivas visibles a la vez en dispositivos móviles
      spaceBetween: 20,
      autoplay: {
        delay: 3000,
        pauseOnMouseEnter: false,
        disableOnInteraction: false,
        reverseDirection: false,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      pagination: {
        el: ".swiper-pagination",
      },
      scrollbar: {
        el: ".swiper-scrollbar",
        hide: true,
      },
    });
  } else {
    // Configuración para PC
    if (swiper) {
      swiper.destroy(); // Destruye la instancia anterior de Swiper
    }

    swiper = new Swiper(".mySwiper", {
      loop: true,
      slidesPerView: 3, // Número de diapositivas visibles a la vez en PC
      spaceBetween: 20,
      autoplay: {
        delay: 3000,
        pauseOnMouseEnter: false,
        disableOnInteraction: false,
        reverseDirection: false,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      pagination: {
        el: ".swiper-pagination",
      },
      scrollbar: {
        el: ".swiper-scrollbar",
        hide: true,
      },
    });
  }
}

// Inicializa Swiper al cargar la página
initSwiper();

// Vuelve a inicializar Swiper cuando cambia el tamaño de la ventana
window.addEventListener("resize", initSwiper);