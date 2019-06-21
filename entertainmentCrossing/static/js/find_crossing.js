$(function() {
	$( "#enter-tainers" ).submit(function( event ) {
		event.preventDefault();
	  $.post({
	  	url: '/',
	  	data: $('form').serialize(),
	  	success: function(response) {
	  		$('.results').css("display", "block");
	  		$.each(response['crossing'], function(index, project) {
	  			$('#results').append(project);
	  			console.log(project);
	  		});
	  		
	  	},
	  	error: function(error) {
	  		console.log(error);
	  	}
	  })
	});
});
