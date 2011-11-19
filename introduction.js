$(function() {
	// Deck initialization
	$.deck('.slide');

  $(document).bind('deck.change', function(event, from, to) {
    
    //id = jQuery.deck('getSlide', to)[0].id
    //if (id.indexOf("chap") == 0)
    //{
    //  $('#decorator-top').fadeIn(1100);
    //  $('#decorator-bottom').fadeIn(1100);
    //}
    
    //else
    //{
    //  $('#decorator-top').hide();
    //  $('#decorator-bottom').hide();
    //};
    
    //alert('moving from slides '+from+' to '+to);
  });

	$('#style-themes').change(function() {
		$('#style-theme-link').attr('href', $(this).val());
	});
	
	$('#transition-themes').change(function() {
		$('#transition-theme-link').attr('href', $(this).val());
	});
});

