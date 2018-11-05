$(function () {
    $('.market').width(innerWidth)
    typeIndex = $.cookie('typeIndex')
    if (typeIndex) {
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    }else {
        $('.type-slider .type-item:first').addClass('active')
    }

    $('.type-item').click(function () {
        $.cookie('typeIndex',$.(this).index(),{expires:3,path:'/'})
        
    })

})