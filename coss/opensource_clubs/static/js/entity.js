$(document).ready(function() {
    'use strict';

    // Pick background image
    var bg_image = $('.jumbotron').data('bg-img');
    if (bg_image) {
        $('.jumbotron').css('background-image', 'url(' + bg_image + ')');
    }
});
