$(document).ready(function() {
    'use strict';

    // Pick background image
    var bg_image = $('#body').data('bg-img');
    if (bg_image) {
        $('.body-image').css('background-image', 'url(' + bg_image + ')');
    } else {
        $('.body-image').css('background-image', 'url(/static/img/alex-wong.jpg)');
    }
});
