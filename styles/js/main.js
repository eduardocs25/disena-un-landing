
$(document).ready(function(){
    $('section#pantallas a').on('click',function(){
        $('#modal img').attr('src',$(this).attr("data-image-url"));
    });
});