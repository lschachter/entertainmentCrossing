$(function() {
	$( "#enter-tainers" ).submit(function( event ) {
		event.preventDefault();
	  $.post({
	  	url: '/',
	  	data: $('form').serialize(),
	  	success: function(response) {
	  		$('.results-section').show()
	  		var imdb = "https://www.imdb.com/";
	  		$('#results-insert-hook').after("<h6>" + response['e1'] + " and " + response['e2'] + " both worked on:</h6>");
	  		$.each(response['crossing'], function(title, link) {
	  			$('#results').append('<a class="col-sm-6" href="' + imdb + link + '">'+title+'</a>');
	  		});
	  		
	  	},
	  	error: function(error) {
	  		console.log(error);
	  	}
	  })
	});
});
