$(document).ready(function() {
    'use strict';

    // Smooth scrolling on nav links
    $('#nav-about a.nav-link[href*="#"]').click(function() {
        var target = $(this.hash);
        $('html, body').animate({
            scrollTop: target.offset().top
        });
    });

    $('#nav-roles a.nav-link[href*="#"]').click(function() {
        var target = $(this.hash);
        $('#nav-roles a.nav-link').removeClass('active');
        $(this).addClass('active');
        $('#roles .nav-content').hide();
        $(target).show();
    });
});
