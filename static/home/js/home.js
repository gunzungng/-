$(function () {
    $('.home').width(innerWidth);

    var swiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        paginationClickable: true,
        spaceBetween: 10,
        centeredSlides: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false,
        loop:true
    });

        new Swiper('#mustbuySwiper', {
        spaceBetween: 10,
        slidesPerView:3,
        loop:true

    });
})

