$(function() {
	$( "#enter-tainers" ).submit(function( event ) {
	  alert( "Handler for .submit() called." );
	  console.log("Handler for .submit() called.")
	  event.preventDefault();

	  $.post('/', {  
	    entertainer1: $('#entertainer1').val(),
	    entertainer2: $('#entertainer2').val(),
	  }, function(data) {
	    $('#results').text(data.overlap);
	  });
	  return false;

	});
});