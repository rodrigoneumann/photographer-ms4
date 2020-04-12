/* SIDEBAR */
$(document).ready(function () {
    
    $('.close-menu, .overlay, .menu-link').on('click', function () {
        $('.sidebar').removeClass('active');
        $('.overlay').removeClass('active');
    });

    $('.open-menu').on('click', function (e) {
        e.preventDefault();
        $('.sidebar').addClass('active');
        $('.overlay').addClass('active');
    });
    
});