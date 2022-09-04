$( document ).ready(function() {
    var w = window.innerWidth;

    if(w > 991){
        $('#fix-head').scrollToFixed();
    }



})


$(document).ready(function(){
    $('.listing-row').slick({
        slidesToShow: 4,
        slidesPerRow: 1,
        infinite: true,
        responsive: [{
                breakpoint: 1024,
                settings: {
                  slidesToShow: 3,
                  infinite: true
                }

              }, {
                breakpoint: 600,
                settings: {
                  slidesToShow: 2,
                 infinite: true
                  //dots: true
                }

              }, {
                breakpoint: 300,
                settings: "unslick" // destroys slick

        }],
        arrows:true,
        prevArrow:'<div class="slick-prev"><i class="fas fa-chevron-left"></i></div>',
        nextArrow:'<div class="slick-next"><i class="fas fa-chevron-right"></i></div>',
    });
});

$(document).ready(function(){
    $("#testimonial-slider").owlCarousel({
        items:2,
        itemsDesktop:[1000,2],
        itemsDesktopSmall:[979,2],
        itemsTablet:[768,1],
        pagination:true,
        navigation:true,
        navigationText:['<i class="fas fa-chevron-left"></i>','<i class="fas fa-chevron-right"></i>'],
        autoPlay:true
    });
});