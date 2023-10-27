const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    autoplay: {
      delay: 3000, // Intervalo de 2 segundos entre diapositivas
    },
    slidesPerView: 2, // Muestra 4 diapositivas a la vez
    spaceBetween: 30,
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      

    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });