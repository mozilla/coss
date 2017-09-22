$(document).ready(function() {
    'use strict';

    $(window).bind('scroll', function () {
        if ($(window).scrollTop() > 300) {
            $('.navbar-brand img').hide();
            $('.navbar-brand img.sticky').show();
        } else {
            $('.navbar-brand img').show();
            $('.navbar-brand img.sticky').hide();
        }
    });
});
