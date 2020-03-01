$(function() {
	$( "#enter-tainers" ).submit(function( event ) {
		event.preventDefault();
	  $.post({
	  	url: '/',
	  	data: $('form').serialize(),
	  	success: function(response) {
	  		$(".processing-overlay").hide();
	  		$('#results').empty();	
	  		$('.results-section').show();	
	  		if (response['success'] == 0) {
	  			console.log(response);
	  			$('#results').append('<p>Sorry, ' + response['error_msg'] + '</p>');
	  		} else {
		  		var imdb = "https://www.imdb.com/";
		  		var person1 = '<a target="_blank" href="' + response['e1'].url + '">' + response['e1'].name + '</a>'
		  		var person2 = '<a target="_blank" href="' + response['e2'].url + '">' + response['e2'].name + '</a>'
		  		$('#results-insert-hook').after("<h6>" + person1 + " and " + person2 + " both worked on:</h6>");
		  		$.each(response['crossing'], function(link, title) {
		  			$('#results').append('<a class="col-sm-6" target="_blank" href="' + imdb + link + '">' + title + '</a>');
		  		});
		  	}
	  	},
	  	error: function(error) {
	  		console.log(error);
	  		$('#results').append('<p>"Sorry, we ran into an error. Please try again: ' + error.error_msg + '</p>');
	  	}
	  })
	});
});

function countdown_clock() {
	var timeleft = 15;
	var downloadTimer = setInterval(function(){
	  document.getElementById("progress-bar").value = 15 - timeleft;
	  timeleft -= 1;
	  if(timeleft <= 0)
	    clearInterval(downloadTimer);
	}, 1000);
}

function show_overlay() {
	$(".processing-overlay").show();
	countdown_clock();
}
