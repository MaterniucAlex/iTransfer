document.addEventListener('DOMContentLoaded', function () {
    var courseSwiper = new Swiper('.course-slider', {
      slidesPerView: 1,      
      spaceBetween: 30,     
      loop: true,           
      autoHeight: true,      // Ajustează înălțimea automat
      autoplay: {
        delay: 8000,         
        disableOnInteraction: true,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
  });