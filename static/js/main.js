$(document).ready(function () {
    
    /* Message Alert fade-out */
    $(".alert").delay(3000).slideUp(200, function () {
        $(this).alert('close');
    });

    /* Magnifc Popup */
    $('.photo-gallery').magnificPopup({
        delegate: 'a', // child items selector, by clicking on it popup will open
        type: 'image',
        gallery:{enabled:true}
      });

});