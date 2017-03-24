function run($) {
  if(!$("#id_featured").is(':checked')) {
    $(".field-quote").hide();
    $(".field-bio").hide();
  }

  $("#id_featured").click(function() {
    $(".field-quote").toggle(this.checked);
    $(".field-bio").toggle(this.checked);
  });
}

django.jQuery(run.bind(django.jQuery));
