$(function() {
	$("#enter-tainers").submit(function( event ) {
		event.preventDefault();
	  $.post({
	  	url: '/',
	  	data: $('form').serialize(),
	  	success: function(response) {
			$(".processing-overlay").hide();
			$("#results").empty();
	  		$(".results-section").show();	
	  		if (response['success'] === 0) {
	  			console.log(response);
	  			$('#results').append('<p>Sorry, ' + response['error_msg'] + '</p>');
	  		} else {
				let people = '';
				const numNames = response.entertainers.length;
				console.log(numNames);
				for (const [i, dict] of response.entertainers.entries()) {
					const person = '<a target="_blank" href="' + dict.url  + '">' + dict.name + '</a>';
					if (i !== numNames - 1)
						people += person + ', ';
					else {
						const nameStrLen = people.length;
						people = people.slice(0, nameStrLen - 2);
						people += ' and ' + person + " worked on:";
					}
				}
				$('#entertainer-links').html(people);
				const imdb = "https://www.imdb.com/";
		  		$.each(response['crossing'], function(url, title) {
		  			$('#results').append('<a class="col-sm-6" target="_blank" href="' + imdb + url + '">' + title + '</a>');
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
