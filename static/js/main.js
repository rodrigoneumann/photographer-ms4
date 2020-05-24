$(document).ready(function () {
    
    /* Message Alert fade-out */
    $(".alert").delay(3000).slideUp(200, function () {
        $(this).alert('close');
    });

});