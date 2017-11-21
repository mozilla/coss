$(document).ready(function() {
    'use strict';

    // Smooth scrolling on nav links
    $('#nav-about a.nav-link[href*="#"]').click(function() {
        var target = $(this.hash);
        $('html, body').animate({
            scrollTop: target.offset().top
        });
    });

    // Details block nav
    $('#nav-details a.nav-link[href*="#"]').click(function(event) {
        event.preventDefault();
        var target = $(this.hash);
        $('#nav-details a.nav-link').removeClass('active');
        $(this).addClass('active');
        $('#details .nav-content').hide();
        $(target).show();
    });

    // Pick background image
    var bg_image = $('#body').data('bg-img');
    if (bg_image) {
        $('.body-image').css('background-image', 'url(' + bg_image + ')');
    }
});
